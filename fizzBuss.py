def fizzBuzz(n):
    for i in range(1, n + 1):  # Include n in the range
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)  # No need for 'return' here; just print

if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)
