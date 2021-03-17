from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room
from flask_cors import CORS
from NineXOGameManager import NineXOGameManager

app = Flask(__name__)
#change this in prod
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

gameManager = NineXOGameManager(300)

@socketio.on('connect')
def connect():
    print("Someone connected to websocket!")

@socketio.on('create')
def createGame(object):
    gid = gameManager.createGame()
    dest = "/" + gid
    socketio.emit('createResponse', dest, room=request.sid)
    print("Game created! gid=" + gid)

@socketio.on('join')
def joinGame(object):
    #need a try/catch here 
    gid = object['gid']
    role = gameManager.addPlayer(gid, request.sid)
    join_room(gid)

    socketio.emit('joinResponse', True)
    socketio.emit('role', role, room=request.sid)
    socketio.emit('message',{"username":"System", "content": "You are " + role}, room=request.sid)

    #This is a kludge; fix later
    #in fact, a lot of this needs refactoring
    if (role == 'O'):
        socketio.emit('turn', 'X')
    
@socketio.on('disconnect')
def disconnect():
    gameManager.removePlayer(request.sid)
    print("Player disconnected!")

@socketio.on('post_submit')
def message(object):
    gid = object['gid']
    username = object['username']
    content = object['content']
    socketio.emit('message',{"username":username, "content":content}, room=gid)

@socketio.on('click')
def click(object):
    gid = object['gid']

    gameMeta = gameManager.get_game(gid)

    try:
        newStateDict = gameMeta.handleClick(request.sid, object)
        socketio.emit('state', newStateDict, room=gid)

if __name__ == '__main__':
    socketio.run(app, port=1337, debug=True, host='0.0.0.0')
