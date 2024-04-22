from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum('Male','Female','Other','Prefer not to say'), nullable=False)
    unique_num = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(150), unique=True)
    ph_num = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(250), nullable=False)
    fam_history = db.Column(db.Enum('Yes', 'No'))
    severity = db.Column(db.Enum('Routine','Moderate','Mild','Urgent','Severe','Emergency'), nullable=False)

    