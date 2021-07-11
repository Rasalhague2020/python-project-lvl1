#!/usr/bin/env python

from brain_games.games import prime

from brain_games import engine


def main():
    engine.play(prime.get_prime_question_and_answer, prime.get_description)


if __name__ == '__main__':
    main()
