import prompt
import random
from brain_games.scripts.brain_games import main as welcome_msg
from brain_games.scripts.engine import incorrect_answer


def get_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    progression_length = 10
    end = start + step * progression_length
    progression = list(range(start, end, step))
    return progression


def get_question(progression, correct_answer):
    correct_answer_index = progression.index(correct_answer)
    progression[correct_answer_index] = '..'
    question = ' '.join(map(str, progression))
    return question


def main():
    name = welcome_msg()
    print('What number is missing in the progression?')
    for _ in range(3):
        progression = get_progression()
        correct_answer = random.choice(progression)
        question = get_question(progression, correct_answer)
        print(f"Question: {str(question)}")
        answer = prompt.string('Your answer: ')
        correct_answer = str(correct_answer)
        if answer == correct_answer:
            print('Correct!')
            continue
        else:
            incorrect_answer(answer, correct_answer, name)
            return
    print(f"Congratulations, {name}")
