import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!\n')
    return name


def welcome_even_rules():
    print('Welcome to Brain Games!\nAnswer "yes" if number ' +
          'even otherwise answer "no".\n')


def welcome_calc_rules():
    print('Welcome to Brain Games!\n' +
          'What is the result of the expression?\n')


def get_answer():
    return prompt.string('Your answer: ')
