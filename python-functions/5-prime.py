def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            # if numbers up to half of itself can divide it it is not a prime
            return False
    return True
