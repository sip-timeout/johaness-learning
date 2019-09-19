def __main__():
    sum = 0
    user_input = input("Welcome to ListSum. I will tell you the sum of all the numbers you give me. Please give me the numbers you'd like to be summed, separated by commas, eg '1,2,3,-3400, 234'. Thanks!")
    user_input_split_by_commas = user_input.split(",")
    print(user_input_split_by_commas)
    try:
        for x in range(len(user_input_split_by_commas)):
            sum += float(user_input_split_by_commas[x])
        print(sum)
    except:
        print("Sorry, that input was not in the format I asked you to use. Please try again by running the programm again.")

__main__()