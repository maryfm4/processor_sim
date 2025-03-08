import random


def page_generator(number, max):
    # number - ilość stron
    # max- maksymalny numer strony

    pages = []

    for item in range(0, number):
        pages.append(random.randint(0, 3))

    return pages


pages_anomaly = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
