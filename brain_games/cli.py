import prompt


def welcome_even_rules():
    print('Welcome to Brain Games!\nAnswer "yes" if number ' +
          'even otherwise answer "no".\n')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!\n')
    return name


def get_answer():
    return prompt.string('Your answer: ')
