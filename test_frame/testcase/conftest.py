import os
import signal
import subprocess

import pytest


@pytest.fixture(scope='module', autouse=True)
def record_vedio():
    cmd = "scrcpy --record file.mp4"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)

