from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO

from inmem_repo import UserRepo, QuestionRepo
from use_cases import GetAllUsersUseCase, GetUserDetailUseCase, AskQuestionUseCase, GetAllQuestionsUseCase

app = Flask(__name__, static_folder='assets')
app.config['SECRET_KEY'] = 'supersecret'

socketio= SocketIO(app)

userRepo = UserRepo()
questionRepo = QuestionRepo()

userRepo.create('Zoey')
userRepo.create('Mal')
userRepo.create('Kaylee')
userRepo.create('Wash')

@app.route('/users', methods=['GET'])
def get_all_users():
    uc = GetAllUsersUseCase(userRepo)
    result = {'output': uc.execute()}

    return jsonify(result)

@app.route('/questions')
def get_all_questions():
    uc = GetAllQuestionsUseCase(questionRepo)
    result = {'output': uc.execute()}

    return jsonify(result)

@app.route('/')
def index():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('connected_event')
def handle_chat_event(json, methods=['GET', 'POST']):
    print("user connected")
    socketio.emit('server_response', json, callback=messageReceived)

    
@socketio.on('chat_event')
def handle_chat_event(json, methods=['GET', 'POST']):
    user_id = json['user_id']
    uc = GetUserDetailUseCase(userRepo)
    user = uc.execute(user_id)
    json['username'] = user['display_name']
    socketio.emit('server_response', json, callback=messageReceived)

@socketio.on('question_event')
def handle_question_event(json, methods=['GET', 'POST']):
    user_id = json['user_id']
    question_text = json['message']
    userUC = GetUserDetailUseCase(userRepo)
    user = userUC.execute(user_id)
    print("=======")
    print(json)
    print(user)
    print("=======")
    json['username'] = user['display_name']

    questionUC = AskQuestionUseCase(questionRepo)
    result = questionUC.execute(question_text, user_id)
    json['question_asked'] = True
    socketio.emit('server_response', json, callback=messageReceived)
    pass
        
if __name__ == '__main__':
    socketio.run(app, debug=True)
