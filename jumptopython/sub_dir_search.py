import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        splitext = os.path.splitext(full_filename) 
        ext = splitext[-1]
        if ext == '.sys':
            print(full_filename)

search("c:/")