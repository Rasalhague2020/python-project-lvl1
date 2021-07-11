#!/usr/bin/env python

from brain_games.games import progression

from brain_games import engine


def main():
    engine.play(progression.get_progression_question_and_answer,
                progression.DESCRIPTION)


if __name__ == '__main__':
    main()
