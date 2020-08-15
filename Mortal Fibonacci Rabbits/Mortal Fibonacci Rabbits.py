def fibonacci(n,m):
    """Made a good fibonaccy sequence, now add the mortality factor"""

    if n==0:
        return 1
    if n==1:
        return 1
    else:

        return (fibonacci(n-1,m) + fibonacci(n-2,m))




if __name__ == '__main__':
    n = 8
    m = 3
    for i in range(n):
        print(fibonacci(i,m))
