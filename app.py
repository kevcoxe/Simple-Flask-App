import sqlite3
from flask import Flask, render_template, g, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

DATABASE = 'flask_db.db'

@app.route('/')
def index():
    posts = query_db('select * from flask_posts')
    return render_template('index.html',posts=posts)

@app.route('/start_post')
def form_post():
    return render_template('add_post.html')

@app.route('/write_post', methods = ['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    post = {'id':'null','title':title,'content':content}
    insert_post(post)
    return redirect('/')

@app.route('/delete_post/<int:id>', methods = ['POST'])
def remove_post(id=0):
    cur = g.db.execute('delete from flask_posts where(id == "%s");' % (
        id,
        ))
    g.db.commit()
    return redirect('/')

def insert_post(post):
    cur = g.db.execute('insert into flask_posts values(%s,"%s","%s");' % (
        post['id'],
        post['title'],
        post['content'],
        ))
    g.db.commit()

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.after_request
def after_request(response):
    g.db.close()
    return response

if __name__ == '__main__':
    app.run(
        host="127.0.0.1", 
        port=8000,
        debug=True
        )
