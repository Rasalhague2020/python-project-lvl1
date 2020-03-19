import brain_games.cli


def game_engine(question, right_answer, user_name, attempts):
    user_answer = brain_games.cli.get_answer_on_question(question)
    if user_answer == right_answer:
        brain_games.cli.correct_message()
        attempts -= 1
    else:
        brain_games.cli.wrong_message(user_answer, right_answer, user_name)
    if attempts == 0:
        brain_games.cli.congrats_message(user_name)
    return attempts
