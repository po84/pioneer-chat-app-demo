from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO

from inmem_repo import UserRepo
from use_cases import GetAllUsers, GetUserDetail

app = Flask(__name__, static_folder='assets')
app.config['SECRET_KEY'] = 'supersecret'

socketio= SocketIO(app)

userRepo = UserRepo()

userRepo.create('Zoey')
userRepo.create('Mal')
userRepo.create('Kaylee')
userRepo.create('Wash')

@app.route('/users', methods=['GET'])
def get_all_users():
    uc = GetAllUsers(userRepo)
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
    uc = GetUserDetail(userRepo)
    user = uc.execute(user_id)
    json['username'] = user['display_name']
    socketio.emit('server_response', json, callback=messageReceived)
        
if __name__ == '__main__':
    socketio.run(app, debug=True)
