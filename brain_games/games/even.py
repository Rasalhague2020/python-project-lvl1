import random


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_even(number):
    return not number % 2


def get_qa_even_game():
    question = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return [question, answer]


def is_even_answer_right(question, answer):
    if ((answer == 'yes') and is_even(question)) or \
       ((answer != 'yes') and not is_even(question)):
        return True
    return False
