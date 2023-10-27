class LibraryBookDB:
    def __init__(self):
        self.books = []

    def add_book(self, book, quantity):
        self.books.append((book, quantity))

    def remove_book(self, book):
        for b, _ in self.books:
            if b == book:
                self.books.remove((b, _))
                break
