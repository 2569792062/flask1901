from flask import Flask,render_template,url_for
app = Flask(__name__)

@app.route('/')
def index():
    name='王涵'
    movies=[
        {'title':'王涵','year':20}

    ]
    return render_template('index.html',name=name,movies=movies)

@app.route('/index/<conn>')
def con(conn):
    print(url_for('index',n=conn))

    return 'hello %s'%conn
