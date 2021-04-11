from jenkinsapi.jenkins import Jenkins


def test_jenkins():
    J = Jenkins('http://182.92.129.158:8080/',username="yuruotong1", password="111823a182b8df84e96efaa668f02100b7")
    print(J.keys())
    J["cekai16"].invoke(build_params={"name": "tmp", "file_name": "tmp.py"})