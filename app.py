# This is your library
#hi my name is gem
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# This initiates the flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)


# Database Class 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String)


# Todo class
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String)
    complete = db.Column(db.Boolean)

# We are telling flask where to go for home page
@app.route('/', methods=['GET'])
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/new_todo', methods=['POST'])
def new_todo():
    if (request.method == 'POST'):
        todo_text = request.form['todo']
        new_todo = Todo(item=todo_text, complete=False)
    
        try: 
            db.session.add(new_todo)
            db.session.commit()
            return redirect('/')   
        except: 
            return "Something went wrong adding your todo item" 

    return render_template('index.html')       


@app.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    item = Todo.query.get_or_404(id)
    item.complete = True
    db.session.commit()
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    item = Todo.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/')

@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/about')
def about():
    return render_template('about.html')

# Runs your flask app
if (__name__ == "__main__"):
    app.run(debug=True)
