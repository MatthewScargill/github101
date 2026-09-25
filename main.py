"""this file  is entry to this python project"""


"""print("this file is currently running")"""

import math

def is_prime(num: int) -> bool:
    """
    Checks if a given positive integer is a prime number.

    Optimization: Only needs to check for divisors up to the square root of the number.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True

    # Check if divisible by 2 or 3 (quick check for common non-primes)
    if num % 2 == 0 or num % 3 == 0:
        return False

    # Optimized check: Primes greater than 3 are of the form 6k +/- 1.
    # We only need to check divisors of this form up to sqrt(num).
    i = 5
    limit = int(math.sqrt(num))
    while i <= limit:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

def calculate_first_n_primes(n: int) -> list[int]:
    """
    Calculates and returns a list containing the first 'n' prime numbers.

    Args:
        n: The number of prime numbers to find (must be a positive integer).

    Returns:
        A list of integers representing the first n primes.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input 'n' must be a positive integer.")

    if n == 1:
        return [2]

    primes = []
    num = 2  # Start checking from the first prime number

    # Loop until we have found 'n' primes
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)

        # Always check the next consecutive integer
        num += 1

    return primes

num = calculate_first_n_primes(2000)
print(num)
