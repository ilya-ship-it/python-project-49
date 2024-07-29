#!/usr/bin/env python3
from brain_games.engine import run_game
import brain_games.scripts.games.brain_calc as game


GAME_DESCRIPTION = 'What is the result of the expression?'


def main():
    run_game(game.main, GAME_DESCRIPTION)


if __name__ == '__main__':
    main()
