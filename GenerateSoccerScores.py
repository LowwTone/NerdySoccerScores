import random

uitsl_tabel = [[13, "1-1"], [25, "1-0"], [35, "2-1"], \
               [44, "0-0"], [53, "0-1"], [61, "2-0"], \
               [68, "1-2"], [74, "2-2"], [79, "0-2"], \
               [84, "3-0"], [89, "3-1"], [92, "1-3"], \
               [95, "3-2"], [98, "0-3"], [100, "1-1"]]

print("This script generates soccerscores based on random picks from the 15 most common soccer scores (weighted for their frequency)")
print("Hacked together in 5 minutes to join a betting competition at work prediciting European championship scores")
print("Trying to prove statistics trump percieved game knowledge")
print()

while True: 
    r = random.randint(0,99)
    
    for uitsl in uitsl_tabel:
        if uitsl[0] > r:
            print()
            print(uitsl[1])
            print()
            break
    input("Enter for next score")
        