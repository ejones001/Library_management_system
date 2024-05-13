from book import Book
from user import User
from author import Author
from genre import Genre
from library import Library

if __name__ == "__main__":
    library = Library()

    book1 = Book("Python Programming", "John Smith", "1234567890", "Programming", "2022-01-01")
    book2 = Book("Data Science Essentials", "Emily Brown", "0987654321", "Data Science", "2021-12-01")
    library.add_book(book1)
    library.add_book(book2)

    user1 = User("Alice", "A123")
    user2 = User("Bob", "B456")
    library.add_user(user1)
    library.add_user(user2)

    author1 = Author("John Smith", "Bestselling author with expertise in Python programming.")
    author2 = Author("Emily Brown", "Data scientist and educator.")
    library.add_author(author1)
    library.add_author(author2)

    genre1 = Genre("Programming", "Books related to programming languages and software development.", "Non-fiction")
    genre2 = Genre("Data Science", "Books on data analysis, machine learning, and statistics.", "Non-fiction")
    library.add_genre(genre1)
    library.add_genre(genre2)

    print("Books:")
    library.display_books()

    print("\nUsers:")
    library.display_users()

    print("\nAuthors:")
    library.display_authors()

    print("\nGenres:")
    library.display_genres()
