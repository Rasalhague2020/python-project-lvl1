import random


DESCRIPTION = ('Answer "yes" if given number is prime. '
               'Otherwise answer "no".')
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def get_description():
    return DESCRIPTION


def get_prime_question_and_answer():
    question = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, (number // 2) + 1):
        if number % divisor == 0:
            return False
    return True
