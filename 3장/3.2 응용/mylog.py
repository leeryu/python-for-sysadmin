#-.*- coding: utf-8 -*-
import codecs

# 인자를 5개로 수정
def printlog(logfile, search_word, start_index, pre_rowcount, next_rowcount):
    f = open(logfile, "r", -1, "utf-8")
    logdata = f.read()
    f.close()

    # 코드 수정시작
    index = logdata.find(search_word, start_index)
    # 코드 수정 완료
    
    if index >= 0:
        print("-" * 70)
        print("Log file : ", logfile)
        print("Find this word : ", search_word)
        print("-" * 70)
        # 
        (data, count) = get_log_data(logdata, search_word, index, pre_rowcount, next_rowcount)
        print(data)
        print(count)
        print("-" * 70)

def get_log_data(logdata, search_word, start_index, pre_rowcount, next_rowcount):
    count = 0
    ret = ""

    while start_index >= 0:
        enter_index = max(0, logdata.rfind("\n", 0, start_index))
        for i in range(0, pre_rowcount):   
            enter_index = max(0, logdata.rfind("\n", 0, enter_index))

        enter_index2 = max(0, logdata.find("\n", start_index, len(logdata)))
        for i in range(0, next_rowcount):
            last_end_index = max(0, logdata.find("\n", enter_index2 + 1, len(logdata)))
            if last_end_index == -1:
                last_end_index = enter_index2
                break
            else: 
                enter_index2 = last_end_index 

        ret = ret + logdata[enter_index : enter_index2]
        ret = ret + "\n" + ("-" * 80)

        # 한 번 출력한 로그의 마지막 줄 바꿈 위치(enter_index2) 뒤부터 찾고자 하는 단어를 찾습니다.
        # 따라서 index가 재조정되며 여러 번 반복한 다음에는 index가 -1이 되어 while 문을 종료합니다.
        start_index = logdata.find(search_word, enter_index2 + 1)
        count = count + 1

    return (ret, count)

# if __name__ == '__main__':
#     printlog("D://aaaaaa.log", "leesanguck", 0, 0, 5)

