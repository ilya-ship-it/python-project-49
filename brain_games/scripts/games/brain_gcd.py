import prompt
import random
from brain_games.scripts.brain_games import main as welcome_msg
from brain_games.scripts.engine import incorrect_answer
from math import gcd


def main():
    name = welcome_msg()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        question = (x, y)
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        correct_answer = str(gcd(x, y))
        if answer == correct_answer:
            print('Correct!')
            continue
        else:
            incorrect_answer(answer, correct_answer, name)
            return
