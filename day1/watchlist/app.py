import os
import sys
import click

from flask import Flask,render_template

from flask import url_for

from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# 注册命令
@app.cli.command()
@click.option('--drop',is_flag=True,help='Create after drop')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库.....')

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

@app.cli.command()
def forge():
    name='王涵'
    movies=[
        {'title':'杀破狼1','year':20},
        {'title':'西游记1','year':20},
        {'title':'分手大师1','year':20},
        {'title':'釜山行1','year':20},
        {'title':'机器之血1','year':20},
        {'title':'扫毒21','year':20},
        {'title':'战狼1','year':20},
        {'title':'战狼21','year':20},
        {'title':'叶问11','year':20},
        {'title':'叶问21','year':20},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        print(m)
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('导入数据库完成.')

    
@app.route('/')
def index():
    # user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html',movies=movies)

#处理页面404错误
@app.route('/index/<conn>')
def con(conn):
    print(url_for('index',n=conn))

    return 'hello %s'%conn

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



#模板上下文处理函数,再多个模板内部需要使用的变量
@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)