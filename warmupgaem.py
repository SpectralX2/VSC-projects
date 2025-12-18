import random

class Enemy:
  def __init__(self, name, health, attack):
    self.name = name
    self.health = health
    self.attack = attack

enemies = [
  Enemy("Goblin", 20, 5),
  Enemy("Skeleton", 30, 8),
  Enemy("Troll", 50, 15)
]

def random_encounter():
  current_enemy = random.choice(enemies)
  
  print(f"A wild {current_enemy.name} appears!")
  print(f"Stats: Health = {current_enemy.health}, Attack = {current_enemy.attack}")
  
  action = input("What do you do? (attack/run): ").lower()
  
  if action == "attack":
    damage_dealt = 5
    current_enemy.health -= damage_dealt
    print(f"You hit the {current_enemy.name} for {damage_dealt} damage!")
    print(f"The {current_enemy.name} now has {current_enemy.health} health left.")
  elif action == "run":
    print("You successfully escaped!")
  else:
    print("Invalid action. The enemy stares at you, confused.")

random_encounter()