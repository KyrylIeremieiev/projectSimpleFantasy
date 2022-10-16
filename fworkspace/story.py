# clr scrn = print("\033c", end="")
# waits for input to allow the reader to menually say when hes done reading
import time
def story1():
    global name
    print("\033c", end="")
    print("$%^&: A human will often make irrational dicisions, even in doubt they will continue")
    input()
    print("$%^&: When a person doesnt know what to do, they choose to stop thinking, set their mind on a specific goal and dont sway from it")
    input()
    print("$%^&: In the end humans have a fragile mind")
    input()
    print("\033c", end="")
    print("A grass hill. That is what you see as you wake up from a mid-day nap")
    input()
    print("You still feel a little sleepy as the wind blows")
    input()
    print("?: Oh, you final woke up...")
    input()
    print("You look over to see a man fully clad in armour sitting next to you")
    input()
    print("?: Oh sorry, I should introduce myself. My name is Adel. Dont mind me, I just like this spot as well")
    input()
    print("Adel: How may I call you?")
    input()
    print("You dont remember how you much about how you got here or why youre here, you dont have any memories about your life before you came to this place, but you do remember your name")
    input()
    name = input("My name is: ")
    input()
    print("\033c", end="")
    print("Adel: Hmm, ok then " + str(name) + "how about you tell me more ab...")
    input()
    print("As the two of you are talking you hear something walking through the grass...")
    input()
    print("\033c", end="")
    print("A golbin appears")
    input()
    print("however Adel doesnt seem fazed")
    input()
    print("Adel: Here catch")
    input()
    print("\033c", end="")
    print("Sword has been added to Inventory")
    input()
    print("\033c", end="")
    print("The goblin has come too close to run away")
    print("\033c", end="")

def story2():
    print("\033c", end="")
    print("Adel: well that was something...")
    input()
    print("random soldier: Captain, we need to keep going!")
    input()
    print("Adel: Aw shit, have to get going...")
    input()
    print("Adel: Have a nice day!")
    input()
    print("Adel: And btw, you can keep the sword.")
    input()
    print("Adel: The most nearby city is to the south")
    input()
    print("\033c", end="")
    print("Adel walks away and you decide to follow his advice and go to south")
    input()
    print("As youre walking you see a vilage, with a crippled man sitting just outside")
    input()
    print("\033c", end="")
    print("Villager: I wouldnt go in there if I were you.")
    input()
    print("Villager: The village is done for")
    input()
    print("Villager: the plague has already consumed this place")

def plg1():
    print("\033c", end="")
    print("Villager: What a naive person")
    input()
    print("\033c", end="")
    print("As you walk you can see dead bodies on the streets")
    input()
    print("Anyone that is alive is more akin to a skin and bones, somehow still moving")
    input()
    print("As you walk you see a big pile of bodies and feel a tap on your shoulder ...")
    input()
    print("You see a squad of men in plague doctor masks, some of them holding staffs")
    input()
    print("\033c", end="")
    print("Doctor: You dont seem to be from around here... Step back or even better get out of here while youre not suffering on the ground")
    input()
    print("Doctor: And oh yea, before you catch the decease")
    input()
    print("\033c", end="")
    print("The Doctor holds his hand in front of you")
    input()
    print("His hand starts to glow faintly")
    input()
    print("\033c", end="")
    print("Doctor: that should do")
    input()
    print("Doctor: Now scram")
    input()
    print("\033c", end="")
    print("??: Hey, you...")
    input()
    print("??: Mind helping me lad?")
    input()
    print("\033c", end="")
    print("you look the way where the sound came from and you see a man, barely breathing")
    input()
    print("Man: It looks like the end of the road for me, could you help me get to my mother")
    input()

def plg2():
    print("Man: Thank you")
    input()
    print("\033c", end="")
    print("you help him walk to an isolated house, as you enter you hear a faint voice")
    input()
    print("\033c", end="")
    print("Victor?")
    input()
    print("Man: Yes mother, its me, im home")
    input()
    print("Victor: Thank you, I will be fine now.")
    input()
    print("As for your reward, look in that locker")
    input()
    print("\033c", end="")
    print("Victor walks over to the bed on which his mother lies")
    input()
    print("As he sits down with a groun he says")
    input()
    print("Victor: you may take whatever you like, I wont be sticking around anyway")
    input()
    print("\033c", end="")
    print("A second later neither the man nor the mother were breathing")

def ghoul1():
    print("\033c", end="")
    print("You decide to not enter the village and go around it")
    input()
    print("As you walk you see a burning cariage")
    input()
    print("And a weird creature, its skin is gray and its hands are practically claws")
    input()
    print("You may have wanted to run away but the creature saw you!")
    print("\033c", end="")

def splprof1():
    print("In the locker you find 2 books")
    input()
    print("\033c", end="")
    print("you find a spell called 'Phoenix Nest'")
    print("Phoenix Nest allowes you to passively heal hp every turn with the formula 0.7 * spell proficiency")
    print("You may only have 1 spell at a time")
    print("You find a chanting book")
    print("Chanting books increase spell proficiency by 20")

def level1():
    print("\033c", end="")
    print("you leveled up!")
    print("you can increase your stats now.")
    print("enter 1 to increase you hp by 50, 2 to increase your dmg by 50")

print("\033c", end="")
story1()
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
level1()
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

story2()

# fist choice

print("Do you still want to enter?")
print("Options: 'enter' and 'leave'")

ghoulhp = 120
ghouldmg = 50
truedmg = False

while 1:
    choice1 = input("> ")
    if choice1 == "enter":
        plg1()
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
        ghoul1()
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
                    stat1
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
                    time.sleep(1)
                    break
    else:
        continue
    break
    


if choice2 == True:
    splprof1()
    splprof += 20
    phnxnest = True
