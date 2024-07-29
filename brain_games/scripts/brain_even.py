#!/usr/bin/env python3
from brain_games.engine import run_game
import brain_games.scripts.games.brain_even as game


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(game.main, GAME_DESCRIPTION)


if __name__ == '__main__':
    main()
