import brain_games.cli
import brain_games.even


def main():
    brain_games.cli.welcome_even_rules()
    user_name = brain_games.cli.welcome_user()
    brain_games.even.even_game(user_name)


if __name__ == '__main__':
    main()
