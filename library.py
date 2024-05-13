class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
        else:
            print("This book already exists in the library.")

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
        else:
            print("This user already exists in the library.")

    def add_author(self, author):
        if author not in self.authors:
            self.authors.append(author)
        else:
            print("This author already exists in the library.")

    def add_genre(self, genre):
        if genre not in self.genres:
            self.genres.append(genre)
        else:
            print("This genre already exists in the library.")

    def display_books(self):
        for book in self.books:
            print(book)

    def display_users(self):
        for user in self.users:
            print(f"Name: {user.name}, Library ID: {user.library_id}")

    def display_authors(self):
        for author in self.authors:
            print(f"Name: {author.name}, Biography: {author.biography}")

    def display_genres(self):
        for genre in self.genres:
            print(f"Name: {genre.name}, Description: {genre.description}, Category: {genre.category}")
