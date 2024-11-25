from datetime import datetime  # Import for managing dates (borrow and return dates)
import pickle  # Import for saving and loading data to/from files

# Book Class: Represents each book in the library
class Book:
    def __init__(self, title, author, isbn, is_available=True):
        """
        Initializes a new Book instance.
        :param title: Title of the book
        :param author: Author of the book
        :param isbn: ISBN of the book (unique identifier)
        :param is_available: Availability status of the book (default: True)
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __repr__(self):
        """
        Returns a detailed string representation of the Book instance.
        This is useful for debugging and displaying the book in an unambiguous format.
        """
        return f"Book({self.title}, {self.author}, {self.isbn}, {'Available' if self.is_available else 'Borrowed'})"


# Borrower Class: Represents each borrower and the book they've borrowed
class Borrower:
    def __init__(self, borrower_id, book_borrowed, borrow_date, return_date=None):
        """
        Initializes a new Borrower instance.
        :param borrower_id: Unique ID of the borrower
        :param book_borrowed: ISBN of the book borrowed by the borrower
        :param borrow_date: Date the book was borrowed
        :param return_date: Date the book was returned (default: None)
        """
        self.borrower_id = borrower_id
        self.book_borrowed = book_borrowed
        self.borrow_date = borrow_date
        self.return_date = return_date

    def __repr__(self):
        """
        Returns a detailed string representation of the Borrower instance.
        Useful for debugging and tracking borrower records.
        """
        return f"Borrower(ID: {self.borrower_id}, Book: {self.book_borrowed}, Borrow Date: {self.borrow_date}, Return Date: {self.return_date})"


# LibraryManager Class: Manages the overall library operations
class LibraryManager:
    def __init__(self):
        """
        Initializes the LibraryManager with empty lists for books and borrowers.
        """
        self.books = []  # List to store all Book objects
        self.borrowers = []  # List to store all Borrower records

    # Add a new book to the library
    def add_book(self, title, author, isbn):
        """
        Adds a new book to the library.
        :param title: Title of the book
        :param author: Author of the book
        :param isbn: ISBN of the book
        """
        if self.validate_isbn(isbn):  # Validate the ISBN format
            self.books.append(Book(title, author, isbn))  # Create and add a Book instance to the list
            print(f"Book '{title}' added successfully.")  # Confirmation message
        else:
            print("Invalid ISBN. Book not added.")  # Error message for invalid ISBN

    # Remove a book from the library using its ISBN
    def remove_book(self, isbn):
        """
        Removes a book from the library based on its ISBN.
        :param isbn: ISBN of the book to remove
        """
        self.books = [book for book in self.books if book.isbn != isbn]  # Filter out the book with the given ISBN
        print(f"Book with ISBN {isbn} removed successfully.")  # Confirmation message

    # Search for books based on title, author, or ISBN
    def search_books(self, query, by="title"):
        """
        Searches for books based on a query and a field (title, author, or ISBN).
        :param query: Search keyword
        :param by: Field to search by (default: title)
        :return: List of matching Book objects
        """
        results = [book for book in self.books if query.lower() in getattr(book, by).lower()]  # Filter books by query
        return results

    # Sort books by a specific field (title or author)
    def sort_books(self, by="title"):
        """
        Sorts books by a specified attribute (title or author).
        :param by: Field to sort by (default: title)
        :return: Sorted list of Book objects
        """
        return sorted(self.books, key=lambda book: getattr(book, by).lower())  # Sort using the field as the key

    # Borrow a book from the library
    def borrow_book(self, borrower_id, isbn):
        """
        Allows a borrower to borrow a book if it's available.
        :param borrower_id: Unique ID of the borrower
        :param isbn: ISBN of the book to borrow
        """
        # Find the book by ISBN and check if it's available
        book = next((b for b in self.books if b.isbn == isbn and b.is_available), None)
        if book:
            book.is_available = False  # Mark the book as borrowed
            self.borrowers.append(Borrower(borrower_id, isbn, datetime.now()))  # Add a new Borrower record
            print(f"Book '{book.title}' borrowed by Borrower ID {borrower_id}.")  # Confirmation message
        else:
            print("Book not available or invalid ISBN.")  # Error message if the book isn't available

    # Return a borrowed book
    def return_book(self, borrower_id, isbn):
        """
        Allows a borrower to return a borrowed book.
        :param borrower_id: Unique ID of the borrower
        :param isbn: ISBN of the book to return
        """
        # Find the borrow record for the borrower and book
        borrower = next((b for b in self.borrowers if b.borrower_id == borrower_id and b.book_borrowed == isbn), None)
        if borrower:
            borrower.return_date = datetime.now()  # Record the return date
            book = next((b for b in self.books if b.isbn == isbn), None)  # Find the book
            book.is_available = True  # Mark the book as available again
            late_fee = self.calculate_late_fee(borrower.borrow_date, borrower.return_date)  # Calculate any late fee
            print(f"Book '{book.title}' returned. Late Fee: ${late_fee:.2f}")  # Confirmation message
        else:
            print("Borrow record not found.")  # Error message if no record matches

    # Calculate late fee based on borrow and return dates
    def calculate_late_fee(self, borrow_date, return_date, daily_fee=1):
        """
        Calculates the late fee for a borrowed book.
        :param borrow_date: Date the book was borrowed
        :param return_date: Date the book was returned
        :param daily_fee: Fee per late day (default: $1)
        :return: Total late fee (0 if returned on time)
        """
        days_late = (return_date - borrow_date).days - 14  # Assuming a 14-day borrow period
        return max(0, days_late * daily_fee)  # Late fee is zero if returned on time or early

    # Save all data (books and borrowers) to a file
    def save_data(self, filename):
        """
        Saves the current state of the library (books and borrowers) to a file.
        :param filename: File to save data to
        """
        with open(filename, 'wb') as f:  # Open the file in write-binary mode
            pickle.dump({"books": self.books, "borrowers": self.borrowers}, f)  # Save both books and borrowers
        print("Data saved successfully.")  # Confirmation message

    # Load all data (books and borrowers) from a file
    def load_data(self, filename):
        """
        Loads the library state (books and borrowers) from a file.
        :param filename: File to load data from
        """
        with open(filename, 'rb') as f:  # Open the file in read-binary mode
            data = pickle.load(f)  # Load the data
            self.books = data["books"]  # Update the books list
            self.borrowers = data["borrowers"]  # Update the borrowers list
        print("Data loaded successfully.")  # Confirmation message

    # Validate an ISBN number
    @staticmethod
    def validate_isbn(isbn):
        """
        Validates the format of an ISBN.
        :param isbn: ISBN to validate
        :return: True if valid, False otherwise
        """
        return len(isbn) == 13 and isbn.isdigit()  # Valid if 13 digits long and all digits


# Example Usage
if __name__ == "__main__":
    library = LibraryManager()  # Create a new library manager

    # Add books to the library
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890123")
    library.add_book("To Kill a Mockingbird", "Harper Lee", "1234567890124")

    # Search and display books
    print("Search Results:", library.search_books("great"))  # Search for books with 'great' in the title
    print("Sorted Books:", library.sort_books(by="title"))  # Sort books alphabetically by title

    # Borrow and return books
    library.borrow_book("1001", "1234567890123")  # Borrow a book by
