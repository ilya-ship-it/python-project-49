import random


GAME_DESCRIPTION = (
    'Answer "yes" if given number is prime. '
    'Otherwise answer "no".'
)


def get_correct_answer(question):
    if question == 1:
        return 'no'
    for i in range(2, int(question ** 0.5) + 1):
        if question % i == 0:
            return 'no'
    return 'yes'


def main():
    question = random.randint(1, 100)
    correct_answer = get_correct_answer(question)
    return question, correct_answer
