import random

from brain_games import engine


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

    for nth_term in range(NUM_QUANTITY - 1):
        sequence.append(str(start + step * nth_term))

    answer = random.choice(sequence)
    question = sequence[:sequence.index(answer)]
    question.append('..')
    question += sequence[sequence.index(answer) + 1:]
    question = ' '.join(question)
    return question, answer


def start_progression_game():
    engine.play(get_progression_question_and_answer, DESCRIPTION)
