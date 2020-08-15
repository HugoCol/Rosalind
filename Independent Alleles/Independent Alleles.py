from scipy.special import binom
"""
To break down the formula:
First we calculate the probability of every possible outcome in a binominal 
calculation
Then substract the times our desired outcome is not true. from the symbol 
that is used in Binary to represent True : 1
This returns the amount of times our outcome is True
"""

def foo(k, N):
    def p(n, k):
        # This is a binominal calculation for the probability of offspring
        # having AaBb alleles when crossing AaBb x AaBb parents. Defining P
        # in our formula
        return binom(2 ** k, n) * 0.25 ** n * 0.75 ** (2 ** k - n)

    # Next we calculate the probability of having at least N organisms with
    # AaBb. This is done by substracting the amount of times N falls below
    # the required tresshold from 1.
    return 1 - sum(p(n, k) for n in range(N))


if __name__ == '__main__':
    answer = foo(2, 1)
    k = 6 # the generation goal
    n = 15 # the amount of offspring in generation k
    print(round(foo(k, n), 3))
