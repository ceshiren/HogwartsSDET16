from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api, abort
from flask_sqlalchemy import SQLAlchemy
from jenkinsapi.jenkins import Jenkins

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tmp:ceshiren.com@182.92.129.158/tmp?charset=utf8mb4'
db = SQLAlchemy(app)
app.config["testcase"] = []


class TestCaseTable(db.Model):
    """
    存储用例
    """
    # 用例的唯一标识：没有任何含义
    id = db.Column(db.Integer, primary_key=True)
    # 用例的唯一标识；但是具有物理含义（使用 nodeid 可以运行用例）
    nodeid = db.Column(db.String(80), unique=True, nullable=False)
    # 描述信息
    description = db.Column(db.String(1024), unique=False, nullable=True)

    def as_dict(self):
        return {"id": self.id, "nodeid": self.nodeid, "description": self.description}

    def __repr__(self):
        return '<TestCase %r>' % self.nodeid


class Task(db.Model):
    """
    存储用例
    """
    # 任务的唯一标识：没有任何含义
    id = db.Column(db.Integer, primary_key=True)
    # 描述信息
    description = db.Column(db.String(1024), unique=False, nullable=True)


class TaskJoinTestcase(db.Model):
    """
    存储用例
    """
    # 唯一标识：没有任何含义
    id = db.Column(db.Integer, primary_key=True)
    # task id
    task_id = db.Column(db.String(80), unique=False, nullable=False)
    # testcase id
    testcase_id = db.Column(db.String(80), unique=False, nullable=False)


# class Report(db.Model):
#     """
#     存储用例
#     """
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(80), unique=False, nullable=True)
#     dir = db.Column(db.String(300), unique=False, nullable=False)
#     testcase_id = db.Column(db.String(80), db.ForeignKey('test_case_table.name'), nullable=False)
#
#     def __repr__(self):
#         return '<TestCase %r>' % self.name


class TestCase(Resource):
    def post(self):
        """
        存储用例
        :return:
        """
        testcase = TestCaseTable(**request.json)
        db.session.add(testcase)
        db.session.commit()
        return "OK"

        # 返回不同的状态码，和默认的错误页
        abort(404)

    def put(self):
        """
        更新用例
        :return:
        """
        if "name" in request.json:
            testcase = TestCaseTable.query.filter_by(name=request.json.get('name')).first()
            testcase.content = request.json.get("content")
            testcase.description = request.json.get("description")
            testcase.file_name = request.json.get("file_name")
            db.session.commit()
            return {"errcode": 0, "content": "OK"}


class CreateTask(Resource):
    """
    用于生成任务
    """

    def post(self):
        """
        创建任务
        :return:
        """
        # 请任务的 id 放到 url 的参数中
        id = request.args.get("id")
        # 将任务的描述信息放到请求体中
        description = request.json.get("description")
        testcase = Task(id=id, description=description)
        db.session.add(testcase)
        db.session.commit()
        return "OK"


class TaskServe(Resource):
    """
    处理任务和用例的关系
    """

    def post(self):
        """
        存储用例
        :return:
        """
        # 把任务跟用例对应
        testcase = TaskJoinTestcase(**request.json)
        db.session.add(testcase)
        db.session.commit()
        return "OK"


class Login(Resource):
    def post(self):
        """
        存储用例
        :return:
        """
        print(request.json)
        if "ceshiren.com" in request.json.get("account") and "123456" == request.json.get("password"):
            return {"msg": "OK"}
        else:
            return {"msg": "ERROR"}


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
    return {"errcode": 0, "body": [i.as_dict() for i in TestCaseTable.query.all()]}


@app.route("/run", methods=['get'])
def run():
    if "name" in request.args:
        name = request.args['name']
        testcase = TestCaseTable.query.filter_by(name=name).first()
        J = Jenkins('http://182.92.129.158:8080/', username="yuruotong1", password="111823a182b8df84e96efaa668f02100b7")
        print(J.keys())
        J["cekai16"].invoke(build_params={"name": name, "file_name": testcase.file_name})
        return "OK"


@app.route("/run_task", methods=['get'])
def run_task():
    if "task_id" not in request.args:
        return "ERROR no task id"
    task_id = request.args.get("task_id")
    # 根据 task_id 从 task 和 testcase 的中间表中查询要运行的所有 testcase_id
    task_join_testcases = TaskJoinTestcase.query.filter_by(task_id=task_id).all()
    nodeids = []
    # 根据 testcase_id 查找 nodeid
    for task_join_testcase in task_join_testcases:
        testcase_id = task_join_testcase.testcase_id
        testcase = TestCaseTable.query.filter_by(id = testcase_id).first()
        nodeids.append(testcase.nodeid)
    # 组装成 pytest 命令，传递给 Jenkins 运行
    command = "pytest " + " ".join(nodeids)
    J = Jenkins('http://182.92.129.158:8099', username="yuruotong1", password="1136cecc6013e701058f5915d4009cb335")
    J["tmp"].invoke(build_params={"command": command})

    # 从测试用例表中，提取 nodeid

    return {"err_code": 0, "err_msg": "OK"}
    # J = Jenkins('http://182.92.129.158:8080/', username="yuruotong1", password="111823a182b8df84e96efaa668f02100b7")
    # print(J.keys())
    # J["cekai16"].invoke(build_params={"name": name, "file_name": testcase.file_name})
    # return "OK"

#
# @app.route("/report_upload", methods=['post'])
# def report_upload():
#     if "file" in request.files and "name" in request.form:
#         DIR = r"C:\Users\yuruo\Desktop\main\tmp"
#         f = request.files["file"]
#         name = request.form['name']
#         file_name = f.filename
#         dir = os.path.join(DIR, file_name)
#         f.save(dir)
#         report = Report(dir=dir, testcase_id=name)
#         db.session.add(report)
#         db.session.commit()
#         return "OK"


api.add_resource(TestCase, '/testcase')
api.add_resource(Login, '/login')
api.add_resource(TaskServe, '/task')
api.add_resource(CreateTask, '/create_task')
if __name__ == "__main__":
    app.run(debug=True)
    # db.drop_all()
    # db.create_all()
