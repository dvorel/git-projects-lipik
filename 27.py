import os
import codecs

data_location = "git_test/data/"
out_dir = "out/"
file_names = ("email", "nums", "names", "rest")

mails = []
numbers = []
names = []
not_important = []

def find_mail(data):
    for i in data:
        if "@" in i and "." in i:
            return i
    return "NoEmail"

def find_num(data):
    for i in data:
        if sum(c.isdigit() for c in i) >= 6:    #broj mobitela/telefona mora imati bar 6 brojeva
            return i
    return "NoNumber"

def find_name(data):
    #ime je na indexu 0
    ime = ""
    for i in range(len(data[0])):
        if data[0][i].isalpha() or data[0][i].isspace():
            ime += data[0][i]
    return ime.strip()

def find_junk(data):
    ret = []
    for i in range(len(data)):
        if data[i] not in mails and data[i] not in numbers:
            if i == 0:
                ret.append(data[i].replace(names[-1], ""))      #remove name from string
            else:
                ret.append(data[i])
    return ret

def proc(str):
    spl = str.split("\n")
    mails.append(find_mail(spl))
    numbers.append(find_num(spl))
    names.append(find_name(spl))
    not_important.append(find_junk(spl))

def write_files():
    out_location = data_location + out_dir
    os.mkdir(out_location)    
    #upisi emailove u file
    f = codecs.open(out_location+ file_names[0], "w", "utf-8")
    f.write(str(mails))
    f.close()
    #upisi brojeve
    f = codecs.open(out_location+ file_names[1], "w", "utf-8")
    f.write(str(numbers))
    f.close()
    #upisi imena
    f = codecs.open(out_location+ file_names[2], "w", "utf-8")
    f.write(str(names))
    f.close()
    #upisi ostalo
    f = codecs.open(out_location+ file_names[3], "w", "utf-8")
    f.write(str(not_important))
    f.close()



for i in os.listdir(data_location):
    data = open(data_location + i, 'r', encoding= "utf8").read()
    proc(data)
    print(data)
try:
    write_files()
except:
    print("Write failed!\nCheck if files already exsists")