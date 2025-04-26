import time
import random

inventory = {"torch": 2}

def print_inventory():
    global inventory
    for (k, v) in inventory.items():
        print("%s: %d" % (k, v))
def print_output(decision):
    choice = "i"
    while (choice == "i"):
        choice = input("{0} [y/n] \nEnter i to see you inventory. ".format(decision))
        if (choice == "i"):
            print_inventory()
    if choice in ['y', 'Y', 'Yes', 'YES', 'yes']:
        return True
    return False

def cyclops_battle (stick):
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (" Fighting... ")
    print (" You must have above a 5 to kill the cyclops.        ")
    print ("If the cyclops hits higher than you, you will die    ")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(2)

    if stick:
        your_hit = int(random.randint(3,10))
    else:
        our_hit = int(random.randint(1, 8))
    cyclops_hit = int(random.randint(1, 5))
    print ("you hit a", your_hit)
    print ("the cyclops hits a", cyclops_hit)
    time.sleep(2)

if cyclops_hit > your_hit:
    print ("The cyclops has dealt more damage than you!")
    complete = 0
    return complete

elif your_hit < 5:
    print ("You didnt do enough damange to kill the cyclops, but you manage to escape")
    complete = 1
    return complete

else:
    print("You killed the cyclops!")
    complete = 1
    return complete

def gamme():
    global inventory
    inventory = {"torch": 2}

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the Cavern Adventure!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(2)
    print("You enter a dark cavern out of curiosity/ It is dark and you can only make out a small stick on the floor.")

    if print_output("Do you take it?"):
        num = random.random()
        if num < 0.8:
            print("You have taken the stick!")
            time.sleep(2)
            inventory["stick"] = 1
        else:
            print("Oh no! The stick was actuall a snake.")
            time.sleep(1)
            complete = 0
            return complete
        
    else:
        print("You did not take the stick")
    print("As you proceed further into the cave, you see a large glowing object")

    if print_output("Do you approach the object?"):
        print("You approach the object...")
        time.sleep(2)
        print("As you draW closer, you begin to ake out the object as an eye!")
        time.sleep(1)
        print("The eye belongs to a giant cyclops!")

        if print_output("Do you try to fight it?"):
            if "stick" in list(inventory.keys()):
                print("You only have a stick to fight with!")
                print("You quickly jab the cyclops in it's eye and gain an advntage")
                time.sleep(2)
                return cyclops_battle(True)
        else:
            print("You don't have anything to fight with!")
            time.sleep(2)
            return cyclops_battle(False)
        
    print("You choose not to fight the cyclops.")
    time.sleep(1)
    print("As you turn away, it ambushes you and grabs by the ")


def main():
    alive = True
    while alive:
        complete = game()
        if complete == 1:
            alive = print_output("You managed to escape the cavern alive! Would you like ot play again?")
        else:
            alive = print_output("You have died! Would you like to play again?")

if __name__ == "__main__":
    main()