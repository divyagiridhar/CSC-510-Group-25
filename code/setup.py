import sys
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    arg = sys.argv
    n = int(arg[1])
    print("factorial of {} is {}".format(n,factorial(n)))
