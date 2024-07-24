import random
from brain_games.scripts.brain_games import main as ask_name
from brain_games.scripts.engine import ask_question
from math import gcd


def main():
    name = ask_name()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        question = (x, y)
        correct_answer = gcd(x, y)
        if not ask_question(question, correct_answer, name):
            return
    print(f"Congratulations, {name}")
