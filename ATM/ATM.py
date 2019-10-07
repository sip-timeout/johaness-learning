import time
import re

class Pin(object):
    def __init__(self, pin_value):
        self.pin_value = pin_value

    def set_pin(self):
        user_input = input("Please enter the PIN you would like to use: ")
        while re.match("^\d\d\d\d$",user_input) is None:
            user_input = input("Please enter a well-formed PIN(four digits): ")
        self.pin_value = user_input

    def get_pin(self):
        return self.pin_value


class Balance(object):
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        self.balance = new_balance


def pin_check(pin):
    number_of_wrong_pin_entries = 0
    while number_of_wrong_pin_entries < 3:
        pin_entry = input("Please enter your four digit PIN ")
        if pin_entry == pin:
            return True
        else:
            number_of_wrong_pin_entries += 1
            print("Number of wrong pin entries " + str(number_of_wrong_pin_entries))
    print("You have entered a wrong PIN three times. Your card has been blocked. Have a nice day.")
    quit()


def set_initial_balance(balance):
    balance.set_balance(input("Please enter your initial balance. "))
    while not is_input_a_positive_float_with_a_max_of_two_decimal_places_check(balance.get_balance()):
        print("Your initial balance must be positive and cannot contain more than two decimals after the dot.")
        balance.set_balance(input("Please enter your initial balance. "))
    print("Thank you.")
    # This sleep is just for a comfortable user experience. IMO it feels more organic to have the menu appear only
    # after a second.
    time.sleep(1)
    return balance.get_balance


def is_input_a_positive_float_with_a_max_of_two_decimal_places_check(input_to_be_checked):
    for x in input_to_be_checked:
        if re.match("[0-9.]", x) is None:
            return False

    if len(re.findall("\.", input_to_be_checked))>1:
            return False

    # Checking whether the dot is in the second or third last position:
    elif len(re.findall("\.", input_to_be_checked))==1 and not (input_to_be_checked[len(input_to_be_checked) - 2] == "." or input_to_be_checked[len(input_to_be_checked) - 3] == "."):
        return False

    return True


def withdraw(balance):
    amount_chosen = input("How much money would you like to withdraw? You may withdraw 20 EUR, 50 EUR or (O)ther amount.")

    while not amount_chosen in ["20", "50", "O"]:
        print("Please use one of the options provided.")
        amount_chosen = input(
            "How much money would you like to withdraw? You may withdraw 20 EUR, 50 EUR or (O)ther amount.")

    if amount_chosen == "O":
        amount_chosen = input("Please enter the amount you would like to withdraw. ")
        while not is_input_a_positive_float_with_a_max_of_two_decimal_places_check(amount_chosen):
            print("You may choose any positive amount with a maximum of two decimal places.")
            amount_chosen = input("Please enter the amount you would like to withdraw. ")

    amount_chosen = float(amount_chosen)

    if check_if_balance_allows_withdrawal(amount_chosen,balance):
        update_balance(amount_chosen,balance)
        print("Here you go!")
        time.sleep(1)

    else:
        print("You do not have enough money.")


def withdraw_other_amount():
    input_amount = input("Please enter the amount you would like to withdraw. ")
    while not is_input_a_positive_float_with_a_max_of_two_decimal_places_check(input_amount):
        input_amount = input("Please enter the amount you would like to withdraw. ")
    return input_amount


def update_balance(amount_withdrawn, balance):
    balance.set_balance(float(balance.get_balance()) - float(amount_withdrawn))

def check_if_balance_allows_withdrawal(amount_to_be_tested, balance):
    return float(balance.get_balance()) - amount_to_be_tested >= 0

def __main__():
    print("Welcome.")

    pin = Pin(None)
    pin.set_pin()
    print("You have set your PIN to " + str(pin.get_pin()) + ".")

    balance = Balance(None)
    set_initial_balance(balance)

    menu_option_chosen = None
    while not menu_option_chosen == "E":
        print(
            """Menu. What would you like to do?"
            \n(A)ccount Balance
            \n(W)ithdraw Money
            \n(C)hange PIN
            \n(E)xit""")
        menu_option_chosen = input()

        if menu_option_chosen in ["A","W","C"]:
            if pin_check(pin.get_pin()):
                if menu_option_chosen == "A":
                    print("Your current account balance is " + str(balance.get_balance()) + ".")

                elif menu_option_chosen == "W":
                    withdraw(balance)

                elif menu_option_chosen == "C":
                    # change_pin()
                    pin.set_pin()

        if menu_option_chosen not in ["A","W","C","E"]:
            print("Please choose one of the options provided.")

    print("Bye!")

__main__()



