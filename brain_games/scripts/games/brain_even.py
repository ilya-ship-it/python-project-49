import random
from brain_games.scripts.brain_games import main as ask_name
from brain_games.scripts.engine import ask_question


def get_correct_answer(question):
    game_result = question % 2 == 0
    return 'yes' if game_result else 'no'


def main():
    name = ask_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        question = random.randint(1, 100)
        correct_answer = get_correct_answer(question)
        if not ask_question(question, correct_answer, name):
            return
    print(f"Congratulations, {name}")
