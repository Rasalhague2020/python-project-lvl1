import random

import brain_games.cli
import brain_games.main_loop


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def get_prime_question_and_answer():
    question = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def is_prime(number):
    if number > 1:
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                break
        else:
            return True
    return False


def start_prime_game():
    attempts = 3
    brain_games.cli.opening_greetings_and_rules(RULES)
    user_name = brain_games.cli.get_user_name()
    brain_games.cli.user_greetings(user_name)
    while attempts:
        question, answer = get_prime_question_and_answer()
        attempts = brain_games.main_loop.game_engine(question, answer,
                                                     user_name, attempts)
