import random
from math import gcd


def main():
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        question = f"{x} {y}"
        correct_answer = gcd(x, y)
        return question, correct_answer
