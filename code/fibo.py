import sys

def fibonacci(n):
	if n <= 1:
		return n
	return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    arg = sys.argv
    n = int(arg[1])
    print("The {}th fibonacci number is {}".format(n,fibonacci(n)))