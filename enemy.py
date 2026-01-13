#TERMINAL BASED RPG GAME(Enemy save)
import random

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
        return random.randint(1, 15)

class Troll(Enemy):
    def __init__(self):
        super().__init__(health = 20, name="Pyrgon")
    
    def deal_damage(self):
        return random.randint(4, 10)
    
    def take_damage(self, damage):
        self.health -= damage

class Slime(Enemy):
    def __init__(self):
        super().__init__(health=15, name="Slimik") 
    
    def deal_damage(self):
        return random.randint(1, 4)
    
    def take_damage(self, damage):
        self.health -= damage

class Goblin_king(Enemy):
    def __init__(self):
        super().__init__(health = 60, name="king karek")
    
    def deal_damage(self):
        return random.randint(1, 10)
    
    def take_damage(self, damage):
        self.health -= damage

class Bat(Enemy):
    def __init__(self):
        super().__init__(health = 15, name="Vimpare")
    
    def deal_damage(self):
        return random.randint(1, 4)
    
    def take_damage(self, damage):
        self.health -= damage

class Assasin(Enemy):
    def __init__(self):
        super().__init__(health = 10, name="Deadla")
    
    def deal_damage(self):
        return random.randint(7, 15)
    
    def take_damage(self, damage):
        self.health -= damage

class Summoner(Enemy):
    def __init__(self):
        super().__init__(health = 10, name="Suminko")
    
    def deal_damage(self):
        return random.randint(1, 3)
    
    def take_damage(self, damage):
        self.health -= damage
