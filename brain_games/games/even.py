import random


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_even(number):
    return not number % 2


def get_qa_even_game():
    number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'
    return [number, answer]


def is_even_answer_right(number, answer):
    if ((answer == 'yes') and is_even(number)) or \
       ((answer != 'yes') and not is_even(number)):
        return True
    return False
