import random


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def get_qa_gcd_game():
    num1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    num2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = str(num1) + ' ' + str(num2)
    answer = str(get_gcd(max(num1, num2), min(num1, num2)))
    return [question, answer]


def is_gcd_answer_right(numbers, answer):
    if answer.isdigit():
        num_list = numbers.split()
        return get_gcd(max(int(num_list[0]), int(num_list[1])),
                       min(int(num_list[0]), int(num_list[1]))) == int(answer)
    return False


def get_gcd(a, b):
    if a % b == 0:
        return b
    return get_gcd(b, a % b)
