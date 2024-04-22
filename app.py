from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, User

app = Flask(__name__)

DB_NAME = "database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Set a secret key for the session
app.secret_key = 'muhammad419#'

@app.route("/submit", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        firstName = request.form.get('first_name')
        lastName = request.form.get('last_name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        unique = request.form.get('unique_number')
        email = request.form.get('email')
        num = request.form.get('phone_number')
        reason = request.form.get('reason')
        famHist = request.form.get('family_history')
        severity = request.form.get('severity')
        
        if len(unique) < 6:
            flash('Incorrect Number!', category='error')
        elif len(email) < 4:
            flash('Email is incorrect!', category='error')
        else:
            new_user = User(firstName=firstName, lastName=lastName, age=age, gender=gender, unique_num=unique,
                            email=email, ph_num=num, reason=reason, fam_history=famHist, severity=severity)
            db.session.add(new_user)
            db.session.commit()
            flash('Form submitted successfully!')
    return render_template("index.html")

@app.route("/", methods=["GET"])
def push():
    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(port=5500, debug=True)
