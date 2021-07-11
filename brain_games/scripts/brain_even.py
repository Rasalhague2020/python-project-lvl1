#!/usr/bin/env python

from brain_games.games import even

from brain_games import engine


def main():
    engine.play(even.get_even_question_and_answer, even.DESCRIPTION)


if __name__ == '__main__':
    main()
