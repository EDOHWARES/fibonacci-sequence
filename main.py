def fibonacci():
    """
    A fibonacci function
    :return: a sequence of fibonacci terms to the inputted range
    """

    global fibon
    n = 0
    while n < 2:
        fibon = []
        try:
            n = int(input("Range of values of the fibonacci sequence: "))
        except ValueError:
            print("Input must be a Digit!")

        if n < 2:
            print("Digit must be greater than 2...")

        a = 0
        b = 1

        while len(fibon) < n:
            fibon.append(a)
            a, b = b, b + a

    return f"Fibonacci Sequence: {fibon}"


print(fibonacci())
