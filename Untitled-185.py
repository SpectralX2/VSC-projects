class Shopkeeper:
    def __init__(self, shop_name, inventory):
        self.shop_name = shop_name
        self.inventory = inventory

    def greet_customer(self):
        print(f"Welcome to {self.shop_name}! How can I help you today?")

    def list_items(self):
        print(f"Items in stock at {self.shop_name}:")
        for item, price in self.inventory.items():
            print(f"{item}: ${price}")

    def take_order(self, item_name, quantity):
        if item_name in self.inventory:
            if quantity <= 0:
                print("Please order a positive quantity.")
                return None
            price = self.inventory[item_name] * quantity
            return price
        else:
            print(f"Sorry, we don't have {item_name} in stock.")
            return None

    def charge_customer(self, amount):
        if amount is not None:
            print(f"Your total is: ${amount}")
            print("Thank you for shopping with us! Have a great day!")
        else:
            print("Unable to process your order. Please try again.")

class Town:
    def __init__(self):
        self.shops = {}

    def add_shop(self, shopkeeper):
        self.shops[shopkeeper.shop_name] = shopkeeper

    def visit_shop(self, shop_name):
        if shop_name in self.shops:
            shopkeeper = self.shops[shop_name]
            print(f"You're now visiting {shopkeeper.shop_name}.")
            shopkeeper.greet_customer()

            while True:
                shopkeeper.list_items()
                order_item = input("Enter the item you want to buy (or type 'exit' to leave): ").capitalize()

                if order_item == 'Exit':
                    print("Thank you for visiting! Goodbye.")
                    break

                if order_item not in shopkeeper.inventory:
                    print("Sorry, we don't have that item.")
                    continue

                try:
                    order_quantity = int(input(f"How many {order_item}s would you like to buy? "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                order_total = shopkeeper.take_order(order_item, order_quantity)
                shopkeeper.charge_customer(order_total)
        else:
            print("That shop doesn't exist in the town.")

def main():
    inventory1 = {"Apple": 1.50, "Banana": 0.75, "Guava": 2.00, "Orange": 1.25, "Strawberries": 1.75}
    inventory2 = {"Water": 1.00, "Juice": 1.50, "Cookies": 2.50, "Potato Chips": 5.00, "Muffin": 3.25, "Soda": 2.00}

    shopkeeper1 = Shopkeeper("The Fruit Stand", inventory1)
    shopkeeper2 = Shopkeeper("The Drink & Snack Bar", inventory2)

    town = Town()
    town.add_shop(shopkeeper1)
    town.add_shop(shopkeeper2)

    print("Welcome to the Town Market!")

    while True:
        print("\nAvailable Shops:")
        for shop_name in town.shops:
            print(f"- {shop_name}")

        shop_choice = input("\nWhich shop would you like to visit (or type 'exit' to leave)? ").strip()

        if shop_choice.lower() == "exit":
            print("Thank you for visiting! Have a great day!")
            break

        matched_shop = None
        for shop_name in town.shops:
            if shop_choice.lower() == shop_name.lower():
                matched_shop = shop_name
                break

        if matched_shop:
            town.visit_shop(matched_shop)
        else:
            print("That shop doesn't exist in the town.")
            
if __name__ == "__main__":
    main()