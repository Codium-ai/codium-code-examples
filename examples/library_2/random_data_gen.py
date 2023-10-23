
from examples.library_2.book_2 import Book2
import random


def random_book() -> Book2:
    # https://datavizblog.com/2018/12/21/dataviz-humor-oreilly-programming-book-parody-covers/
    BOOK_TITLES = [
        "Blaming the user",
        "Vague understanding of computer science",
        "Writing code that nobody else can read",
        "Pointless meetings",
        "Coding drunk",
        "Buzzword-first design",
    ]

    AUTHORS = [
        "Bright-eyed junior",
        "Disillusioned senior",
        "A tired developer",
        "Dev with unrealistic deadlines",
    ]
    return Book2(
        title=random.choice(BOOK_TITLES),
        author=random.choice(AUTHORS),
        )
