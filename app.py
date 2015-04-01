from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    posts = [
        {'title': 'How to start a flask app', 'content': 'Here is some info about how to start creating flask apps'},
        {'title': 'Add to a form', 'content': "Let's add something to this!"},
        ]
    return render_template('index.html',posts=posts)

if __name__ == '__main__':
    app.run(
        host="127.0.0.1", 
        port=8000,
        debug=True
        )
