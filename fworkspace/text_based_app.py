import time
from chapters import chapter1

def stat():
    print("\033c", end="")
    print('Your hp is called php. Your own damage is called pdmg.')
    print('php = ' + str(php) + "           "  + 'Enemy hp = ' + str(ehp))
    print('pdmg = ' + str(pdmg) + '          ' + 'Enemy dmg = ' + str(edmg))
def combat():
    global php; global pdmg; global ehp; global edmg
    pturn = True
    while php > 0 and ehp > 0:
        print("\033c", end="")
        stat()
        if pturn:
            print("1 = attack")
            while 1:
                move = input("> ")
                if move == "1":
                    print("\033c", end="")
                    ehp -= pdmg
                    print("Enemy hp decreased by " + str(pdmg))
                    break
                elif move == "2":
                    if php < bhp:
                        print("\033c", end="")
                        print("hp restored")
                        php += pheal
                        break
            pturn = False
        else:
            print("\033c", end="")
            print("Enemy turn")
            time.sleep(1)
            php -= edmg
            pturn = True

bhp = 100
bdmg = 5
bheal = 30

php = bhp
pdmg = bdmg
pheal = bheal

ehp = 100
edmg = 30

r = 0
while 1:
    print("\033c", end="")
    print("Enter 'x' to start")
    print("Enter 'y' to exit")
    i = input("> ")
    if i == "x":
        r = 109
    elif i == "y":
        break
    else:
        print("wrong input")

    if r == 109:
        chapter1.awk()
        print("Wich way do you want to go?")
        print("(stairs/kitchen")
        while 1:
            i = input("> ")

            if i == "kitchen":
                chapter1.ktch()
                print("You you run back and up the stairs or do you freeze?")
                print("(run/freeze)")
                while 1:
                    i = input("> ")
                    if i == "run":
                        r = 2
                        chapter1.run()
                        print("Do you want to run to the stairs or to the bathroom?")
                        while 1:
                            i = input("> ")
                            if i == "stairs":
                                r = 2
                                break
                            elif i == "bathroom":
                                r = 6
                                break
                        break
                    elif i == "freeze":
                        combat()
                        print("Butcher: Youre gonna make a good dinner, hehehe")
                        time.sleep(1)
                        print("The butcher has caught you (ending 1)")
                        r = 0
                        break
            elif i == "stairs":
                r = 2
                break
            else:
                print("Invalid input, remember, no capital letters")
                continue
            break

    if r == 2:
        chapter1.stairs()
        print("Do you wish to enter the bedroom or the children room?")
        print("(children room/bedroom)")
        while 1:
            i = input("> ")
            if i == "children room":
                r = 7
                break
            elif i == "bedroom":
                chapter1.broom()
                while 1:
                    print("(lie down/dont)")
                    i = input("> ")
                    if i == "lie down":
                        chapter1.broom1()
                        r = 10
                        break
                    elif i == "dont":
                        print("guess your going to the childrens room anyways...")
                        input()
                        r = 7
                        break
                    else:
                        print("wrong input idiot")
                        continue
                break
            if r == 7:
                chapter1.chroom()
                print("(play/fight)")
                while 1:
                    chapter1.chroomop()
                    i = input("> ")
                    if i == "play":
                        print("\033c", end="")
                        print("The kid chuckles")
                        print("It seems like he has taken a liking to you!")
                        print("Next thing you see are some boxes in the attic...")
                        r = 9
                        break
                    elif i == "fight":
                        print("You throw back a lego brick")
                        print("The boy seems hurt and lets out a screech")
                        print("Out of no-were, the Butcher appears, looking furious")
                        combat()
                        r = 0
                        print("\033c", end="")
                        print("That's what you get fucker")
                        print("The butcher has caught you (ending 1)")
                        chapter1.death()
                    else:
                        print("make sure there arent any spelling mistakes or capital letters")
                        continue
                    break
                break
    elif r == 6:
        chapter1.bathroom()
        print("(window/door)")
        while 1:
            i = input("> ")
            if i == "window":
                print("You climb down the window and find yourself in the garden")
                r = 11
                input()
                break
            elif i == "door":
                chapter1.door()
                combat()
                print("The butcher has caught you (ending 1)")
                chapter1.death()
                input()
                r = 0
                break
            else:
                print("wrong input")
                continue

    if r == 11:
        chapter1.garden()
        while 1:
            i = input("> ")
            if i == "1":
                chapter1.garden1()
                bdmg = 35
                print("(confront/shed)")
                while 1:
                    i = input("> ")
                    if i == "confront":
                        r = 16
                        break
                    elif i == "shed":
                        r = 18
                        break
                break
            elif i == "2":
                print("Lady: HUh?")
                edmg = 60
                ehp = 50
                combat()
                print("You got cut up by the wind for insulting the lady (Ending 2)")
                r = 0
            
    if r == 16:
        chapter1.confront()
        pdmg = 35
        combat()
        chapter1.confront2()
        while 1:
            i = input("> ")
            if i == "ok":
                print("Sounds good, its not like you have a family waiting for you at home or anything, lets forget about all of that!")
                print("Welcome to the Family (Ending 3)")
                input()
                r = 0
                break
            elif i == "no":
                chapter1.impolite()
                print("Ending 6, cut in half")
                input()
                r = 0
                break
            else:
                print("Invalid")
                continue
    elif r == 18:
        chapter1.shed()
        r = 0

    if r == 10:
        chapter1.basement()
        print("(heater/stairs")
        while 1:
            i = input("> ")
            if i == "heater":
                chapter1.heater()
                print("(y/n)")
                while 1:
                    i = input("> ")
                    if i == "y":
                        chapter1.fire()
                        while 1:
                            i = input("> ")
                            if i == "run":
                                chapter1.run2()
                                chapter1.hell()
                                r = 0
                                break
                            elif i == "freeze":
                                chapter1.impolite2()
                                print("Ending 6, Cut in half")
                                r = 0
                                break
                            else:
                                print("wrong input")
                                continue
                        break
                    elif i == "n":
                        print("guess were going upstairs")
                        r = 12
                break
            elif i == "stairs":
                r = 12
                
    if r == 12:
        print("As your walking up the stairs you see a familiar face...")
        print("ITS THE BUTCHER!")
        input()
        combat()
        chapter1.death()
        r = 0
    elif r == 9:
        chapter1.attic()
        while 1:
            i = input("> ")
            if i == "home":
                chapter1.falsehome()
                r = 0
                break
            elif i == "stairs":
                print("you encounter butcher")
                combat()
                chapter1.death()
                r = 0
                break
    
    print("Game has ended")
    input()