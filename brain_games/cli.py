import prompt
from brain_games.scripts.brain_games import main as welcome_msg


def welcome_user():
    welcome_msg()
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    return name


if __name__ == '__main__':
    welcome_user()
