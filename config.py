from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_path = "./db/"
db_file = "database.db"
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path + db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

session = db.session

