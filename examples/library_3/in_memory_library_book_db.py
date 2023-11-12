class InMemoryLibraryBookDB:
    """
    Books that are available in the library.
    Does not track borrowing actions - only the full inventory.
    """
    def __init__(self):
        self._books = {}

    def add_book(self, book_listing):
        if book_listing.uid in self._books:
            raise ValueError(f"Book with UID {book_listing.uid} already exists")
        self._books[book_listing.uid] = book_listing

    def find_books(self, author=None, title=None):
        with_author = self.filter_books_by_author(author, self._books.values())
        with_author_and_title = self.filter_books_by_title(title, with_author)

        return with_author_and_title

    def filter_books_by_author(self, author, orig_list):
        if author is None:
            return orig_list
        else:
            return [book for book in orig_list if book.book_info.author == author]
    
    def filter_books_by_title(self, title, orig_list):
        if title is None:
            return orig_list
        else:
            return [book for book in orig_list if book.book_info.title == title]
    
    def find_book_by_id(self, book_id):
        return self._books.get(book_id)
    
    def update_copies_count(self, book_id, copies_count):
        if copies_count < 0:
            raise ValueError("Copies count cannot be negative")
        if book_id not in self._books:
            raise ValueError(f"Book with UID {book_id} does not exist")
        if copies_count == 0:
            del self._books[book_id]
        else:
            self._books[book_id].existing_copies_count = copies_count


    def remove_book(self, book_id):
        self.update_copies_count(book_id, 0)
