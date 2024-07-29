class LibraryManager:
    def _init_(self):
        self.books = {}
    
    def add_book(self, title, author, publisher, volume, year, isbn):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
            return
        self.books[isbn] = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'volume': volume,
            'year': year,
            'isbn': isbn
        }
        print(f"Book '{title}' added successfully.")

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed successfully.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def retrieve_book(self, isbn):
        book = self.books.get(isbn)
        if book:
            return book
        else:
            print(f"No book found with ISBN {isbn}.")
            return None

    def search_books(self, search_term):
        results = []
        for book in self.books.values():
            if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower():
                results.append(book)
        return results

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return []
        return list(self.books.values())

    def update_book(self, isbn, title=None, author=None, publisher=None, volume=None, year=None):
        if isbn not in self.books:
            print(f"No book found with ISBN {isbn}.")
            return
        
        book = self.books[isbn]
        if title:
            book['title'] = title
        if author:
            book['author'] = author
        if publisher:
            book['publisher'] = publisher
        if volume:
            book['volume'] = volume
        if year:
            book['year'] = year
        
        print(f"Book with ISBN {isbn} updated successfully.")

    def is_book_available(self, isbn):
        return isbn in self.books

# Sample usage
if __name__ == "_main_":
    library = LibraryManager()

    # Adding books
    library.add_book("Operating Systems: Principles and Practice", "Sunil Vasthav", "Tech Press", "1st", 2021, "978-1234567890")
    library.add_book("Data Structures and Algorithms in Python", "Nita Mary", "Coding Books", "2nd", 2023, "978-0987654321")
    library.add_book("Machine Learning with Python", "Ankit Raj", "Data Science Inc.", "1st", 2022, "978-1122334455")

    # Listing all books
    print("\nListing all books:")
    for book in library.list_books():
        print(book)

    # Retrieving a book by ISBN
    print("\nRetrieving book with ISBN 978-1234567890:")
    book = library.retrieve_book("978-1234567890")
    print(book)

    # Searching for books
    print("\nSearching for books by author 'Nita Mary':")
    results = library.search_books("Nita Mary")
    for book in results:
        print(book)

    # Updating a book
    print("\nUpdating book with ISBN 978-1122334455:")
    library.update_book("978-1122334455", title="Advanced Machine Learning with Python", year=2024)

    # Checking availability
    print("\nChecking availability of book with ISBN 978-1234567890:")
    print("Available" if library.is_book_available("978-1234567890") else "Not Available")

    # Removing a book
    print("\nRemoving book with ISBN 978-0987654321:")
    library.remove_book("978-0987654321")

    # Listing all books after removal
    print("\nListing all books after removal:")
    for book in library.list_books():
        print(book)