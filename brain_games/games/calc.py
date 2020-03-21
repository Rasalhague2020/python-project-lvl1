import random
import brain_games.cli
import brain_games.main_loop


RULES = 'What is the result of the expression?\n'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
OPERATORS = ['+', '-', '*']


def get_calc_question_and_answer():
    first_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    second_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operator = random.choice(OPERATORS)
    answer = get_answer(first_number, second_number, operator)
    question = str(first_number) + ' ' + operator + ' ' + str(second_number)
    return [question, str(answer)]


def get_answer(first_number, second_number, operator):
    if operator == OPERATORS[0]:
        return first_number + second_number
    if operator == OPERATORS[1]:
        return first_number - second_number
    if operator == OPERATORS[2]:
        return first_number * second_number
    return None


def start_calc_game():
    attempts = 3
    brain_games.cli.opening_greetings_and_rules(RULES)
    user_name = brain_games.cli.get_user_name()
    brain_games.cli.user_greetings(user_name)
    while attempts:
        question, answer = get_calc_question_and_answer()
        attempts = brain_games.main_loop.game_engine(question, answer,
                                                     user_name, attempts)
