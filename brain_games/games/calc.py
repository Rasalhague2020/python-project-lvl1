import random

from brain_games import engine


DESCRIPTION = 'What is the result of the expression?'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
OPERATORS = ['+', '-', '*']


def get_calc_question_and_answer():
    first_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    second_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    sign = random.choice(OPERATORS)

    answer = calculate(first_number, second_number, sign)
    question = f'{first_number} {sign} {second_number}'
    return question, str(answer)


def calculate(first_number, second_number, sign):
    if sign == '+':
        return first_number + second_number
    if sign == '-':
        return first_number - second_number
    if sign == '*':
        return first_number * second_number
    return None


def start_calc_game():
    engine.play(get_calc_question_and_answer, DESCRIPTION)
