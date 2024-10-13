class Book:
    """A class to represent a book in the library."""

    def __init__(self, title, author):
        """Initialize the book with a title, author, and set it as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book to the library."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class to manage a collection of books in a library."""

    def __init__(self):
        """Initialize the library with an empty book list."""
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title and book.check_out():
                print(f"You have checked out '{title}'.")
                return
        print(f"Sorry, '{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and book.return_book():
                print(f"You have returned '{title}'.")
                return
        print(f"Sorry, '{title}' was not checked out.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")



