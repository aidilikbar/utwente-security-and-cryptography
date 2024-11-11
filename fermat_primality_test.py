import random

# Function to perform modular exponentiation using the square-and-multiply algorithm
def modular_exponentiation(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if (exponent % 2) == 1:  # If exponent is odd
            result = (result * base) % mod
        exponent = exponent >> 1  # Divide exponent by 2
        base = (base * base) % mod  # Square the base
    return result

# Fermat's primality test
def fermat_primality_test(n, k):
    # Perform the test k times to reduce the probability of error
    for _ in range(k):
        # Choose a random integer a such that 1 <= a <= n-1
        a = random.randint(2, n - 2)
        # Compute a^(n-1) mod n
        if modular_exponentiation(a, n - 1, n) != 1:
            return False  # n is definitely composite
    return True  # n is probably prime

# Test the number m = 41041 with 10 witnesses
m = 41041
k = 10  # Number of times to run the test
is_probably_prime = fermat_primality_test(m, k)

print(f"Is {m} probably prime? {is_probably_prime}")