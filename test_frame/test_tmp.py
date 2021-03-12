import os
import subprocess
from time import sleep

import pytest


class TestRecord():
    # def setup(self, request):
    #     cmd = "scrcpy --record " + request.param['name']
    #     p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #     print(p)
    #     sleep(5)
    #     os.popen('taskkill.exe/pid:' + str(p.pid))
    @pytest.mark.parametrize('record_vedio',['hello.mp4'],indirect=True )
    def test_record(self, record_vedio):

        print("hello")

    @pytest.mark.parametrize('record_vedio', ['hello2.mp4'], indirect=True)
    def test_record_2(self, record_vedio):
        print("hello")

    def test_record_3(self):
        print("hello")
