from subprocess import *
import subprocess
import os
import sys

#
def exec_cmd_sys(cmd):
    os.system(cmd)

#
def exec_cmd_call(cmd):
    subprocess.call(cmd, shell=True)

#
def exec_cmd_process(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    (ret, err) = p.communicate()
    return ret

#
def exec_cmd_check_output(cmd):
    return subprocess.check_output(cmd, shell=True)


