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
        """Returns True when order can be made, False if ingredients are insufficient."""
        validity = True
        if self.machine_resources["bread"] < recipes[ingredients]["ingredients"]["bread"]:
            print("Sorry there is not enough bread.")
            validity = False
        if self.machine_resources["ham"] < recipes[ingredients]["ingredients"]["ham"]:
            print("Sorry there is not enough ham.")
            validity = False
        if self.machine_resources["cheese"] < recipes[ingredients]["ingredients"]["cheese"]:
            print("Sorry there is not enough cheese.")
            validity = False
        return validity

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        dollars = int(input("how many dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))
        return dollars + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins == cost:
            return True
        elif coins > cost:
            diff = coins - cost
            print("Here is your change:", diff)
            return True
        else:
            return False

    def make_sandwich(self, sandwich_size):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        self.machine_resources["bread"] -= recipes[sandwich_size]["ingredients"]["bread"]
        self.machine_resources["ham"] -= recipes[sandwich_size]["ingredients"]["ham"]
        self.machine_resources["cheese"] -= recipes[sandwich_size]["ingredients"]["cheese"]


### Make an instance of SandwichMachine class and write the rest of the codes ###
sM = SandwichMachine(resources)
while True:
    selection = input("What would you like? (small/ medium/ large/ off/ report): ")
    if selection == "off":
        break

    elif selection == "small":
        if not sM.check_resources(selection):
            continue
        if sM.transaction_result(sM.process_coins(), recipes[selection]["cost"]):
            sM.make_sandwich(selection)
        else:
            print("insufficient coins")

    elif selection == "medium":
        if not sM.check_resources(selection):
            continue
        if sM.transaction_result(sM.process_coins(), recipes[selection]["cost"]):
            sM.make_sandwich(selection)
        else:
            print("insufficient coins")

    elif selection == "large":
        if not sM.check_resources(selection):
            continue
        if sM.transaction_result(sM.process_coins(), recipes[selection]["cost"]):
            sM.make_sandwich(selection)
        else:
            print("insufficient coins")

    elif selection == "report":
        print("Bread:", sM.machine_resources["bread"], "slice(s)")
        print("Ham:", sM.machine_resources["ham"], "slice(s)")
        print("Cheese:", sM.machine_resources["cheese"], "slice(s)")

    else:
        print("invalid input")