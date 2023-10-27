class BookListing(BookInfo):
    def __init__(self, title, author, publication_date, available_count):
        super().__init__(title, author, publication_date)
        self.available_count = available_count
