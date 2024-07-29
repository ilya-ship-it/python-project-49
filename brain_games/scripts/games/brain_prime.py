import random


GAME_DESCRIPTION = (
    'Answer "yes" if given number is prime. '
    'Otherwise answer "no".'
)


def get_correct_answer(question):
    if question == 1:
        return 'no'
    if not (question % 2 == 0 or question % 3 == 0) or (question == 2):
        return 'yes'
    else:
        return 'no'


def main():
    question = random.randint(1, 100)
    correct_answer = get_correct_answer(question)
    return question, correct_answer
