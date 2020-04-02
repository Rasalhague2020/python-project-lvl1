import prompt


def play(get_game_question_and_answer, description):
    attempts_count = 3

    print('Welcome to Brain Games!')
    print(f'{description}\n')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n')

    while attempts_count:
        question, right_answer = get_game_question_and_answer()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')

        if user_answer != right_answer:
            print(f'\"{user_answer}\" is wrong answer ;(. '
                  f'Correct answer was \"{right_answer}\". '
                  f'Let\'s try again, {user_name}!\n')
            continue
        print('Correct!\n')
        attempts_count -= 1

    print(f'Congratulations, {user_name}!')
