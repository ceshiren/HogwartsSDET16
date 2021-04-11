import os

from flask import Flask
from flask import request
from flask_restful import Resource, Api, abort
from flask_sqlalchemy import SQLAlchemy
from jenkinsapi.jenkins import Jenkins

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tmp:ceshiren.com@182.92.129.158/tmp?charset=utf8mb4'
db = SQLAlchemy(app)
app.config["testcase"] = []


class TestCaseTable(db.Model):
    """
    存储用例
    """
    name = db.Column(db.String(80), primary_key=True)
    description = db.Column(db.String(80), unique=False, nullable=True)
    file_name = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(300), unique=False, nullable=False)
    report = db.relationship('Report', backref='test_case_table', lazy=True)

    def __repr__(self):
        return '<TestCase %r>' % self.name


class Report(db.Model):
    """
    存储用例
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), unique=False, nullable=True)
    dir = db.Column(db.String(300), unique=False, nullable=False)
    testcase_id = db.Column(db.String(80), db.ForeignKey('test_case_table.name'), nullable=False)


    def __repr__(self):
        return '<TestCase %r>' % self.name


class TestCaseStore(Resource):
    def post(self):
        """
        存储用例
        :return:
        """
        if "file" in request.files and "name" in request.form:
            f = request.files["file"]
            name = request.form['name']
            file_name = f.filename
            content = f.read()
            testcase = TestCaseTable(name=name, file_name=file_name, content=content)
            db.session.add(testcase)
            db.session.commit()
            return "OK"
        # 返回不同的状态码，和默认的错误页
        abort(404)


@app.route("/get_testcase", methods=['get'])
def get_testcase():
    """
    存储用例
    :return:
    """
    if "name" in request.args:
        # 通过 name ，指定要运行的用例
        name = request.args['name']
        testcase = TestCaseTable.query.filter_by(name=name).first()
        return testcase.content
    abort(404)


@app.route("/run", methods=['get'])
def run():
    if "name" in request.args:
        name = request.args['name']
        testcase = TestCaseTable.query.filter_by(name=name).first()
        J = Jenkins('http://182.92.129.158:8080/', username="yuruotong1", password="111823a182b8df84e96efaa668f02100b7")
        print(J.keys())
        J["cekai16"].invoke(build_params={"name": name, "file_name": testcase.file_name})
        return "OK"


@app.route("/report_upload", methods=['post'])
def report_upload():
    if "file" in request.files and "name" in request.form:
        DIR = r"C:\Users\yuruo\Desktop\main\tmp"
        f = request.files["file"]
        name = request.form['name']
        file_name = f.filename
        dir = os.path.join(DIR, file_name)
        f.save(dir)
        report = Report(dir=dir, testcase_id=name)
        db.session.add(report)
        db.session.commit()
        return "OK"


api.add_resource(TestCaseStore, '/store')

if __name__ == "__main__":
    app.run(debug=True)
    # # db.drop_all()
    # db.create_all()