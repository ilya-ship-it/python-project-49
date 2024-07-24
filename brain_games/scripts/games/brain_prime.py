import random
from brain_games.cli import welcome_user
from brain_games.scripts.engine import ask_question


def get_correct_answer(question):
    if question == 1:
        return 'no'
    if not (question % 2 == 0 or question % 3 == 0) or (question == 2):
        return 'yes'
    else:
        return 'no'


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        question = random.randint(1, 100)
        correct_answer = get_correct_answer(question)
        if not ask_question(question, correct_answer, name):
            return
    print(f"Congratulations, {name}")
