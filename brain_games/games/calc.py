import random
import operator

from brain_games import engine


DESCRIPTION = 'What is the result of the expression?'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
OPERATORS = ['+', '-', '*']


def get_calc_question_and_answer():
    first_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    second_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    calc_operator = random.choice(OPERATORS)

    answer = get_answer(first_number, second_number, calc_operator)
    question = f'{first_number} {calc_operator} {second_number}'
    return question, str(answer)


def get_answer(first_number, second_number, calc_operator):
    if calc_operator == OPERATORS[0]:
        return operator.add(first_number, second_number)
    if calc_operator == OPERATORS[1]:
        return operator.sub(first_number, second_number)
    if calc_operator == OPERATORS[2]:
        return operator.mul(first_number, second_number)
    return None


def start_calc_game():
    engine.play(get_calc_question_and_answer, DESCRIPTION)
