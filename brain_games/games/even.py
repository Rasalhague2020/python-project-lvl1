import random


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_even(number):
    return not number % 2


def even_game():
    number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'
    return [number, answer]


def even_check(number, answer):
    if ((answer == 'yes') and is_even(number)) or \
       ((answer != 'yes') and not is_even(number)):
        return True
    return False

# def even_game(user_name):
#     number_of_attempts = 3
#     while number_of_attempts:
#         number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
#         print('Question:', number)
#         answer = brain_games.cli.get_answer()

#         if ((answer == 'yes') and is_even(number)) or \
#            ((answer != 'yes') and not is_even(number)):
#             print('Correct!\n')
#             number_of_attempts -= 1
#         elif answer == 'yes':
#             print("\"yes\" is wrong answer ;(. Correct answer was " +
#                   "\"no\". Let's try again, " + user_name + '!\n')
#         else:
#             print("\"no\" is wrong answer ;(. Correct answer was " +
#                   "\"yes\". Let's try again, " + user_name + '!\n')

#     print('Congratulations, ' + user_name + '!')
