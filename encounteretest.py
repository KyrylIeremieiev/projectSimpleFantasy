import time
action = '1 = fight; 2 = heal;'
def stat1():
    time.sleep(5)
    print("\033c", end="")
    print('Your hp is called php. Your own damage is called pdmg.')
    print('php = ' + str(php) + "           "  + 'Enemy hp = ' + str(m1hp))
    print('pdmg = ' + str(pdmg) + '          ' + 'Enemy dmg = ' + str(m1dmg))
    print(action)
php = 100
pdmg = 50
m1hp = 100
m1dmg = 20
def att1():
    m1hp -= pdmg
    php -= m1dmg
    stat1()
print("\033c", end="")
print("hey you, yes you idiot, wanna fight?")
print("(y/n)")
in1 = input()
#encounter 1 turn 1
while php > 0 or m1hp > 0:
    if in1 == "y":    
        time.sleep(1)
        stat1()
        in2 = input()
        if in2 == "1":
            m1hp -= pdmg
            php -= m1dmg
            stat1()
        elif in2 == "2":
            print("\033c", end="")
            print("No healing equiped")
            print("want to attack instead?")
            print("(y/n)")
            int3 = input()
            if int3 == "y":
                m1hp -= pdmg
                php -= m1dmg
                stat1()
            elif int3 == "n":
                print("ok")
            else:
                print("invalid input")
        else:
            print("invalid input")   
    elif in1 == "n":
        print("ok, fair enough")
    else:
        print("invalid input")
    if m1hp == 0 or m1hp < 0:
        break
#end turn 1
print("\033c", end="")
print('you win')
#test