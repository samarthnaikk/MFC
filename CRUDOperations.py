class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book_id, title, author):
        self.books.append(Book(book_id, title, author))

    def add_member(self, member_id, name):
        self.members.append(Member(member_id, name))

    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.book_id != book_id]

    def remove_member(self, member_id):
        self.members = [member for member in self.members if member.member_id != member_id]

    def update_book(self, book_id, title, author):
        for book in self.books:
            if book.book_id == book_id:
                book.title = title
                book.author = author

    def update_member(self, member_id, name):
        for member in self.members:
            if member.member_id == member_id:
                member.name = name

    def list_books(self):
        for book in self.books:
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

    def list_members(self):
        for member in self.members:
            print(f"ID: {member.member_id}, Name: {member.name}")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Update Book")
        print("4. List Books")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. Update Member")
        print("8. List Members")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            library.add_book(book_id, title, author)
        elif choice == "2":
            book_id = input("Enter Book ID to remove: ")
            library.remove_book(book_id)
        elif choice == "3":
            book_id = input("Enter Book ID to update: ")
            title = input("Enter new Title: ")
            author = input("Enter new Author: ")
            library.update_book(book_id, title, author)
        elif choice == "4":
            library.list_books()
        elif choice == "5":
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            library.add_member(member_id, name)
        elif choice == "6":
            member_id = input("Enter Member ID to remove: ")
            library.remove_member(member_id)
        elif choice == "7":
            member_id = input("Enter Member ID to update: ")
            name = input("Enter new Name: ")
            library.update_member(member_id, name)
        elif choice == "8":
            library.list_members()
        elif choice == "9":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
