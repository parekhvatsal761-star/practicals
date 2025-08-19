import time


def factorial_iter(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)


if __name__ == "__main__":
    n = int(input("Enter Any Singel Digit:"))
    print("Number:", n)

    start = time.time()
    result_iter = factorial_iter(n)
    end = time.time()
    print("\n Iterative Factorial:", result_iter)
    print("Time Taken (Iterative):", (end - start), "seconds")

    start = time.time()
    result_rec = factorial_rec(n)
    end = time.time()
    print("\n Recursive Factorial:", result_rec)
    print("Time Taken (Recursive):", (end - start), "seconds")
