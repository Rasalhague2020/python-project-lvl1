import prompt


ATTEMPTS_COUNT = 3


def play(get_game_question_and_answer, description):
    print('Welcome to Brain Games!')
    print(f'{description}\n')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n')

    for _ in range(ATTEMPTS_COUNT):
        question, right_answer = get_game_question_and_answer()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')

        if user_answer != right_answer:
            print(f'\"{user_answer}\" is wrong answer ;(. '
                  f'Correct answer was \"{right_answer}\". '
                  f'Let\'s try again, {user_name}!\n')
            return
        print('Correct!\n')

    print(f'Congratulations, {user_name}!')
