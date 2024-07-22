import prompt
import random
from brain_games.scripts.brain_games import main as welcome_msg

def main():
    name = welcome_msg()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        question = random.randint(1, 100)
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if question % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                continue
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}")
                return
        else:
            if answer == 'no':
                print('Correct!')
                continue
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}")
                return
    print(f"Congratulations, {name}")
