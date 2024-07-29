import random


def get_question():
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    question = (f"{x} {operation} {y}")
    return question


def main():
    question = get_question()
    correct_answer = eval(question)
    return question, correct_answer
