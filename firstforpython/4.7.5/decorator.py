import curses

# *args와 **kargs
# 내부함수 
# 함수인자

def document_it(func):
    '''
    함수 이름과 인자값을 출력
    인자로 함수를 실행
    결과를 출력
    수정된 함수를 사용할 수 있도록 반환한다.
    '''
    def new_func(*args, **kargs):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kargs)
        result = func(*args, **kargs)
        print('Result : ', result)
        return result
    return new_func

@document_it
def add_ints(a, b):
    return a + b

def str_it(func):
    def new_func(name=''):
        print("-" * 70)
        result = func(name)
        print(result)
        print("-" * 70)
        return result
    return new_func 


@str_it
def str_deco(value=''):
    return value.capitalize() + "!"

v = str_deco('hi guys')

print(type(v))

# cooler_add_ints = document_it(add_ints) #
# print(cooler_add_ints(3, 5))
# print(add_ints(10, 5))
