import prompt


def welcome_user(rules=''):
    print('Welcome to Brain Games!')
    if rules:
        print(rules)
    name = prompt.string('\nMay I have your name? ')
    print('Hello, ' + name + '!\n')
    return name


def get_answer_on_question(question):
    print('Question:', question)
    return prompt.string('Your answer: ')


def correct_message():
    print('Correct!\n')


def wrong_message(user_answer, right_answer, user_name):
    print('\"' + user_answer + '\" is wrong answer ;(. ' +
          'Correct answer was \"' + right_answer + '\". ' +
          'Let\'s try again, ' + user_name + '!\n')


def congrats_message(user_name):
    print('Congratulations, ' + user_name + '!')
