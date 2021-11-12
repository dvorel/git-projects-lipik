#tuple dostupnih kovanica/novcanica (redom min->max)
coins = (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5)
coin_names = ("1lp", "2lp", "5lp", "10lp", "20lp", "50lp", "1kn", "2kn", "5kn")

def get_change(mon, pri):
    #prilagodba (*100) da nema decimalnog dijeljenja
    ch = int((mon-pri)*100)
    c_coins = [int(i*100) for i in coins]
    ret = []
    for i in range(len(c_coins)):
        num = ch//c_coins[(-1-i)]
        ret.insert(0, num)
        ch -= ret[0]*c_coins[(-1-i)]

    return ret

def printC(list):
    print("\nAutomat vraca:", end=" ")
    for i in range(len(list)):
        if list[i]>0:
            print(coin_names[i], ":", list[i], end=" | ")

printC(get_change(3.14, 1.99))
printC(get_change(0.61, 0.30))