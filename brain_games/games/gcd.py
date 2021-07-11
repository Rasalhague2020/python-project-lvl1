import random

from brain_games import engine


DESCRIPTION = 'Find the greatest common division of given numbers.'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def get_description():
    return DESCRIPTION


def get_gcd_question_and_answer():
    num1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    num2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)

    question = f'{num1} {num2}'
    answer = str(get_gcd(num1, num2))
    return question, answer


def get_gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    return get_gcd(b, a % b)
