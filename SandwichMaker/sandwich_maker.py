import data

class sandwich_maker:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        validity = True
        if self.machine_resources["bread"] < data.recipes[ingredients]["ingredients"]["bread"]:
            print("Sorry there is not enough bread.")
            validity = False
        if self.machine_resources["ham"] < data.recipes[ingredients]["ingredients"]["ham"]:
            print("Sorry there is not enough ham.")
            validity = False
        if self.machine_resources["cheese"] < data.recipes[ingredients]["ingredients"]["cheese"]:
            print("Sorry there is not enough cheese.")
            validity = False
        return validity

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        self.machine_resources["bread"] -= order_ingredients[sandwich_size]["ingredients"]["bread"]
        self.machine_resources["ham"] -= order_ingredients[sandwich_size]["ingredients"]["ham"]
        self.machine_resources["cheese"] -= order_ingredients[sandwich_size]["ingredients"]["cheese"]