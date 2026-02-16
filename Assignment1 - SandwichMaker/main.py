from sandwich_maker import sandwich_maker as SandwichMachine
import data
import cashier

resources = data.resources
cashier = cashier.cashier()

### Make an instance of SandwichMachine class and write the rest of the codes ###
sM = SandwichMachine(resources)
while True:
    selection = input("What would you like? (small/ medium/ large/ off/ report): ")
    if selection == "off":
        break

    elif selection == "small":
        if not sM.check_resources(selection):
            continue
        if cashier.transaction_result(cashier.process_coins(), data.recipes[selection]["cost"]):
            sM.make_sandwich(selection, data.recipes)
            print(selection, "sandwich is ready. Bon appetit!")
        else:
            print("Sorry, that’s not enough money. Money refunded")

    elif selection == "medium":
        if not sM.check_resources(selection):
            continue
        if cashier.transaction_result(cashier.process_coins(), data.recipes[selection]["cost"]):
            sM.make_sandwich(selection, data.recipes)
            print(selection, "sandwich is ready. Bon appetit!")
        else:
            print("Sorry, that’s not enough money. Money refunded")

    elif selection == "large":
        if not sM.check_resources(selection):
            continue
        if cashier.transaction_result(cashier.process_coins(), data.recipes[selection]["cost"]):
            sM.make_sandwich(selection, data.recipes)
            print(selection, "sandwich is ready. Bon appetit!")
        else:
            print("Sorry, that’s not enough money. Money refunded")

    elif selection == "report":
        print("Bread:", sM.machine_resources["bread"], "slice(s)")
        print("Ham:", sM.machine_resources["ham"], "slice(s)")
        print("Cheese:", sM.machine_resources["cheese"], "slice(s)")

    else:
        print("invalid input")