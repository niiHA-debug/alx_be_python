# library_management.py

class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
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
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out


class Library:
    """Represents a collection of books and library operations."""

    def __init__(self):
        self._books = []  # Private list of Book instances

    def add_book(self, book):
        """Add a book to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Only Book instances can be added.")

    def check_out_book(self, title):
        """Check out a book by title if it’s available."""
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                print(f"'{book.title}' has been checked out.")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                book.return_book()
                print(f"'{book.title}' has been returned.")
                return
        print(f"Book '{title}' was not checked out or not found.")

    def list_available_books(self):
        """Print a list of available books."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
