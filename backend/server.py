from flask import Flask
from flask import request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config["testcase"] = []


class TestCaseServer(Resource):
    def get(self):
        if "id" in request.args:
            # 从用例库中找对应的用例
            for i in app.config["testcase"]:
                # 返回用例
                if i["id"] == int(request.args["id"]):
                    print(i)
                    return i
        else:
            return app.config["testcase"]

    def post(self):
        """
        每条 testcase 要有 id, description ，steps
        :return:
        """
        if "id" not in request.json:
            return {"result": "error", "errcode": "404", "errmessage": "need testcase id"}
        app.config["testcase"].append(request.json)
        return {"result": "ok", "errcode": "0"}


api.add_resource(TestCaseServer, '/testcase')

if __name__ == "__main__":
    app.run(debug=True)
