import brain_games.games.even
import brain_games.games.calc
import brain_games.games.gcd


def get_qa(game_name):
    if game_name == 'even':
        return brain_games.games.even.even_game()
    if game_name == 'calc':
        return brain_games.games.calc.calc_game()
    if game_name == 'gcd':
        return brain_games.games.gcd.gcd_game()


def check_answer(game_name, question, answer):
    if game_name == 'even':
        return brain_games.games.even.even_check(question, answer)
    if game_name == 'calc':
        return brain_games.games.calc.calc_check(question, answer)
    if game_name == 'gcd':
        return brain_games.games.gcd.gcd_check(question, answer)


def main_loop(game_name, user_name):
    number_of_attempts = 3
    while number_of_attempts:
        qa = get_qa(game_name)
        print('Question:', qa[0])

        answer = brain_games.cli.get_answer()

        if check_answer(game_name, qa[0], answer):
            print('Correct!\n')
            number_of_attempts -= 1
        else:
            print("\"" + answer + "\" is wrong answer ;(. " +
                  "Correct answer was \"" + qa[1] + "\". " +
                  "Let's try again, " + user_name + "!\n")

    print('Congratulations, ' + user_name + '!')
