import brain_games.games.even
import brain_games.games.calc
import brain_games.games.gcd
import brain_games.games.progression
import brain_games.games.prime


def get_qa(game_name):
    if game_name == 'even':
        return brain_games.games.even.get_qa_even_game()
    if game_name == 'calc':
        return brain_games.games.calc.get_qa_calc_game()
    if game_name == 'gcd':
        return brain_games.games.gcd.get_qa_gcd_game()
    if game_name == 'progression':
        return brain_games.games.progression.get_qa_progression_game()
    if game_name == 'prime':
        return brain_games.games.prime.get_qa_prime_game()


def check_answer(game_name, question, answer):
    if game_name == 'even':
        return brain_games.games.even.\
               is_even_answer_right(question, answer)
    if game_name == 'calc':
        return brain_games.games.calc.\
               is_calc_answer_right(question, answer)
    if game_name == 'gcd':
        return brain_games.games.gcd.\
               is_gcd_answer_right(question, answer)
    if game_name == 'progression':
        return brain_games.games.progression.\
               is_progression_answer_right(question, answer)
    if game_name == 'prime':
        return brain_games.games.prime.\
               is_prime_answer_right(question, answer)


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
