#!/usr/bin/env python

from brain_games.games import calc

from brain_games import engine


def main():
    engine.play(calc.get_calc_question_and_answer, calc.DESCRIPTION)


if __name__ == '__main__':
    main()
