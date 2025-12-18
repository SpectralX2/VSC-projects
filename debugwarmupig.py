from random import randint

class Enemy:
    def __init__(self, name, x, y, hp):
        self.name = name
        self.x = x
        self.y = y
        self.hp = hp
 
    def move_towards(self, tx, ty):
        if tx > self.x:
            self.x += 1
        elif tx < self.x:
            self.x -= 1
        if ty > self.y:
            self.y += 1
        elif ty < self.y:
            self.y -= 1
 
    def take_damage(self, amount):
        self.hp -= amount   
 
    def is_dead(self):
        return self.hp <= 0  
 
    def __repr__(self):
        return f"{self.name}({self.x},{self.y}) HP:{self.hp}"
 
 
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
def spawn_enemies(enemies, count, area):
    for i in range(count):
        e = Enemy("Goblin", randint(0, area-1), randint(0, area-1), 10)
        enemies.append(e)
    return enemies
 
def main():
    enemies = []
    enemies = spawn_enemies(enemies, 3, 10)
    player = Player(5, 5)
 
    for turn in range(1,6):
        print(f"\n-- Turn {turn} --")
        for e in enemies:
            e.move_towards(player.x, player.y)
            print(f"{e} moved to ({e.x},{e.y})")
            if abs(e.x - player.x) + abs(e.y - player.y) <= 1:
                print(f"{e.name} is close! Player hits for 5.")
                e.take_damage(5)
        enemies = [e for e in enemies if not e.is_dead()]
        print("Alive enemies:", enemies)
 
if __name__ == "__main__":
    main()