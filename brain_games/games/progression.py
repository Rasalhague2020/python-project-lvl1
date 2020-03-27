import random
import brain_games.cli
import brain_games.main_loop


RULES = 'What number is missing in the progression?\n'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100

MIN_STEP = 1
MAX_STEP = 10

NUM_QUANTITY = 10

HIDDEN_SYMBOL = '..'


def get_progression_question_and_answer():
    sequence = []
    start = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)

    for i in range(NUM_QUANTITY - 1):
        sequence.append(str(start + step*i))

    answer = random.choice(sequence)
    new_sequence = sequence[:sequence.index(answer)]
    new_sequence.append(HIDDEN_SYMBOL)
    new_sequence += sequence[sequence.index(answer) + 1:]

    return ' '.join(new_sequence), answer


def start_progression_game():
    attempts = 3
    brain_games.cli.opening_greetings_and_rules(RULES)
    user_name = brain_games.cli.get_user_name()
    brain_games.cli.user_greetings(user_name)
    while attempts:
        question, answer = get_progression_question_and_answer()
        attempts = brain_games.main_loop.game_engine(question, answer,
                                                     user_name, attempts)
