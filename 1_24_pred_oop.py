import random

#zadatci pred oop
#1.
def rem_duplicate(data):
    l = list()
    for i in data:
        if i not in l:
            l.append(i)
    return l

#2.
def reverse_str(t):
    n_str = ""
    for i in range(len(t)):
        n_str += t[(-1-i)]
        if i%2==0:
            n_str+=str(random.randrange(0, 10))
    return n_str

#3.
def sum_comps():
    score_list = list()
    score = 0
    while True:
        score = input("Input score or -1 for exit")
        if score == "-1":
            break
        score_list.append(int(score))
    score_list.remove(max(score_list))
    score_list.remove(min(score_list))
    return score_list

#4.
def list_pow(l):
    l_pow = {i: i**2 for i in l}
    return l_pow

#5.
def spl_str(s):
    nums = list()
    chars = list()
    for i in range(len(s)):
        if s[i].isdigit:
            nums.append(int(s[i]))
        else:
            chars.append(s[i])
    return nums, chars

#6.
def sum_int():
    last = int(input("NUM: "))
    sum = 0
    i = 0
    while True:
        i = int(input("NUM: "))
        if i<last:
            break
        sum +=i
    return sum

#7.
def find_ind(l1, l2):
    indexes = list()
    l1.tolower()
    l2.tolower()
    index = 0
    for i in l1:
        index = l2.index(i)
        if index!=None:
            indexes.append(index)
    return indexes

#8.
def next_p():
    inp = int(input("Input int: "))
    if len(inp)==3:
        return inp+1
    return "Error"

#9.
def min_sum():
    num = list()
    sum_num = list()

    while True:
        i = input("Num: ")
        if int(i) <= 0:
            break
        num.append(i)
        sum = 0
        for d in range(len(i)):
            sum += int(i[d])
        sum_num.append(sum)

    ind = sum_num.index(min(sum_num))
    return sum_num[ind], num[ind]

#10. ne znam zasto ne radi
def str_maxmin(s):
    new_s = ""
    is_max = False
    for i in s:
        print(i)
        if is_max:
            if i.isupper():
                new_s += i
        else:
            if i.islower():
                new_s += i
        print(new_s)

        if is_max:
            is_max = False
        else:
            is_max = True 

    return new_s

#11.
def num_pairs():
    n = int(input("N:"))
    nums = {}
    max_sum = 0
    max_ind = 0
    while n<3 and n>20:
        n = int(input("N:"))
    
    for i in range(n):
        nums[i].append(int(input("1. ")))
        nums[i].append(int(input("2. ")))
    print(nums)
    
    for i in range(len(nums)):
        sum = nums[i][0] + nums[i][1]
        if sum >max_sum:
            max_sum = sum
            max_ind = i
    return max_sum, nums[max_ind]

#12.
def find_pal(s):
    s.lower()
    if s == s[::-1]:
        return True
    return False

#13.
def matrix():
    n = int(input("N: "))
    mat = []
    for i in range(n):
        mat.append(list())
        for j in range(n):
            if i==j:
                mat[i].append(1)
            else:
                mat[i].append(0)
    return mat

#14.
def coord(x, y):
    l = list()
    for i in range(10):
        l.append(list())
        for j in range(10):
            if i==y and j==x:
                l[i].append("X")
            else:
                l[i].append("-")
    return l

def coord_print(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j], end="")
        print("\n")

#15.
def prosti(low, upp):
    n = 0
    for i in range(low, upp, 1):
        for j in range(2, i, 1):
            if i%j==0:
                break
            if j==(i-1):
                print(i)
                n+=1
    return n

#16.
def print_n(s, n):
    if n>len(s):
        print("N>S")
        return None
    s_new = ""
    for i in range(0, len(s), n):
        s_new += s[i]
    return s_new

#17.
def upper_count(s):
    num = 0
    for i in range(len(s)):
        if s[i] == "A":
            print("A found")
            break
        if s[i].isupper():
            num+=1
    return num

#18.
def print_18():
    for i in range(1, 1000, 1):
        if i%5==0 and i%13==0:
            print(i)

#19. i 20.
def new_num():
    new_nums = []
    while True:
        n = input("N: ")
        new_nums.append(list())
        max = 0
        for i in n:
            if int(i)>max:
                max=int(i)
        new_nums[-1].append(max)
        n//=10
        new_nums[-1].append(n%10)

#21.
def stars(n):
    j = 0
    if n%2!=0:
        n+=1
    i=0
    while True:
        if i<=n/2:
            j+=1
        else:
            j-=1
        if j==-1:
            break

        for k in range(j):
            print("*", end="")
        print("")
        
        i+=1

def stars2(n):
    j = 1
    add = True

    while True:
        for k in range((n//2)-(j//2)):
            print(" ", end="")
        for k in range(j):

            print("*", end="")
        print("")

        if j<n and add:
            j+=2
        else:
            j-=2
            add = False
        if j<0:
            break

def stars3(n):
    j = 0
    n+=3
    s = ""

    while True:
        s = "1"
        for i in range(1, n, 1):
            if s[i-1] == "1":
                s+="0"
            else:
                s+="1"
        for i in range(j):
            print(" ", end="")
        print(s)
        
        j+=1
        n-=2
        if n<1:
            break
        
def stars4(n):
    j = n//2 + 1
    add = False

    while True:
        for k in range(j):
            print("x", end="")
        print("")

        if j>1 and not add:
            j-=1
        else:
            j+=1
            add = True
        if j>n//2+1:
            break

#22.
def max_div(a, b):
    div = 0
    for i in range(min(a, b)):
        if a%i==0 and b%0==0:
            div = i
    return div

#23.
def transactions():
    account = {"D" : list() ,"W" : list(), "T" : None}
    while True:
        i = input(": ")
        if i == "quit":
            break
        s = i.split("=")
        
        if s[0] == "T":
            account["T"] = int(s[1])
        elif s[0] == "W":
            if int(s[1]) < account["T"]:
                account["T"] -=int(s[1])
                account["W"].append(int(s[1]))
        elif s[0] == "D":
            val = account["T"]
            val +=int(s[1])
            account["T"] = val
            account["D"].append(int(s[1]))
        print(account)
