import random

import brain_games.main_loop


DESCRIPTION = 'What number is missing in the progression?'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100

MIN_STEP = 1
MAX_STEP = 10

NUM_QUANTITY = 10


def get_progression_question_and_answer():
    sequence = []
    start = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)

    for i in range(NUM_QUANTITY - 1):
        sequence.append(str(start + step*i))

    answer = random.choice(sequence)
    question = sequence[:sequence.index(answer)]
    question.append('..')
    question += sequence[sequence.index(answer) + 1:]
    question = ' '.join(question)
    return question, answer


def start_progression_game():
    brain_games.main_loop.game_engine(get_progression_question_and_answer,
                                      DESCRIPTION)
