import prompt
from brain_games.cli import welcome_user


def ask_question(question, correct_answer, name):
    print(f"Question: {question}")
    answer = prompt.string('Your answer: ')
    correct_answer = str(correct_answer)
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(
            f"{answer} is wrong answer ;(. "
            f"Correct answer was {correct_answer}.\n"
            f"Let's try again, {name}!"
        )
        return False


def run_game(game, GAME_DESCRIPTION):
    name = welcome_user()
    print(GAME_DESCRIPTION)
    ROUNDS_AMOUNT = 3
    for _ in range(ROUNDS_AMOUNT):
        question, correct_answer = game()
        if not ask_question(question, correct_answer, name):
            return
    print(f'Congratulations, {name}!')
