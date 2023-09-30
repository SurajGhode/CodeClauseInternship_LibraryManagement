class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'Book "{title}" by {author} added to the library.')

    def display_books(self):
        print("Books in the library:")
        for index, book in enumerate(self.books, start=1):
            print(f'{index}. "{book.title}" by {book.author} - {"Available" if book.is_available else "Not Available"}')

    def lend_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if book.is_available:
                book.is_available = False
                print(f'You have successfully borrowed "{book.title}".')
            else:
                print('Sorry, this book is not available.')
        else:
            print('Invalid book index.')

    def return_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if not book.is_available:
                book.is_available = True
                print(f'Thank you for returning "{book.title}".')
            else:
                print('This book is already in the library.')
        else:
            print('Invalid book index.')

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author's name: ")
            library.add_book(title, author)
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            library.display_books()
            book_index = int(input("Enter the index of the book you want to borrow: "))
            library.lend_book(book_index)
        elif choice == '4':
            library.display_books()
            book_index = int(input("Enter the index of the book you want to return: "))
            library.return_book(book_index)
        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
