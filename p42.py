# coding:utf-8

from sys import exit
from random import randint



class Game(object):
    def __init__(self,start):
        self.death_gift = ["Heroes, please come back again!",
                           "You win some,you lose some.",
                           "You are dead!",
                           "Zombies eat your brain.",
                           ]
        self.start = start



    def play(self):
        next = self.start



        while True:
            print("\n*******************************************")
            room = getattr(self, next)
            next = room()



    def death(self):
        print(self.death_gift[randint(0, len(self.death_gift) - 1)])
        exit(1)



    def novice_village(self):
        print("""There are many NPC, a garandfather in the old village.
Find him, he will give you the task of the notice Village.
Be careful! Find the blacksmith to buy the weapon first.
Otherwise, your first failure apeared.""")
        print("Now,waht do you choose?Equipment?Or out the village?")



        action = input(">>>")




        if action == "Equipment":
            print("UNcle blacksmith is good, give you free equipment to defend yourself!")
            print("Go on, boy!")
            print("Wait! The village chief has something to do with you.")
            return "task"
        else:
            print("What did you forget to do?")
            return "novice_village"



    def task(self):
        print("Haha, man, I'm surpised to see you bones,I ask if you are willing to help the village of pesticides.")
        


        action = input(">>>")



        if action == "Yes!":
            print("Go, warrior,Iam not wrong!")
            return "misty_forest"
        elif action == "Stupid old man...":
            print("Suddenly the rolling thunder.")
            print("You dead!")
            return "death"
        else:
            print("You can think it over.")
            return "task"



    def misty_forest(self):
        print("The smoke fills the air.")
        print("Skeletons everywhere should be adventurers")
        print("No, you met goblin!")
        print("The battle degins!")
        monster = "gobin"
        killing = input("[WuWa]> ")
        frequency = 0
        

        
        while killing == monster and frequency < 10:
            print("Upgrade!")
            frequency += 1
            killing = input("[WuWa]> ")



        if killing != monster:
            print("Oh,no.The other mobs are too high,")
            print("You dead!")
            return "death"


        else:
            print("Your rank is high enough.")
            print("Go ahead, boy, beat the goblin King")
            return "gobin_palace"




    def gobin_palace(self):
        print("There's nothing here.")
        print("You've been cheated")
        print("\n(●—●)")
        exit(0)


a_game = Game("novice_village")

a_game.play()



































        
