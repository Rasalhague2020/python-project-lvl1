import prompt


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    return user_name
