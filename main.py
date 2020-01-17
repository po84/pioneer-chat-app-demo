from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO

from inmem_repo import UserRepo, QuestionRepo, AnswerRepo
from use_cases import GetAllUsersUseCase, GetUserDetailUseCase, AskQuestionUseCase, GetAllQuestionsUseCase, AnsweringQuestionUseCase, GetAllAnswersUseCase

app = Flask(__name__, static_folder='assets')
app.config['SECRET_KEY'] = 'supersecret'

socketio= SocketIO(app)

userRepo = UserRepo()
questionRepo = QuestionRepo()
answerRepo = AnswerRepo()

# inserting some "users"
userRepo.create('Zoey')
userRepo.create('Mal')
userRepo.create('Kaylee')
userRepo.create('Wash')

@app.route('/users', methods=['GET'])
def get_all_users():
    uc = GetAllUsersUseCase(userRepo)
    result = {'output': uc.execute()}

    return jsonify(result)

# for debugging purpose
@app.route('/questions')
def get_all_questions():
    uc = GetAllQuestionsUseCase(questionRepo)
    result = {'output': uc.execute()}

    return jsonify(result)

# for debugging purpose
@app.route('/answers')
def get_all_answers():
    uc = GetAllAnswersUseCase(answerRepo)
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
    json['username'] = user['display_name']

    questionUC = AskQuestionUseCase(questionRepo)
    question = questionUC.execute(question_text, user_id)
    json['question_id'] = question['id']

    socketio.emit('server_response', json, callback=messageReceived)
    
@socketio.on('answer_event')
def handle_answer_event(json, methods=['GET', 'POST']):
    user_id = json['user_id']
    answer_text = json['message']
    question_id = json['question_id']

    userUC = GetUserDetailUseCase(userRepo)
    user = userUC.execute(user_id)
    json['username'] = user['display_name']

    answerUC = AnsweringQuestionUseCase(answerRepo)
    answer = answerUC.execute(answer_text, user_id, question_id)
    json['answer_id'] = answer['id']

    socketio.emit('server_response', json, callback=messageReceived)
        
if __name__ == '__main__':
    socketio.run(app, debug=True)
