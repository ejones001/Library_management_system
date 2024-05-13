class Book:
    def __init__(self, title, author, isbn, genre, publication_date, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.availability = availability
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nGenre: {self.genre}\nPublication Date: {self.publication_date}\nAvailability: {'Available' if self.availability else 'Not Available'}"
