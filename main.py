from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, static_folder='assets')
app.config['SECRET_KEY'] = 'supersecret'

socketio= SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('chat_event')
def handle_chat_event(json, methods=['GET', 'POST']):
    print('received chat event: ' + str(json))
    socketio.emit('server_response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)
