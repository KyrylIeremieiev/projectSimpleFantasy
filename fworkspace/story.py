# clr scrn = print("\033c", end="")
# waits for input to allow the reader to menually say when hes done reading
import time
from chapters import chapter1

print("\033c", end="")
chapter1.story1()
input()

cls = print("\033c", end="")
bhp = 100
bdmg = 30
splprof = 10
phnx = 0.7 * splprof
php = bhp
pdmg = bdmg
m1hp = 100
m1dmg = 20
action = '1 = fight'
invalid = "invalid input"

inv = {
    "weapon": "sword"
}

def stat1():
    time.sleep(5)
    print("\033c", end="")
    print('Your hp is called php. Your own damage is called pdmg.')
    print('php = ' + str(php) + "           "  + 'Enemy hp = ' + str(m1hp))
    print('pdmg = ' + str(pdmg) + '          ' + 'Enemy dmg = ' + str(m1dmg))
    print(action)

def stat2():
    time.sleep(5)
    print("\033c", end="")
    print('Your hp is called php. Your own damage is called pdmg.')
    print('php = ' + str(php) + "           "  + 'Enemy hp = ' + str(ghoulhp))
    print('pdmg = ' + str(pdmg) + '          ' + 'Enemy dmg = ' + str(ghouldmg))
    print(action)

truedmg = False
pturn = True

#first fight

while php > 0 and m1hp > 0:

    if truedmg == False and inv["weapon"] == "sword":
        pdmg += 30
        print("sword equiped, damage increased")
        time.sleep(1)
        cls
        truedmg = True
    else:
        truedmg = True

    if truedmg == True:
        stat1()
        if pturn:
            stat1
            while 1:
                i1 = input("> ")
                if i1 == "1":
                    print("\033c", end="")
                    m1hp -= pdmg
                    print("Enemy hp is decreased by " + str(pdmg))
                    time.sleep(1)
                    print("\033c", end="")
                    break
                else:
                    print(invalid)
                    continue
        else:
            print("\033c", end="")
            print("Enemy Turn")
            time.sleep(1)
            print(str(m1dmg) + " damage taken")
            time.sleep(1)
            php -= m1dmg
            stat1()
            pturn = True
        if m1hp <= 0:
            print("\033c", end="")
            print("the creature died")
            time.sleep(1)
            break

print("\033c", end="")
print("you leveled up!")
print("you can increase your stats now.")
print("enter 1 to increase you hp by 50, 2 to increase your dmg by 50")

#level up 1
chapter1.level1()
while 1:
    i2 = input("> ")
    if i2 == "1":
        bhp += 50
        print("\033c", end="")
        print("base hp increased!")
        time.sleep(1)
        break
    elif i2 == "2":
        bdmg += 50
        print("\033c", end="")
        print("base damage increased")
        time.sleep(1)
        break
    else:
        print(invalid)

php = bhp
pdmg = bdmg

print("your base hp is now " + str(bhp))
print("your base dmg is now " + str(bdmg))

chapter1.story2()

# fist choice

print("Do you still want to enter?")
print("Options: 'enter' and 'leave'")

ghoulhp = 120
ghouldmg = 50
truedmg = False

while 1:
    choice1 = input("> ")
    if choice1 == "enter":
        chapter1.plg1()
        print("Do you want to help the man?")
        print("(y/n)")
        while 1:
            choice2 = input("> ")
            if choice2 == "y":
                choice2 = True
                break
            elif choice2 == "n":
                choice2 = False
                break
            else:
                print(invalid)
                continue
    elif choice1 == "leave":
        pturn = True
        chapter1.ghoul1() # Ghoul Encounter
        while php > 0 and ghoulhp > 0:
            if truedmg == False and inv["weapon"] == "sword":
                pdmg += 30
                print("sword equiped, damage increased")
                time.sleep(1)
                truedmg = True
            else:
                truedmg = True

            if truedmg == True:
                stat2()
                if pturn:
                    stat2()
                    while 1:
                        i1 = input("> ")
                        if i1 == "1":
                            print("\033c", end="")
                            ghoulhp -= pdmg
                            print("Enemy hp is decreased by " + str(pdmg))
                            time.sleep(1)
                            print("\033c", end="")
                            break
                        else:
                            print(invalid)
                            continue
                    pturn = False
                else:
                    print("\033c", end="")
                    print("Enemy Turn")
                    time.sleep(1)
                    print(str(ghouldmg) + " damage taken")
                    time.sleep(1)
                    php -= ghouldmg
                    stat2()
                    pturn = True
                if ghouldmg <= 0:
                    print("\033c", end="")
                    print("the creature died")
                    gspell = True
                    time.sleep(1)
                    break
    else:
        continue
    break
    


if choice2 == True:
    chapter1.plg2()
    holystatue = True
    chapter1.splprof1()
    splprof += 20
    phnxnest = True
    def phoenix():
        if rcount <=5:
            php += phnx
            rcount += 1
        if rcount == 5:
            rcount = 0

elif gspell == True:
    chapter1.ghoul2()
    while 1:
        choice = input("> ")
        if choice == "y":
            chapter1.splprof2()
            splprof += 20
            dmnzation = True
                
gstatus = "/"
pstatus = "/"
rcount = 0
while php > 0 and ghoulhp > 0:
            if truedmg == False and inv["weapon"] == "sword":
                pdmg += 30
                print("sword equiped, damage increased")
                time.sleep(1)
                truedmg = True
            else:
                truedmg = True

            if truedmg == True:
                stat2()
                if pturn:
                    if rcount >= 5:
                        gstatus = "/"
                        pstatus = "/"
                    elif gstatus == "active":
                        if pdmg == bdmg:
                            pdmg *= 2
                            rcount += 1
                        else:
                            rcount += 1
                    elif pstatus == "active":
                        if php < bhp:
                            php += phnx
                            rcount += 1
                    stat2()
                    while 1:
                        i1 = input("> ")
                        if i1 == "1":
                            print("\033c", end="")
                            ghoulhp -= pdmg
                            print("Enemy hp is decreased by " + str(pdmg))
                            time.sleep(1)
                            print("\033c", end="")
                            break
                        elif i1 == "2":
                            if dmnzation == True:
                                gstatus = "active"
                                rcount = 0
                            elif phnxnest == True:
                                pstatus = "active"
                                rcount = 0
                            break
                        else:
                            print(invalid)
                            continue
                    pturn = False
                else:
                    print("\033c", end="")
                    print("Enemy Turn")
                    time.sleep(1)
                    print(str(ghouldmg) + " damage taken")
                    time.sleep(1)
                    php -= ghouldmg
                    stat2()
                    pturn = True
                if ghoulhp <= 0:
                    print("\033c", end="")
                    print("the creature died")
                    gspell = True
                    time.sleep(1)
                    break