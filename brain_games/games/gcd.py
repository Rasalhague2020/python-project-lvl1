import random
import brain_games.cli
import brain_games.main_loop


RULES = 'Find the greatest common division of given numbers.\n'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def get_gcd_question_and_answer():
    num1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    num2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = str(num1) + ' ' + str(num2)
    answer = str(get_gcd(max(num1, num2), min(num1, num2)))
    return [question, answer]


def get_gcd(a, b):
    if a % b == 0:
        return b
    return get_gcd(b, a % b)


def start_gcd_game():
    attempts = 3
    user_name = brain_games.cli.welcome_user(RULES)
    while attempts:
        question, answer = get_gcd_question_and_answer()
        attempts = brain_games.main_loop.game_engine(question, answer,
                                                     user_name, attempts)
