import time
php = 100
pdmg = 30
pheal = 10
m1hp = 100
m1dmg = 20
action = '1 = fight; 2 = heal;'
inv = {
    "weapon": "knife",
    "armour": "leather",
    "staff": "staff of healing"
}
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
    dn = False
    tdmg = False
    th = False

    #to prevent dmg increasing every turn
    if pheal == 10:
        if inv["staff"] == "staff of healing":
            pheal += 20
            print("\033c", end="")
            print("Staff of healing is equiped, healing increased by 20")
            th = True
            time.sleep(1)
        else:
            th = True
    elif pdmg == 30:
        if inv["weapon"] == "knife":
            pdmg += 20
            print("\033c", end="")
            print("Knife equiped, damage increased by 20")
            tdmg = True
            time.sleep(1)
        else:
            tdmg = True
    elif m1dmg == 20:
        if inv["armour"] == "leather":
            m1dmg *= 0.8
            print("\033c", end="")
            print("Leather armour equiped, enemy dmg decreased by 20%")
            dn = True
            time.sleep(1)
        else:
            dn = True
    else:
        dn = True
        tdmg = True
        th = True
    
    if dn == True and tdmg == True and th == True:
        if pturn:
            stat1()
            while 1:
                move = input('> ')
                if move == '1':
                    m1hp -= pdmg
                    stat1()
                    time.sleep(1)
                elif move == '2':
                    if php < 100:
                        php += pheal
                        print("\033c", end="")
                        print("HP Restored")
                        stat1()
                        time.sleep(1)
                    else:
                        print("HP is already full")
                        continue
                else:
                    print("invalid input")
                    continue
                break   
            pturn = False        
        else:
            print("\033c", end="")
            print("Enemy Turn")
            time.sleep(1)
            print("you have leather armour, the enemy damage is lowered by 20%")
            time.sleep(1)
            php -= m1dmg
            stat1()
            pturn = True
        if m1hp <= 0:
            break
print("\033c", end="")
print("you win")