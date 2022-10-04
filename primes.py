"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Please enter a value greater than 0")
    list = []
    count = 0
    i = 2
    while (count < number_of_primes):
        add = True
        for j in range(2, i):
            if (i % j) == 0:
                add = False
                break;
        if add:
            list.append(i)
            count += 1

        i += 1
    return list
