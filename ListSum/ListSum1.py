def __main__():
    sum = 0
    user_input = None
    print("Welcome to ListSum. I will tell you the sum of all the numbers you give me. Once you have given me all the numbers you would like to be summed, please type 'stop'. Thanks!")
    while not user_input == "stop":
        user_input = input("Give me a number you would like to be added to the current sum or type 'stop' to, well, stop.")
        try:
            sum += float(user_input)
        except:
            print("It seems you tried to input something that was neither a number nor the word 'stop'. Please try again!")
        print("Currently, the sum of the numbers you gave me is " + str(sum))
    print("Your final sum is " + str(sum) + ". Have a nice day!")

__main__()