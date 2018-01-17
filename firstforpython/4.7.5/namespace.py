
animal = "fruitbats"

def print_global():
    print('inside print_global : ', animal)

def change_and_print_global():
    global animal
    print('inside change_and_print_global : ', animal)

print('globals :', globals())