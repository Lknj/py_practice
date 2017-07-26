# coding:utf-8
# 调用sys模块的exit函数
from sys import exit
# 同上
from random import randint

# randint()随机生成一个int整数，在指定范围内，有上限和下限


# 这是一个文字游戏




#定义函数 死
def death():
    quips = ["You died. You kinda suck at this.",
             "Nice job, you died ...jackass.",
             "Such a luser.",
             "I have a small puppy that's better at this."]
    print(quips[randint(0, len(quips) - 1)])
    exit(1)

#定义函数  中央走廊 地点
def central_corridor():
    print("The Gothons of planet #25 have invaded your ship and destroyed")
    print("your entire crew. You are the last surviving member and your last")
    print("mission is to get the neutron destruct bomb from the Weapons Armory,")
    print("put it in the bridge, and blow the ship up after getting into an ")
    print("escape pod.")
    print("\n")
    print("You're running down the central corridor to the Weapons Arromory when")
    print("a Gothon jumps out, red scaly skin,dark grimy teeth, and evil clown costum")
    print("flowing around his hate filled body. He's blocking the door to the")
    print("Armory and about to pull a weapon to blast you.")

# 玩家输入

    action = input(">")
    if action == "shoot!":
        print("Quick on the draw you yank out your blaster and fire it the Gothon.")
        print("His clown costume is flowing and moving around his body, whice throws")
        print("off your aim. youe laser hits his costume but misses him entirely. This")
        print("completely ruins his brand new costume his mother bought, him, which")
        print("makes him fly into an insane rage and blast you repeatedly in the face until")
        print("you are dead. Then he eats you.")
        return 'death'



    elif action == "dodge!":
        print("Like woeld class boxer you dodge,weave,slip and slipe right")
        print("as the Gothon's blaster cranks a laser past your head.")
        print("In the middle of your artful dodge your foot slips and your")
        print("bang your head on shortly after on;y to die as the Gothon stomps on")
        print("your head and eats you.")
        return('death')



    elif action == "tell a joke":
        print("Lucky for you they made you learn Gothon insults in the academy.")
        print("You tell the one Gothon joke you know:")
        print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gurunbhfr, fur fvgf hdg dsghh  gjdsh.")
        print("The Gothon stops, tries not to laugh, then busts out laughing and can't move.")
        print("WHile he's laughing you run up and shoot him square in the head")
        print("putting him down, then jump through the Weapon Armory door.")
        return 'laser_weapon_armory'



    else:
        print("DOES NOT COMPUTE!")
        return 'central_corridor'

# 定义函数  激光武器的军械库 地点
def laser_weapon_armory():
    print("You do a dive roll into the Weapon Armory, crouch and scan the room")
    print("for more Gothous that might be hiding. It's dead quiet, too quiet.")
    print("You stand up and run to the far side of the roomand find the")
    print("neutron bomb in its container. There's a keypad lock on the box")
    print("and you need the code to get the omb out. If you get the code")
    print("wrong 10 times then the lock closes forever and you can't")
    print("get the bomb. The code is 3 digits.")
    code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
    guess = input("[keypad]> ")
    guesses = 0

# 循环 猜测
    while guess != code and guesses < 10:
        print("BZZZZEDDD!")
        guesses += 1
        guess = input("[keypad]> ")


# if语句
    if guesses == code:
        print("The container clicks open and the seal breaks, letting gas out.")
        print("You grab the neutron bomb and run as fast as you can to the")
        print("bridge where you must place it in the right spot.")
        return 'the_bridge'

    else:
        print("The lock buzzes one last time and then you hear a sickening")
        print("melting sound as the mechanism is fused together.")
        print("You decide to sit there, and finally the Gothons blow up the")
        print("ship from their ship and you die.")
        return 'death'



#定义函数 地点 桥
def the_bridge():
    print("you burst onto the Bright with the neutron destruct bomb")
    print("under your arm and surprise 5 Gothons who trying to")
    print("take control of the ship. Each of them has an even uglier")
    print("clown costume than last. Thay haven't pulled their")
    print("weapons out yet, as they see the active bomb under your")
    print("arm and don't want to see it off.")



# 玩家输入
    action = input(">")


# if 语句
    if action == "throw the bomb":
        print("In a panic you throw the bomb at teh group of Gothons")
        print("and make a leap for the door. Right as you drop it a")
        print("Gothon shoots you right in the back killing you.")
        print("As you die you see abother Gothon frantically try to disarm")
        print("the bomb. You die knowing they will probably blow up when")
        print("it goes off.")
        return 'death'



    elif action == 'slowly place the bomb':
        print("You point your blaster at the bomb under your arm")
        print("and the Gothons put their hands up and start to sweat.")
        print("You inch backward to the door, open it, and then carefully")
        print("place the bomb on the floor, pointing your blaster at it.")
        print("You then jump back throught the door, punch the close button")
        print("and blast the lock so the Gothons can't get out.")
        print("Now that the bomb is placed you run to the escape pod to")
        print("get off this tin can.")
        return 'escape_pod'
    else:
        print("DOES NOT COMPUTE!")
        return("the_bridge")



# 定义函数 逃生舱
def escape_pod():
    print("Yo rush through the ship desperately trying to make it to")
    print("the escape pod befor the whole ship exxplodes. It seems like")
    print("hardly any Gothons are on the ship,so your run is clear of")
    print("interference. You get to the chamber with the eacape pods, and")
    print("now need to pick one to take. Some of them could be damaged")
    print("but you don't have time to look. There's 5 pods, which one")
    print("do you take?")


    good_pod = randint(1,5)
    guess = input("[pod #]> ")



# if语句
    if int(guess) != goog_pod:
        print("You jump into pod %s and hit the eject button." % guess)
        print("The pod escapes out into the void of space, then")
        print("implodes as the hull ruptures, crushing your body")
        print("into jam jelly.")
        return 'death'
    else:
        print("You jump into pod %s and hit the eject button." % guess)
        print("The pod easily slides out into space heading to")
        print("the lpant below. As it flies to the planet, you look")
        print("back and see your ship implode then explode like a")
        print("bright star, taking out the Gothon ship at the same")
        print("time. you won!")
        exit(0)



# 字典
ROOMS = {
    'death': death,
    'central_corridor': central_corridor,
    'laser_weapon_armory': laser_weapon_armory,
    'the_beidge': the_bridge,
    'escape_pod': escape_pod
    }


# 定义函数 
def runner(map,start):
    next = start


    while True:
        room = map[next]
        print("\n--------")
        next = room()


# 开始
runner(ROOMS, 'central_corridor')



































    
          
