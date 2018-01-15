import mylog


# docstring
def main():
    loop = True
    while loop:
        print("\n")
        print("-" * 70)
        print("종료하실려면 q나 -1를 입력해 주세용.")
        print("-" * 70)
        input_num = input("로그파일 명을 입력해주세요. : ")
        if input_num == "q" :
            print("종료되었습니다.^^")
            loop = False
        elif len(input_num) > 0:   
            __loop__ = True
            while __loop__:  
                print("=" * 70)
                print("단어종료를 하실려면 q나 -1를 입력해 주세용.")
                input_keyword = input("찾을 단어를 입력해 주세요. : ")
                if input_keyword == "q":
                    print("파일명 찾기로 이동합니당^^")
                    __loop__ = False
                elif len(input_keyword) > 0:    
                    mylog.printlog(input_num, input_keyword, 0, 3, 5)
                else:
                    print("단어를 입력해 주세용^^.....")
        else:
            print("파일명을 입력해 주세용....")

if __name__ == '__main__':
    main()