import random
from operator import add
from operator import sub
from operator import mul

import brain_games.main_loop


DESCRIPTION = 'What is the result of the expression?'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
OPERATORS = ['+', '-', '*']


def get_calc_question_and_answer():
    first_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    second_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operator = random.choice(OPERATORS)

    answer = get_answer(first_number, second_number, operator)
    question = f'{first_number} {operator} {second_number}'
    return question, str(answer)


def get_answer(first_number, second_number, operator):
    if operator == OPERATORS[0]:
        return add(first_number, second_number)
    if operator == OPERATORS[1]:
        return sub(first_number, second_number)
    if operator == OPERATORS[2]:
        return mul(first_number, second_number)
    return None


def start_calc_game():
    brain_games.main_loop.game_engine(get_calc_question_and_answer,
                                      DESCRIPTION)
