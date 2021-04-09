import os
import signal
import subprocess

import allure
import pytest


@pytest.fixture(scope='module', autouse=True)
def record_vedio(request):
    cmd = "scrcpy --record tmp.mp4"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    p.send_signal(signal.CTRL_C_EVENT)
    allure

