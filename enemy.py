#TERMINAL BASED RPG GAME(Enemy save)
import random

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def deal_damage(self):
        return random.randint(1, 10)

    def take_damage(self, damage):
        self.health -= damage

    def info(self):
        return f"Name: {self.name} \nHP: {self.health}"