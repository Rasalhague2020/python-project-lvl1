import prompt


def game_engine(get_game_question_and_answer=None, description=''):
    attempts_count = 3

    print('Welcome to Brain Games!')
    print(f'{description}\n')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n')

    if not description:
        quit()

    while attempts_count:
        question, right_answer = get_game_question_and_answer()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')

        if user_answer == right_answer:
            print('Correct!\n')
            attempts_count -= 1
        else:
            print(f'\"{user_answer}\" is wrong answer ;(. '
                  f'Correct answer was \"{right_answer}\". '
                  f'Let\'s try again, {user_name}!\n')
    print(f'Congratulations, {user_name}!')
