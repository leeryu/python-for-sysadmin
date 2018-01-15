import os

print("어떤 파이썬 서버에 연결하시겠습니까?")
select = input("연결하고 하는 파이썬 서버를 선택하세요(1,2) : ")

if select == 1:
    os.system("ssh 218.153.6.218")
elif select == 2:
    os.system("ssh 121.126.218.207")
else:
    print("not 1 or 2 프로그램을 다시 시작해주세요.")