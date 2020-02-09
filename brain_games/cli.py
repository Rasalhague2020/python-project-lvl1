import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!\n')
    return name


def welcome_even_rules():
    print('Welcome to Brain Games!\n' +
          'Answer "yes" if number even otherwise answer "no".\n')


def welcome_calc_rules():
    print('Welcome to Brain Games!\n' +
          'What is the result of the expression?\n')


def welcome_gcd_rules():
    print('Welcome to Brain Games!\n' +
          'Find the greatest common division of given numbers.\n')


def welcome_progression_rules():
    print('Welcome to Brain Games!\n' +
          'What number is missing in the progression?\n')


def welcome_prime_rules():
    print('Welcome to Brain Games!\n' +
          'Answer "yes" if given number is prime. Otherwise answer "no".\n')


def get_answer():
    return prompt.string('Your answer: ')
