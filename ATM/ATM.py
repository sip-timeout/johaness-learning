import time

def set_pin():
    user_input = None
    while not pin_input_well_formed_check(user_input):
        user_input = input("Please choose your four digit PIN. ")
    return user_input


def pin_input_well_formed_check(pin_input_to_be_checked):
    if pin_input_to_be_checked == None:
        return False
    try:
        int(pin_input_to_be_checked)
    except:
        print("You entered characters other than digits. Please try again.")
        return False
    if len(pin_input_to_be_checked) < 4:
        print("You did not enter enough digits. Please try again.")
        return False
    if len(pin_input_to_be_checked) > 4:
        print("You entered too many digits. Please try again.")
        return False
    if int(pin_input_to_be_checked) < 0:
        print("Please refrain from trying to enter a negative number. Thank you.")
        return False
    else:
        print("Thank you. You have set your pin to:" + pin_input_to_be_checked)
        return True


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


def set_initial_balance():
    balance = input("Please enter your initial balance. ")
    while not is_input_a_positive_float_with_a_max_of_two_decimal_places_check(balance):
        balance = input("Please enter your initial balance. ")
    print("Thank you.")
    time.sleep(1)
    return balance


def is_input_a_positive_float_with_a_max_of_two_decimal_places_check(input_to_be_checked):
    try:
        float(input_to_be_checked)
    except:
        print("You entered characters other than digits. Please try again.")
        return False

    if float(input_to_be_checked) <= 0:
        print("Please enter a positive amount.")
        return False

    if "." in input_to_be_checked:
        if len((input_to_be_checked.split("."))[1]) > 2:
            print("Please enter an amount without fractions of cents.")
            return False
        else:
            return True
    else:
        return True


def withdraw():
    amount_chosen = input("How much money would you like to withdraw? You may withdraw 20 EUR, 50 EUR or (O)ther amount.")

    while not amount_chosen in ["20", "50", "O"]:
        print("Please use one of the options provided.")
        amount_chosen = input(
            "How much money would you like to withdraw? You may withdraw 20 EUR, 50 EUR or (O)ther amount.")

    if amount_chosen == "O":
        amount_chosen = input("Please enter the amount you would like to withdraw. ")
        while not is_input_a_positive_float_with_a_max_of_two_decimal_places_check(amount_chosen):
            amount_chosen = input("Please enter the amount you would like to withdraw. ")

    amount_chosen = float(amount_chosen)

    if check_if_balance_allows_withdrawal(amount_chosen):
        update_balance(amount_chosen)
        print("Here you go!")
        time.sleep(1)

    else:
        print("You do not have enough money.")


def withdraw_other_amount():
    input_amount = input("Please enter the amount you would like to withdraw. ")
    while not is_input_a_positive_float_with_a_max_of_two_decimal_places_check(input_amount):
        input_amount = input("Please enter the amount you would like to withdraw. ")
    return input_amount


def update_balance(amount_withdrawn):
    global balance
    balance = balance - float(amount_withdrawn)


def change_pin():
    global pin
    pin = set_pin()
    print("You have successfully changed your PIN.")


def check_if_balance_allows_withdrawal(amount_to_be_tested):
    if balance - amount_to_be_tested > 0:
        return True
    else:
        return False


def __main__():
    global pin
    global balance

    print("Welcome.")

    pin = set_pin()

    balance = float(set_initial_balance())

    menu_option_chosen = None
    while not menu_option_chosen == "E":
        print(
            """Menu. What would you like to do?"
            \n(A)ccount Balance
            \n(W)ithdraw Money
            \n(C)hange PIN
            \n(E)xit""")
        menu_option_chosen = input()

        if menu_option_chosen == "A":
            if pin_check(pin):
                print("Your current account balance is " + str(balance) + ".")

        if menu_option_chosen == "W":
            if pin_check(pin):
                withdraw()

        if menu_option_chosen == "C":
            if pin_check(pin):
                change_pin()

        if menu_option_chosen not in ["A","W","C","E"]:
            print("Please choose one of the options provided.")

    print("Bye!")

__main__()



