import time
php = 100
pdmg = 50
m1hp = 100
m1dmg = 20
action = '1 = fight; 2 = heal;'
def stat1():
    time.sleep(5)
    print("\033c", end="")
    print('Your hp is called php. Your own damage is called pdmg.')
    print('php = ' + str(php) + "           "  + 'Enemy hp = ' + str(m1hp))
    print('pdmg = ' + str(pdmg) + '          ' + 'Enemy dmg = ' + str(m1dmg))
    print(action)

def att1():
    m1hp -= pdmg
    stat1()

pturn = True
while php >= 0 and m1hp >= 0:
    if pturn:
        stat1()
        while 1:
            move = input('> ')
            if move == '1':
                # att1() for some reason does not work
                m1hp -= pdmg
                stat1()
                break
            else:
                print("invalid input")
                continue
        pturn = False        
    else:
        print("\033c", end="")
        print("Enemy Turn")
        time.sleep(1)
        php -= m1dmg
        stat1()
        pturn = True
    if m1hp <= 0:
        break
print("hope it worked")