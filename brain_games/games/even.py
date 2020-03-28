import random

import brain_games.main_loop


RULES = 'Answer "yes" if number even otherwise answer "no".\n'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_even(number):
    return not number % 2


def get_even_question_and_answer():
    question = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer


def start_even_game():
    brain_games.main_loop.game_engine(get_even_question_and_answer, RULES)
