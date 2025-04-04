# Q1 Write Z notation specifications for a library management system and validate the specifications in python

class Library:
    def __init__(self):
        # Initial state: ∅ for books, members, and borrowed
        self.books = set()
        self.members = set()
        self.borrowed = {}  # BOOK ↦ MEMBER

    def add_book(self, book):
        # Z: AddBook
        # Preconditions: book ∉ books
        if book in self.books:
            raise ValueError(f"Book '{book}' already exists.")
        self.books.add(book)

    def register_member(self, member):
        # Z: RegisterMember
        # Preconditions: member ∉ members
        if member in self.members:
            raise ValueError(f"Member '{member}' already registered.")
        self.members.add(member)

    def borrow_book(self, book, member):
        # Z: BorrowBook
        # Preconditions:
        #   book ∈ books
        #   member ∈ members
        #   book ∉ dom borrowed
        if book not in self.books:
            raise ValueError(f"Book '{book}' does not exist.")
        if member not in self.members:
            raise ValueError(f"Member '{member}' is not registered.")
        if book in self.borrowed:
            raise ValueError(f"Book '{book}' is already borrowed by '{self.borrowed[book]}'.")
        self.borrowed[book] = member

    def return_book(self, book):
        # Z: ReturnBook
        # Preconditions: book ∈ dom borrowed
        if book not in self.borrowed:
            raise ValueError(f"Book '{book}' was not borrowed.")
        del self.borrowed[book]

    def print_status(self):
        print("Library Status:")
        print(f"  Books   : {sorted(self.books)}")
        print(f"  Members : {sorted(self.members)}")
        print(f"  Borrowed: {self.borrowed}")
        print()


# --- Example Simulation (Validation of Z specs) ---

if __name__ == "__main__":
    lib = Library()

    # InitLibrary is implicitly satisfied by __init__()

    # Add books
    lib.add_book("Book1")
    lib.add_book("Book2")

    # Register members
    lib.register_member("Alice")
    lib.register_member("Bob")

    lib.print_status()

    # Borrow a book
    lib.borrow_book("Book1", "Alice")
    lib.print_status()

    # Attempt to borrow the same book again (should raise an error)
    try:
        lib.borrow_book("Book1", "Bob")
    except ValueError as e:
        print("Error:", e)

    # Return the book
    lib.return_book("Book1")
    lib.print_status()

    # Try to return a non-borrowed book (should raise an error)
    try:
        lib.return_book("Book2")
    except ValueError as e:
        print("Error:", e)
