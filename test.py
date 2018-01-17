

def is_none(thing):
    if thing is None:
        print("It is a None")
    elif thing:
        print("it is true")
    else:
        print("it is false")

def menu(menu_name="left"):
    print(menu_name)

def buggy(args, result=[]):
    result.append(args)
    return result

def print_more(*args):
    print(type(args))
    print(args)

if __name__ == '__main__':
    print_more(1,2,3, ["ddd", "aaa"])

