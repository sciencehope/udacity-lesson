from flask import Flask, render_template, abort, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:abc@localhost:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)

  def __repr__(self):
    return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/')
def index():
  return render_template('index.html', data=Todo.query.all())

@app.route('/todos/create', method=['POST'])
def create_todo():
  error = False
  body = {}
  try:
    description = request.get_json()['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    body['description'] = todo.description
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  if not error:
    return jsonify({body})

#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=3000)

# FLASK_APP=app.py FLASK_DEBUG=true flask run