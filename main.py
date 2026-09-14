### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False

        return True

    def process_coins(self):
        #test#
        print("Please insert coins.")

        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = (
                large_dollars * 1.00
                + half_dollars * 0.50
                + quarters * 0.25
                + nickels * 0.05
        )

        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]

        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)

machine_on = True

while machine_on:
    choice = input(
        "What would you like? (small/ medium/ large/ off/ report): "
    ).lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        print(f"Bread: {machine.machine_resources['bread']} slice(s)")
        print(f"Ham: {machine.machine_resources['ham']} slice(s)")
        print(f"Cheese: {machine.machine_resources['cheese']} pound(s)")

    elif choice in recipes:
        sandwich = recipes[choice]
        ingredients = sandwich["ingredients"]
        cost = sandwich["cost"]

        if machine.check_resources(ingredients):
            money_inserted = machine.process_coins()

            if machine.transaction_result(money_inserted, cost):
                machine.make_sandwich(choice, ingredients)

    else:
        print("Invalid selection.")