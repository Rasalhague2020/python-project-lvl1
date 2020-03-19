#!/usr/bin/env python3

# import brain_games.cli
# import brain_games.main_loop

import brain_games.games.even


def main():
    brain_games.games.even.start_even_game()

    # brain_games.cli.welcome_even_rules()
    # user_name = brain_games.cli.welcome_user()
    # brain_games.main_loop.main_loop('even', user_name)


if __name__ == '__main__':
    main()
