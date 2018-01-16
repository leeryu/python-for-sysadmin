import os 

print("어떤 파이썬 서버에 연결하시겠습니까?")

while True:
    print("1. python1 ")
    print("2. python2 ")
    select = input("선택(1,2)  : ")

    if select == '1':
        os.system("ssh 121.126.218.207")
        break
    if select == '2':
        os.system("ssh 218.153.6.218")
        break
    if select == 'q':
        break
    else:
        print("not")    
        continue
