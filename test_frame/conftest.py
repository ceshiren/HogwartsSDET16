import os
import subprocess

import pytest


@pytest.fixture(scope='function')
def record_vedio(request):
    cmd = "scrcpy --record " + request.param
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.popen('taskkill.exe/pid:' + str(p.pid))
