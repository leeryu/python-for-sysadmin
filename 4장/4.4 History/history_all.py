from exec_cmd import *
from user_list import *
from datetime import datetime

def remove_num(string):
    tmp = string.strip()
    first_space = tmp.find(" ")
    if first_space < 0:
        return string
    
    tmp = tmp[first_space : len(tmp)]
    return tmp

def history(account):
    ret = exec_cmd_process("sudo -H -u  %s bash -i -c 'history -r;history'" % account)
    ret_str = ret.decode("utf-8")
    ret_split = ret_str.strip().split("\n") 

    i = len(ret_split) - 1
    
    history_list = []
    while i > 0:
        cmd = ret_split[i].strip()
        i = i - 2
        # 명령을 cmd 변수에, 타임스탬프를 timestamp 변수로 추출
        cmd = remove_num(cmd) 
        history_list.append(cmd)

    return history_list

if __name__ == "__main__":
    accounts = get_accounts()
    for account in accounts:
        account_str = account.decode("utf-8")
        print("계정 : " + account_str)
        history_list = history(account_str)
        if len(history_list) == 0:
            print("\t기록된 이력없음")

        for h in history_list:
            print(h)
        print("-" * 70)    






