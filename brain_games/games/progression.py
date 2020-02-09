import random


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100

MIN_STEP = 1
MAX_STEP = 10

NUM_QUANTITY = 10

HIDDEN_SYMBOL = '..'


def progression_game():
    sequence = []
    sequence.append(str(random.randint(MIN_RANDOM_NUMBER,
                                       MAX_RANDOM_NUMBER)))
    step = random.randint(MIN_STEP, MAX_STEP)

    for i in range(NUM_QUANTITY - 1):
        sequence.append(str(int(sequence[i]) + step))

    answer = random.choice(sequence)
    new_sequence = sequence[:sequence.index(answer)]
    new_sequence.append(HIDDEN_SYMBOL)
    new_sequence += sequence[sequence.index(answer) + 1:]

    return [' '.join(new_sequence), answer]


def progression_check(string, answer):
    if not answer.isdigit():
        return False
    string = string.replace(HIDDEN_SYMBOL, answer)
    sequence = string.split()

    step = int(sequence[1]) - int(sequence[0])

    for i in range(len(sequence) - 1):
        if int(sequence[i+1]) - int(sequence[i]) != step:
            return False
    return True
