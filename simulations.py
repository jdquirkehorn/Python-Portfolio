#Jay QH
#Simulations
#make simulations in code

#init
import random
finish = 50
tort_pos = 0
hare_pos = 0
hareasleep = False
turtwin = 0
harewin = 0

#main

for i in range(100000):
    while hare_pos < finish and tort_pos < finish:
            tmove = random.randint(1,3)
            sleep = random.randint(1, 10)
            if sleep <= 8:
                hmove = 0
            else:
                hmove = random.randint(1,10)
            hare_pos = hare_pos + hmove
            tort_pos = tort_pos + tmove
            print(f'tortoise {tort_pos} - hare {hare_pos}')
    if tort_pos >= finish:
        print("turtle wins!")
        turtwin = turtwin + 1
        print(turtwin)
        hare_pos = 0
        tort_pos = 0
    elif hare_pos >= finish:
        print("hare wins!")
        harewin = harewin + 1
        print(harewin)
        hare_pos = 0
        tort_pos = 0
