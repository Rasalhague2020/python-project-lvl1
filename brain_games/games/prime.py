import random


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def prime_game():
    number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return [number, answer]


def prime_check(number, answer):
    if ((answer == 'yes') and is_prime(number)) or \
       ((answer != 'yes') and not is_prime(number)):
        return True
    return False


def is_prime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True
