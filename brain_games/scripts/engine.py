def is_answer_correct(game_result):
    return 'yes' if game_result else 'no'


def incorrect_answer(answer, correct_answer, name):
    print(
        f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.\n"
        f"Let's try again, {name}"
    )
