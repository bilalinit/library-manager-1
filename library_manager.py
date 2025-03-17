import json
import os

LIBRARY_FILE = 'library.txt'

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input(f"\nEnter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")


    print("Have you read this book?")
    print("1. Yes")
    print("2. No")

    while True:  
        read_choice = input("Enter your choice (1/2): ").strip()
        if read_choice == '1':
            read_status = True
            break
        elif read_choice == '2':
            read_status = False
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read_status
    }

    library.append(book)
    print("Book added successfully!\n")

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!\n")
            return
    print("Book not found.\n")

def search_book(library):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")

    if choice == '1':
        search_key = 'title'
    elif choice == '2':
        search_key = 'author'
    else:
        print("Invalid choice.\n")
        return
    
    query = input(f"Enter the {search_key}: ").strip().lower()
    matches = [book for book in library if query in book[search_key].lower()]

    if matches:
        print("\nMatching Books:")
        for i, book in enumerate(matches, 1):
            status = 'Read' if book['read'] else 'Unread'
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        print()
    else:
        print("No matching books found.\n")

def display_books(library):
    if not library:
        print("Your library is empty.\n")
        return
    
    print("\nYour Library:")
    for i, book in enumerate(library, 1):
        status = 'Read' if book['read'] else 'Unread'
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    print()

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        read_percentage = 0
    else:
        read_books = sum(1 for book in library if book['read'])
        read_percentage = (read_books / total_books) * 100
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {read_percentage:.2f}%\n")

def main():
    library = load_library()
    
    while True:
        print("Welcome to your Personal Library Manager! \n")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("\nLibrary saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

