#THE CORE
from enemy import Enemy
from player import Player
import random
import time

human = Player("Aku", 40)
orc = Enemy("Blork", 40)


while True:
    question = input("Are u ready for dungeon(Y or N): ").lower()
    if question == "n":
        print("...")
        continue
    
    else:
        print("Lets begin!!")
        print()
        break

print("║║║║║║║║║║║║║║║║║║║║")
print(human.info())
print(orc.info())
print("║║║║║║║║║║║║║║║║║║║║")
print()

while True:
    print("---HUMAN ACTION---")
    print("1.attack")
    print("2.use item")
    print("3.skip round")
    action = input("Select number: ")
    
    if not action.isdigit():
        print("Please enter digits only!")

    elif action > "3":
        print("Out of the range of actions!")

    else:
        print("ACCES GRANTED!")
    
    if action == "1":
        dmg = human.deal_damage()
        orc.take_damage(dmg)
        
        print("Player is attacking...")
        time.sleep(2)
        print("             ║-------------------------║\n" 
                f"             ║Player:                  ║\n" 
                f"             ║dealt: {dmg}                 ║\n" 
                f"             ║enemy HP: {orc.health}             ║\n" 
               "             ║-------------------------║\n")
        
        if orc.health <= 0:
            print("You Win!")
            print("---------------")
            loot_item = human.get_loot()
            Player.save_loot(loot_item)
            print(f"INVENTORY: ║{human.inventory}║")
            break

        dmg = orc.deal_damage()
        human.take_damage(dmg)
        
        print("Enemy is attacking...")
        time.sleep(2)
        
        print("             ║-------------------------║\n" 
                f"             ║ENEMY:                   ║\n" 
                f"             ║dealt: {dmg}                 ║\n" 
                f"             ║player HP: {human.health}            ║\n" 
               "             ║-------------------------║\n")
        
        if human.health <= 0:
            print("You Lose!")
            break

    elif action == "2":
        print(Player.load_loot())
        loots = human.load_loot()
        question = input("Item name: ")
        
        if not question in loots:
                print("You dont own that item!")
        
        elif question in loots:
            if question == "Large healing potion":
                if human.health <= 25:
                    human.health += 25
                    print(f"CURRENT HP: {human.health} HEALED: 25")
                else:
                    print("YOU CANT HEAL MORE THAN YOU MAX HP!")
                    continue

            elif question == "Small healing potion":
                if human.health <= 30:
                    human.health += 10
                    print(f"CURRENT HP: {human.health} HEALED: 10")
                else:
                    print("YOU CANT HEAL MORE THAN YOU MAX HP!")
                    continue

            elif question == "Meat":
                if human.health <= 35:
                    human.health += 5
                    print(f"CURRENT HP: {human.health} HEALED: 5")
                else:
                    print("YOU CANT HEAL MORE THAN YOU MAX HP!")
                    continue

            try: 
                if question == "Sword":
                    orc.take_damage(dmg + 3)
                    human.take_damage(dmg)
                    print("             ║-------------------------║\n" 
                    f"             ║Player:                  ║\n" 
                    f"             ║dealt: {dmg}                 ║\n" 
                    f"             ║enemy HP: {orc.health}             ║\n" 
                    f"             ║                         ║\n" 
                    f"             ║ENEMY:                   ║\n" 
                    f"             ║dealt: {dmg}                 ║\n" 
                    f"             ║player HP: {human.health}            ║\n" 
                   "             ║-------------------------║\n")

                elif question == "Iron sword":
                    orc.take_damage(dmg + 5)
                    human.take_damage(dmg)
                    print("             ║-------------------------║\n" 
                    f"             ║Player:                  ║\n" 
                    f"             ║dealt: {dmg}                 ║\n" 
                    f"             ║enemy HP: {orc.health}             ║\n" 
                    f"             ║                         ║\n" 
                    f"             ║ENEMY:                   ║\n" 
                    f"             ║dealt: {dmg}                 ║\n" 
                    f"             ║player HP: {human.health}            ║\n" 
                   "             ║-------------------------║\n")
            
            except NameError:
                print("You need to attack first!")
        
            try:
                human.save_loot_removed(question)
                print(f"Item used: {question}")
        
            except ValueError:
                print("You dont own this item!")
       

        
