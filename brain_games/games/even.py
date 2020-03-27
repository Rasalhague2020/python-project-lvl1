import random

import brain_games.cli
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
    attempts = 3
    brain_games.cli.opening_greetings_and_rules(RULES)
    user_name = brain_games.cli.get_user_name()
    brain_games.cli.user_greetings(user_name)
    while attempts:
        question, answer = get_even_question_and_answer()
        attempts = brain_games.main_loop.game_engine(question, answer,
                                                     user_name, attempts)
