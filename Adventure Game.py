player = {'location': 'cabin'}
game_map = {'cabin':{'east':'yard'}, 'yard':{'east':'forest', 'south':'barn','west':'cabin'},'forest':{'west': 'yard'}, 'barn':{'north': 'yard'}}
descriptions = {'cabin': 'You are in a quaint cabin, there is a door to the east.',
    'yard':'You find yourself in a beautiful garden. There is a forest to the east, a barn to the south, and a cabin to the west.',
    'forest':'You are in a spooky forest. The yard is back to the west.',
    'barn': 'You are in a barn. There is a treasure chest in the middle of the room. The yard lies to the north.'}
#directions = ['north','east','south','west']
items = {'cabin': [],'yard':[],'forest':['key'],'barn':[]}
win_events = {'key barn': 'You unlocked the treasure chest! You Win'}
game_over = False

def look(location):
    print(descriptions[location])
    if len (items [location]) > 0:
        for item in items [location]:
            print("There is a {} here.".format(item))

def move(direction):
    if direction in game_map[player['location']]:
        player['location'] = game_map[player['location']][direction]
        look(player['location'])
    else:
        print("You cannot go {}.".format(direction))

def inventory():
    if len(player["inventory"]) > 0:
        for item in player["inventory"]:
            print('You are carrying a {}.'.format(item))
    else:
        print("You are not carrying anything")

def get_item(item):
    if item in items[player['location']]:
        player['inventory'].append(item)
        items[player['location']].remove(item)
        print("You picked up the {}.".format(item))
    else:
        print("There is no {} here.".format(item))

def drop_item(item):
    if item in player['inventory']:
        items[player['location']].append(item)
        player['inventory'].remove(item)
        print("You are no longer carrying the {}.".format(item))

def use_item(item):
    global game_over
    if item in player['inventory']:
        if item+" "+player['location'] in win_events:
            print(win_events[items+" "+player['location']])
            game_over = True
        else:
            print("You cannot use the {} here.".format(item))
    else:
        print("You are not carring a {}.".format(item))

def main():
    global game_over
    look(player['location'])
    while not game_over:
        choice = input("What would you like to do?\n").split(" ")
        if choice[0] = 'go':
            move(choice[1])
        elif choice[0] == 'get':
            get_item(choice[1])
        elif choice[0] == 'use':
            use_item(choice[1])
        elif choice[0] == 'drop':
            drop_item(choice[1])
        elif choice[0] == 'inventory':
            inventory()
        elif choice[0] == 'look':
            look(player['location'])
        elif choice[0] == 'quit':
            print("Goodbye!!!")
            game_over = True

        elif choice[0] == 'help':
            print("\nInstructions:\n")
            print("Enter 'go <'north', 'east', 'south', 'west'>' to move")
            print("Enter 'look' to view the room or 'inventory' to view your inventory")
            print("Type 'get <item name>' to acquire items")
            print("Type 'drop <item name>' to get rid of items")
            print("Type 'use <item name>' to use items")
            print("Type 'quit' to exit the game")
        else:
            print("I don't understand {}".format(choice[0]))

if __name__ == '__main__':
    main()