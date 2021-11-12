
conversions = (3600,60,1)

def sec_to_time(seconds):
    t = [0, 0, 0]
    #how much hours
    t[0] = seconds//conversions[0]
    seconds -= t[0]*conversions[0]
    t[1] = seconds//conversions[1]
    seconds -= t[1]*conversions[1]
    t[2] = seconds
    return t


t = sec_to_time(int(input("Sekunde: ")))
print(t[0], "h, ", t[1],"min, ",t[2],"sec")
