import random


GAME_DESCRIPTION = 'What number is missing in the progression?'


def get_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    PROGRESSION_LENGTH = 10
    end = start + step * PROGRESSION_LENGTH
    progression = list(range(start, end, step))
    return progression


def get_question(progression, correct_answer):
    correct_answer_index = progression.index(correct_answer)
    progression[correct_answer_index] = '..'
    question = ' '.join(map(str, progression))
    return question


def main():
    progression = get_progression()
    correct_answer = random.choice(progression)
    question = get_question(progression, correct_answer)
    return question, correct_answer
