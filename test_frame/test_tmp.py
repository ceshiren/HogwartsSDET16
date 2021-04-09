from time import sleep

import pytest

from test_frame.logger import log_init, log


class TestRecord():
    def setup_class(self):
        log_init()
    # def setup(self, request):
    #     cmd = "scrcpy --record " + request.param['name']
    #     p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #     print(p)
    #     sleep(5)
    #     os.popen('taskkill.exe/pid:' + str(p.pid))
    @pytest.mark.parametrize('record_vedio',['hello.mp4'],indirect=True )
    def test_record(self, record_vedio):
        log.debug("hello")
        sleep(3)

    @pytest.mark.parametrize('record_vedio', ['hello2.mp4'], indirect=True)
    def test_record_2(self, record_vedio):
        log.debug("hello")
        sleep(3)


