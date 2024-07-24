import prompt


def incorrect_answer(answer, correct_answer, name):
    print(
        f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.\n"
        f"Let's try again, {name}!"
    )


def ask_question(question, correct_answer, name):
    print(f"Question: {question}")
    answer = prompt.string('Your answer: ')
    correct_answer = str(correct_answer)
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        incorrect_answer(answer, correct_answer, name)
        return False
