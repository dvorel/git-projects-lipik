var = input(": ")
spl = var.rsplit(" ")

if spl[0] == "on":
    if (spl[1])[-1] != "i":
        s = "on je " + (spl[1])[0:-1] + "ao"
    else:
        s = "on je " + (spl[1])[0:] + "o"
    print(s)
else:
    s = spl[0] + " je "
    if (spl[1])[-1] == "a":
       s+= spl[1] + "la"
    elif (spl[1])[-3] == "a":
        s+= (spl[1])[0:-3] + "la"
    else:
        s+= (spl[1])[0:-3] + "kala"
    print(s)
