from user_list import *
from datetime import datetime

def history(account):
    # 이력 조회를 위한 명령어 실행
    ret = exec_cmd("sudo -H -u %s bash -i -c 'history -r;history'" % account)
    ret_split = ret.split().split("\n")
    i = len(ret_split) - 1


    
