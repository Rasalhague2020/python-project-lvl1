#!/usr/bin/env python

from brain_games.games import gcd

from brain_games import engine


def main():
    engine.play(gcd.get_gcd_question_and_answer, gcd.get_description)


if __name__ == '__main__':
    main()
