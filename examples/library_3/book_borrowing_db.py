class BookBorrowingDB:
    def __init__(self):
        self.borrowed_books = []

    def borrow_book(self, book, user):
        self.borrowed_books.append((book, user))

    def return_book(self, book, user):
        for b, u in self.borrowed_books:
            if b == book and u == user:
                self.borrowed_books.remove((b, u))
                break

