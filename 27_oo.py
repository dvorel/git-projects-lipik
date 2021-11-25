import os
import codecs

class Person:
    def __init__(self) -> None:
        self.email = ""
        self.number = ""
        self.name = ""
        self.info = ""

    def print_person(self):
        print("Name: ", self.name)
        print("Number: ", self.number)
        print("Email: ", self.email)
        print("Info: ", self.info)

    #setters
    def set_name(self, name):
        self.name = name
    
    def set_email(self, email):
        self.email = email
    
    def set_number(self, num):
        self.number = num

    def set_info(self, info):
        self.info = info

    #getters
    def get_name(self):
        return(self.name)
    
    def get_email(self):
        return(self.email)
    
    def get_number(self):
        return(self.number)

    def get_info(self):
        return(self.info)

out_dir = "out"
file_names = ("email", "nums", "names", "rest")

#get mail from data
def find_mail(data):
    for i in data:
        if "@" in i and "." in i:
            return i
    return "NoEmail"

def find_num(data):
    for i in data:
        if sum(c.isdigit() for c in i) >= 6:
            return i
    return "NoNumber"

def find_name(data):
    #ime je na indexu 0
    ime = ""
    for i in range(len(data[0])):
        if data[0][i].isalpha() or data[0][i].isspace():
            ime += data[0][i]
    return ime.strip()

def find_info(data, person):
    ret = []
    email = person.get_email()
    number = person.get_number()
    name = person.get_name()
    for i in range(len(data)):
        if data[i] not in email and data[i] not in number:
            if i == 0:
                ret.append(data[i].replace(name, ""))      #remove name from string
            else:
                ret.append(data[i])
    return ret

def proc(str, person):
    spl = str.split("\n")
    person.set_email(find_mail(spl))
    person.set_number(find_num(spl))
    person.set_name(find_name(spl))
    person.set_info(find_info(spl, person))



def write_files(data_location, person):
    out_location = os.path.normcase(os.path.join(data_location, out_dir))
    #create output dir
    if not os.path.isdir(out_location):
        try:
            os.mkdir(out_location)
        except:
            print("\nFailed to create dir!")

    #write emails to file
    f = codecs.open(os.path.join(out_location, file_names[0]), "a", "utf-8")
    f.write(str(person.get_email()))
    f.write("\n")
    f.close()
    #write numbers
    f = codecs.open(os.path.join(out_location, file_names[1]), "a", "utf-8")
    f.write(str(person.get_number()))
    f.write("\n")
    f.close()
    #write names
    f = codecs.open(os.path.join(out_location, file_names[2]), "a", "utf-8")
    f.write(str(person.get_name()))
    f.write("\n")
    f.close()
    #write other info
    f = codecs.open(os.path.join(out_location, file_names[3]), "a", "utf-8")
    f.write(str(person.get_info()))
    f.write("\n")
    f.close()

def open_files(data_location):
    ret = []
    for i in os.listdir(data_location):
        path = os.path.normcase(os.path.join(data_location, i))
        if os.path.isfile(path):
            ret.append(Person())
            data = open(path, 'r', encoding= "utf8").read()
            print(data)
            proc(data, ret[-1])
            ret[-1].print_person()

    return ret


#call funcs
people = open_files("david/datoteke/data")

for i in people:
    write_files("david/datoteke/data", i)
