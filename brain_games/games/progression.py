import random


DESCRIPTION = 'What number is missing in the progression?'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100

MIN_STEP = 1
MAX_STEP = 10

NUM_QUANTITY = 10


def get_description():
    return DESCRIPTION


def get_progression_question_and_answer():
    question = []
    start = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)

    for nth_term in range(NUM_QUANTITY):
        question.append(str(start + step * nth_term))

    answer_index = random.randint(0, NUM_QUANTITY - 1)
    answer = question[answer_index]
    question[answer_index] = '..'
    question = ' '.join(question)
    return question, answer
