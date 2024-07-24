import random
from brain_games.cli import welcome_user
from brain_games.scripts.engine import ask_question


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
    name = welcome_user()
    print('What number is missing in the progression?')
    for _ in range(3):
        progression = get_progression()
        correct_answer = random.choice(progression)
        question = get_question(progression, correct_answer)
        if not ask_question(question, correct_answer, name):
            return
    print(f"Congratulations, {name}")
