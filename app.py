# pip3 install fask
# pip3 install flask_sqlalchemy
# pip3 install Flask-Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from alembic import op
# from sqlalchemy import sa
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  def __repr__(self):
    return f'<Person ID: {self.id}, name: {self.name}>'


# db.create_all() #If we use migration, we don't specify create_all here anymore

@app.route('/')

def index():
  return 'Hello World!'

#This code goes at the bottom of your flask Python file(this is actually your server)
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)

# Run on terminal
# flask db init #init the migration and create a bunch of file
# flask db migrate # launch migration, before we need to dropdb and recreat db using createdb
# flask db upgrade or flask db downgrade # Run the migration file and apply change to our db