#TERMINAL BASED RPG GAME(Player file)
import random
import json


class Player:
    def __init__(self, name, health, inventory=None):
        self.name = name
        self.health = health
        self.inventory = inventory if inventory else []

    def deal_damage(self):
        return random.randint(1, 10)
        
    def take_damage(self, damage):
        self.health -= damage
        
    def info(self):
        return f"Name: {self.name} \nHP: {self.health}"
    
    def get_loot(self):
        loot_table = ["Large healing potion","Small healing potion", "Meat", "Sword", "Iron sword"]
        
        item = random.choice(loot_table)
        self.inventory.append(item) # Add to player's inventory
        return item

    @staticmethod
    def load_loot():
        try:
            with open("loot.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_loot(item):
        loot = Player.load_loot()  # load existing loot
        loot.append(item)          # append new item
        with open("loot.json", "w") as f:
            json.dump(loot, f, indent=4)
    
    def save_loot_removed(self, x):
        removed = Player.load_loot()
        removed.remove(x)
        with open("loot.json", "w") as f:
            json.dump(removed, f, indent=4)

        