
import sqlite3

from flask import Flask, render_template, g, request, redirect
app = Flask(__name__)

DATABASE = 'my_database.db'


@app.route('/')
def index():
    posts = query_db('select * from my_posts')
    return render_template('index.html', posts=posts)


@app.route('/start_post')
def form_post():
    return render_template('add_post.html')


@app.route('/write_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    post = {'id': 'null', 'title': title, 'content': content}
    insert_post(post)
    return redirect('/')


# delete items from the database
# using their 'id'
@app.route('/delete_post/<int:id>', methods = ['POST'])
def remove_post(id=0):
    delete_post(id)
    return redirect('/')


def delete_post(id):
    cur = g.db.execute('delete from my_posts where(id == "%s");' % (
        id,
        ))
    g.db.commit()


# insert a 'post' into the database
def insert_post(post):
    cur = g.db.execute('insert into my_posts values(%s,"%s","%s");' % (
        post['id'],
        post['title'],
        post['content'],
        ))
    g.db.commit()


# take a 'query' string and execute it
def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv


# connect to the database
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
        debug=True,
    )
