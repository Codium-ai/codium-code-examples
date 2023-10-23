from __future__ import annotations

from typing import List, Optional

from examples.library_2.book_2 import Book2


class Library2:
    def __init__(self) -> None:
        self._available_books: List[Book2] = []
        self._borrowed_books: List[Book2] = []

    def add_new_book_to_library(self, book: Book2) -> None:
        self._available_books.append(book)
    
    def remove_book(self, book: Book2) -> None:
        if book in self._available_books:
            self._available_books.remove(book)
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)

    def borrow_book(self, book: Book2) -> None:
        if book not in self._available_books:
            raise ValueError(f"Book {book} is not available for borrowing")
        self._available_books.remove(book)
        self._borrowed_books.append(book)
    
    def return_borrowed_book(self, book: Book2) -> None:
        if book not in self._borrowed_books:
            if not book in self._available_books:
                self._available_books.append(book)
            raise ValueError(f"Book {book} is not in borrowed books list")
        self._borrowed_books.remove(book)
        self._available_books.append(book)

    def find_available_book_by_title(self, title: int) -> Optional[Book2]:
        for book in self._available_books:
            if book.title == title:
                return book
        return None
    
    def find_available_book_by_author(self, author: int) -> Optional[Book2]:
        for book in self._available_books:
            if book.author == author:
                return book
        return None
