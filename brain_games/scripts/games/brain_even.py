import prompt
import random
from brain_games.scripts.brain_games import main as welcome_msg
from brain_games.scripts.engine import is_answer_correct
from brain_games.scripts.engine import incorrect_answer


def is_even(num):
    return num % 2 == 0


def main():
    name = welcome_msg()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        question = random.randint(1, 100)
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        correct_answer = is_answer_correct(is_even(question))
        if answer == correct_answer:
            print('Correct!')
            continue
        else:
            incorrect_answer(answer, correct_answer, name)
            return
    print(f"Congratulations, {name}")
