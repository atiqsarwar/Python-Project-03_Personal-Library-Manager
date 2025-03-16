import json

def load_library(filename='library.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading library file. Starting with empty library.")
        return []

def save_library(books, filename='library.json'):
    with open(filename, 'w') as f:
        json.dump(books, f, indent=4)

def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book(books):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    
    while True:
        year_str = input("Enter the publication year: ").strip()
        try:
            year = int(year_str)
            if year < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid year. Please enter a valid positive integer.")
    
    genre = input("Enter the genre: ").strip()
    
    while True:
        read_input = input("Have you read this book? (yes/no): ").strip().lower()
        if read_input in ['yes', 'y']:
            read_status = True
            break
        elif read_input in ['no', 'n']:
            read_status = False
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    book = {
        'title': title,
        'author': author,
        'publication_year': year,
        'genre': genre,
        'read_status': read_status
    }
    books.append(book)
    print("Book added successfully!")

def remove_book(books):
    title = input("Enter the title of the book to remove: ").strip()
    matches = [book for book in books if book['title'].lower() == title.lower()]
    
    if not matches:
        print("No book found with that title.")
        return
    
    if len(matches) == 1:
        books.remove(matches[0])
        print("Book removed successfully!")
    else:
        print("Multiple books found with that title:")
        for idx, book in enumerate(matches, 1):
            print(f"{idx}. {book['title']} by {book['author']} ({book['publication_year']})")
        choice = input("Enter the number of the book to remove: ")
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(matches):
                books.remove(matches[choice_idx])
                print("Book removed successfully!")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def search_books(books):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ").strip()
    
    if choice not in ['1', '2']:
        print("Invalid choice.")
        return
    
    search_term = input("Enter the search term: ").strip().lower()
    results = []
    
    if choice == '1':
        results = [book for book in books if search_term in book['title'].lower()]
    else:
        results = [book for book in books if search_term in book['author'].lower()]
    
    if not results:
        print("No matching books found.")
    else:
        print("Matching Books:")
        for idx, book in enumerate(results, 1):
            read_status = "Read" if book['read_status'] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {read_status}")

def display_all_books(books):
    if not books:
        print("Your library is empty.")
        return
    print("\nYour Library:")
    for idx, book in enumerate(books, 1):
        read_status = "Read" if book['read_status'] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {read_status}")

def display_statistics(books):
    total = len(books)
    print(f"\nTotal books: {total}")
    if total == 0:
        print("Percentage read: 0.0%")
        return
    read_count = sum(1 for book in books if book['read_status'])
    percentage = (read_count / total) * 100
    print(f"Percentage read: {percentage:.1f}%")

def main():
    books = load_library()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_book(books)
        elif choice == '2':
            remove_book(books)
        elif choice == '3':
            search_books(books)
        elif choice == '4':
            display_all_books(books)
        elif choice == '5':
            display_statistics(books)
        elif choice == '6':
            save_library(books)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()