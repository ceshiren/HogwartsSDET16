def test_sqlalchemy():
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tmp_hello:ceshiren.com@182.92.129.158/tmp123?charset=utf8mb4'
    db = SQLAlchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return '<User %r>' % self.username

    class UserAbc(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return '<User %r>' % self.username4
    db.session.add(User(id=1234, username="xiaohong", email="abc@163.com"))
    db.session.commit()