from os import listdirt
from os.path import isfile, join

def find(path, filename):
    for f in listdirt(path):
        if isfile(join(path,f)):
            if filename in f:
                print(f)

        else:
            find(join(path,f), filename)

find(r"D:\2nd year, second sem\Software Design", "Laboratory-Activity-No.4.docx")