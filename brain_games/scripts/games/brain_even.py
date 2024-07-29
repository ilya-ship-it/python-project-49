import random


def get_correct_answer(question):
    game_result = question % 2 == 0
    return 'yes' if game_result else 'no'


def main():
    question = random.randint(1, 100)
    correct_answer = get_correct_answer(question)
    return question, correct_answer
