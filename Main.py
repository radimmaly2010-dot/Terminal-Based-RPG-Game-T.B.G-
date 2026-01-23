# THE CORE
from player import *
import random
import time
from enemy import Orc, Summoner, Bat, Troll, Goblin_king, Slime, Assasin

def main():
    enemies = [
        #Orc(), 
        #Troll(), 
        #Summoner(), 
        Assasin(), 
        #Goblin_king(), 
        #Bat(), 
        #Slime(),
        ]
        

    enemy = random.choice(enemies)
    while True:
        question = input("Are u ready for dungeon(Y or N): ").lower()
        if question == "n":
            print("...")
            continue
        elif question != "y":
            print("Invalid, Please try again!\n")
        else:
            print("Lets begin!!\n")
            break

    print("║-------------------------║\n"
          f"║Player:                  ║\n"
          f"║Name: {human.name}                ║\n"
          f"║Player HP: {human.health}❤           ║\n"
          f"║                         ║\n"
          f"║ENEMY:                   ║\n"
          f"║Name: {enemy.name}              \n"
          f"║Enemy HP: {enemy.health}❤            ║\n"
          "║-------------------------║\n")

    while True:
        print("---HUMAN ACTION---")
        print("1.attack")
        print("2.use item")
        action = input("Select number: ")

        if not action.isdigit():
            print("Please enter digits only!")
            continue
        elif action > "2":
            print("Out of the range of actions!")
            continue

        if action == "1":
            dmg = human.deal_damage()
            enemy.take_damage(dmg)

            print("Player is attacking...")
            time.sleep(2)
            print("             ║-------------------------║\n"
                  f"             ║Player:                  ║\n"
                  f"             ║dealt: {dmg}🩸               ║\n"
                  f"             ║enemy HP: {enemy.health}❤            ║\n"
                  "             ║-------------------------║\n")

            if enemy.health <= 0:
                print("Enemy defeated💀")
                print("You Win!")
                print("---------------")
                loot_item = human.get_loot()
                Player.save_loot(loot_item)
                print(f"INVENTORY: ║{human.inventory}║")
            
            #ENEMY ABILITIES
            elif isinstance(enemy, Orc) and enemy.health <= 20:
                enemy.ability()

            #elif isinstance(enemy, Summoner):
                #enemy.ability()

            #elif isinstance(enemy, Goblin_king):
                #enemy.ability()

            elif isinstance(enemy, Bat):
                print("BAT passive: [!vampirism!]")
                enemy.ability()

            else:
                dmg = enemy.deal_damage()
                human.take_damage(dmg)

                print("Enemy is attacking...")
                time.sleep(2)
                print("             ║-------------------------║\n"
                    f"             ║ENEMY:                   ║\n"
                    f"             ║dealt: {dmg}🩸               ║\n"
                    f"             ║player HP: {human.health}❤           ║\n"
                   "             ║-------------------------║\n")
                
                if isinstance(enemy, Troll) and enemy.health <= 10:
                    print("TROLL is using: [!regeneration!]")
                    enemy.ability()
                
                elif isinstance(enemy, Slime):
                    print("SLIME using ability: [!CLONE!]")
                    enemy.ability()
                
                elif isinstance(enemy, Assasin):
                    action1 = input("Ability(Y / N): ").lower()
                    count = 0
                    if action1 == "y" and count == 0:
                        enemy.ability()
                        count += 1


                elif human.health <= 0:
                    print("You lose")
                    break

        elif action == "2":
            print(Player.load_loot())
            loots = human.load_loot()
            question = input("Item name: ")

            if question not in loots:
                print("You dont own that item!")

            elif question in loots:
                if question == "Large healing potion":
                    if human.health <= 35:
                        human.health += 25
                        print(f"CURRENT HP: {human.health} HEALED: 25")
                    
                    else:
                        print("YOU CANT HEAL MORE THAN YOU MAX HP!")
                        continue

                elif question == "Small healing potion":
                    if human.health <= 50:
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
                        enemy.take_damage(dmg + 3) 
                        human.take_damage(dmg) 
                        print(" ║-------------------------║\n" 
                              f" ║Player: ║\n" f" ║dealt: {dmg}🩸 ║\n" 
                              f" ║enemy HP: {enemy.health}❤ ║\n" f" ║ ║\n" 
                              f" ║ENEMY: ║\n" f" ║dealt: {dmg}🩸 ║\n" 
                              f" ║player HP: {human.health}❤ ║\n" 
                             " ║-------------------------║\n")


                    elif question == "Iron sword":
                        enemy.take_damage(dmg + 5) 
                        human.take_damage(dmg) 
                        print(" ║-------------------------║\n" 
                              f" ║Player: ║\n" f" ║dealt: {dmg}🩸 ║\n" 
                              f" ║enemy HP: {enemy.health} ║\n" f" ║ ║\n" 
                              f" ║ENEMY: ║\n" f" ║dealt: {dmg}🩸 ║\n" 
                              f" ║player HP: {human.health} ║\n" 
                              " ║-------------------------║\n")

                except NameError:
                    print("You need to attack first!")

                try:
                    human.save_loot_removed(question)
                    print(f"Item used: {question}")
                
                except ValueError:
                    print("You dont own this item!")
        
if __name__ == "__main__":
    main()
