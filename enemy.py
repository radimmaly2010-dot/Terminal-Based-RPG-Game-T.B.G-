#TERMINAL BASED RPG GAME(Enemy save)
import random
from player import *
import time

class Enemy:
    def __init__(self, health, name):
        self.health = health
        self.name = name

    def deal_damage(self):
        pass

    def take_damage(self):
        pass

    def info(self):
        pass

class Orc(Enemy):
    def __init__(self):   
        super().__init__(health = 40, name="Zyrog")
    
    def deal_damage(self):
        return random.randint(1, 10)
    
    def take_damage(self, damage):
        self.health -= damage

    def ability(self):
        time.sleep(2)
        dmg = random.randint(4, 15)
        print("ORC IS USING HIS ABILITY:[!RAGE!]")
        print("             ║-------------------------║\n"
    f"             ║ENEMY:                   ║\n"
    f"             ║dealt(with ability): {human.take_damage(dmg)}🩸               ║\n"
    f"             ║player HP: {human.health}❤           ║\n"
   "             ║-------------------------║\n")
        

class Troll(Enemy):
    def __init__(self):
        super().__init__(health = 20, name="Pyrgon")
    
    def deal_damage(self):
        return random.randint(4, 10)
    
    def take_damage(self, damage):
        self.health -= damage
    
    def ability(self):
        self.health += 3
        print(f"current HP: {self.health} Healed: 3")

class Slime(Enemy):
    def __init__(self):
        super().__init__(health=15, name="Slimik") 
    
    def deal_damage(self):
        return random.randint(1, 4)
    
    def take_damage(self, damage):
        self.health -= damage
    
    def ability(self):
        alive = True
        class Clone_slime(Enemy):
            def __init__(self):
                super().__init__(health=15, name="Slimik1")
                
                def deal_damage(self):
                    return random.randint(1, 4)
                
                def take_damage(damage):
                    self.health -= damage      
        
        Clone_slime()

        while alive:
            dmg = self.deal_damage()
            dmg1 = human.deal_damage()
            self.take_damage(dmg1)
            time.sleep(2)
            print("             ║-------------------------║\n"
    f"             ║ENEMY:                   ║\n"
    f"             ║dealt(Clone): {human.take_damage(dmg)}🩸               ║\n"
    f"             ║player HP: {human.health}❤           ║\n"
   "             ║-------------------------║\n")
            time.sleep(2)
            print("║-------------------------║\n"
            f"║Player:                  ║\n"
            f"║dealt: {dmg1}🩸               ║\n"
            f"║enemy HP: {self.health}❤            ║\n"
            "║-------------------------║\n")
            
            if self.health <= 0:
                alive = False

class Goblin_king(Enemy):
    def __init__(self):
        super().__init__(health = 60, name="king karek")
    
    def deal_damage(self):
        return random.randint(1, 10)
    
    def take_damage(self, damage):
        self.health -= damage

    def ability():
        print("")

class Bat(Enemy):
    def __init__(self):
        super().__init__(health = 15, name="Vimpare")
    
    def deal_damage(self):
        return random.randint(1, 4)
    
    def take_damage(self, damage):
        self.health -= damage

    def ability(self):
        vamp = self.deal_damage()
        time.sleep(2)
        print("             ║-------------------------║\n"
    f"             ║ENEMY:                   ║\n"
    f"             ║dealt: {human.take_damage(vamp)}🩸               ║\n"
    f"             ║player HP: {human.health}❤           ║\n"
   "             ║-------------------------║\n")
        
        self.health += vamp
        print(f"BAT vampired: {vamp} current HP: {self.health}")

class Assasin(Enemy):
    def __init__(self):
        super().__init__(health = 10, name="Deadla")
    
    def deal_damage(self):
        return random.randint(7, 15)
    
    def take_damage(self, damage):
        self.health -= damage
    
    def ability(self):
        dmg = self.deal_damage()
        for _ in range(2):
            print("ASSASIN IS USING HIS ABILITY:[!DOUBLE HIT!]")
            print("             ║-------------------------║\n"
        f"             ║ENEMY:                   ║\n"
        f"             ║dealt(with ability): {human.take_damage(dmg)}🩸               ║\n"
        f"             ║player HP: {human.health}❤           ║\n"
    "             ║-------------------------║\n")
            break


class Summoner(Enemy):
    def __init__(self):
        super().__init__(health = 10, name="Suminko")
    
    def deal_damage(self):
        return random.randint(1, 3)
    
    def take_damage(self, damage):
        self.health -= damage
