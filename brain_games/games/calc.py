import random


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
OPERATORS = ['+', '-', '*']


def get_qa_calc_game():
    expression = (str(random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER))
                  + ' '
                  + random.choice(OPERATORS)
                  + ' '
                  + str(random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)))
    answer = get_answer(expression)
    return [expression, answer]


def get_answer(expression):
    sequence = expression.split()
    if sequence[1] == OPERATORS[0]:
        return str(int(sequence[0]) + int(sequence[2]))
    if sequence[1] == OPERATORS[1]:
        return str(int(sequence[0]) - int(sequence[2]))
    if sequence[1] == OPERATORS[2]:
        return str(int(sequence[0]) * int(sequence[2]))
    return 'error'


def is_calc_answer_right(expression, answer):
    if get_answer(expression) == answer:
        return True
    return False
