import random
from brain_games.cli import welcome_user
from brain_games.scripts.engine import ask_question


def get_question():
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    question = (f"{x} {operation} {y}")
    return question


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        question = get_question()
        correct_answer = eval(question)
        if not ask_question(question, correct_answer, name):
            return
    print(f"Congratulations, {name}!")
