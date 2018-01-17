

def answer():
    print(42)

def run_something(func):
    func()

def add_args(arg1, arg2):
    print(arg1 + arg2)

def sum_args(*args):
    return sum(*args)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

def run_with_positional_args(sum_args, *args):
    print(sum_args(args))

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

def knights(saying):
    def inner(quote):
        return "inner print '%s'" % quote 
    return inner(saying)

print(knights("ssssss"))

