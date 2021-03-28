from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room
from flask_cors import CORS
from NineXOGameManager import NineXOGameManager
from GameManager import GameNotAvailibleException
import logging

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
    gid = object['gid']

    try:
        role = gameManager.addPlayer(gid, request.sid)
        join_room(gid)
    except(GameNotAvailibleException):
        socketio.emit('joinResponse', False, room=request.sid)
        return

    socketio.emit('joinResponse', True)
    socketio.emit('role', role, room=request.sid)
    socketio.emit('message',{"username":"System", "content": "You are " + role}, room=request.sid)

    if gameManager.getGame(gid).gameReady():
        newStateDict = gameManager.getGame(gid).getStateDict()
        socketio.emit('start_game', newStateDict, room=gid)
    
@socketio.on('disconnect')
def disconnect():
    gameManager.removePlayer(request.sid)
    print("Player disconnected!")

@socketio.on('timeout_check')
def checkTimeout():
    for gid in gameManager.getTimeout():
        socketio.emit('timeout', room=gid)
        socketio.close_room(gid)
        gameManager.cleanUpGame(gid)

@socketio.on('post_submit')
def message(object):
    gid = object['gid']
    username = object['username']
    content = object['content']
    socketio.emit('message',{"username":username, "content":content}, room=gid)

@socketio.on('click')
def click(object):
    gid = object['gid']

    gameMeta = gameManager.getGame(gid)

    try:
        newStateDict = gameMeta.handleClick(request.sid, object)
        socketio.emit('state', newStateDict, room=gid)
    except Exception as e:
        print(e)
        return

if __name__ == '__main__':
    socketio.run(app, port=1337, debug=True, host='0.0.0.0')
