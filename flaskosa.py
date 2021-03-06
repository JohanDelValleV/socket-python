from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')