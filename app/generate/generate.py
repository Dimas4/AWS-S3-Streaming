import random


def generate():
    index = 0
    while index < 10000:
        number = random.randint(9879879875846897, 4968498798458498494) ** 15
        index += 1
        yield str(number) + '\n'

