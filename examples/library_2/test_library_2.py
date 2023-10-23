
from examples.library_2.book_2 import Book2
from examples.library_2.library_2 import Library2
from examples.library_2.random_data_gen import random_book

class TestLibrary2:
    def setup_method(self):
        self.library = Library2()

    def test_add_new_book_to_library(self):
        book: Book2 = random_book()
        self.library.add_new_book_to_library(book)
        assert book in self.library._available_books
