# Return: The total number of rabbit pairs that will be present after n months,
# if we begin with 1 pair and in each generation,
# every pair of reproduction-age rabbits produces a litter of k rabbit pairs
# (instead of only 1 pair).
#

# # amount of generations
# genertions, litter_size = input("Enter generation amount to run, and litter size").split()
# # amount of rabbits per litter
# print(genertions , litter_size)

# amount of rabbits after n generations and k rabbits per litter

months = 36

litterSize = 4
# This is just a basic Fibonacci function with a littersize as a variabele
# The only function of this variabele is to multiple the oldest number as you add two numbers up in the sequence
# This is to accomodate for the fact that rabbits have multiple offspring
def rabbits(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 1
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return rabbits(n - 1) + litterSize*(rabbits(n - 2))

        # Driver Program



if __name__ == '__main__':
    # for i in range(1,months):
    print(rabbits(months))