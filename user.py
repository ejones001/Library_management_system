class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.availability:
            self.borrowed_books.append(book)
            book.availability = False
            print(f"{self.name} has borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.availability = True
            print(f"{self.name} has returned {book.title}")
        else:
            print(f"You have not borrowed {book.title}")
