import prompt
import random
from brain_games.scripts.brain_games import main as welcome_msg
from brain_games.scripts.engine import incorrect_answer


def get_question():
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    question = (f"{x} {operation} {y}")
    return question


def main():
    name = welcome_msg()
    print('What is the result of the expression?')
    for _ in range(3):
        question = get_question()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        correct_answer = str(eval(question))
        if answer == correct_answer:
            print('Correct!')
            continue
        else:
            incorrect_answer(answer, correct_answer, name)
            return
