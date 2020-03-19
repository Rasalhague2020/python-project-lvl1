#!/usr/bin/env python3

# import brain_games.cli
# import brain_games.main_loop

import brain_games.games.progression


def main():
    brain_games.games.progression.start_progression_game()

    # brain_games.cli.welcome_progression_rules()
    # user_name = brain_games.cli.welcome_user()
    # brain_games.main_loop.main_loop('progression', user_name)


if __name__ == '__main__':
    main()
