import time
import collections
import flask
import flask_socketio

MAX_MESSAGES = 25

INDEX_PAGE = "/"
INDEX_SOURCE = "index.html"
NAME = "name"
MESSAGE = "message"
MESSAGES = "messages"

app = flask.Flask(__name__)
messages = collections.deque()
app.config['SECRET_KEY'] = 'secret!'
socketio = flask_socketio.SocketIO(app)

@app.route(INDEX_PAGE)
def index():
    return flask.render_template(INDEX_SOURCE)

@socketio.on("message")
def push_and_pull(json):
    name = json.get(NAME)
    message = json.get(MESSAGE)
    
    if name and message:
        messages.appendleft((
            time.asctime(),
            name,
            message
        ))
        
        if len(messages) > MAX_MESSAGES:
            messages.pop()
        
        flask_socketio.send({MESSAGES: list(messages)}, json = True, broadcast = True)

if __name__ == "__main__":
    socketio.run(app)