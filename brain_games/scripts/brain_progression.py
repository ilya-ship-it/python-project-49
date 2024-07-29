#!/usr/bin/env python3
from brain_games.engine import run_game
import brain_games.scripts.games.brain_progression as game


GAME_DESCRIPTION = 'What number is missing in the progression?'

def main():
    run_game(game.main, GAME_DESCRIPTION)


if __name__ == '__main__':
    main()