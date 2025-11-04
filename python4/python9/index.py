class Library:
    def __init__(self, list_of_books, name):
        self.booksList = list_of_books
        self.name = name
        self.lendDict = {}

        def displayBooks(self):
            print(f"We have the following books in our library: {self.name}")
            for book in self.booksList:
                print(book)

    def lendBook(self, user, book):
        if book not in self.bookList:
            print("Sorry, we do not have that book.")
        elif book in self.LendDict:
            print(f"The book is already being used by {self.LendDict[book]}")
        else:
            self.lendDict[book] = user
            print(
                "Lender-Book database has been updated. You can take the book now."
            )
            def addBooj(self, book):
                self.bookList.append(book)
                print(f"{book} has been added to the book list.")

            def returnBook(self, book):
                if book in self.LendDict:
                    del self.LendDict[book]
                    print("Book has been returned")
                else:
                    print("That book wasn't borrowed from us.")
if__name__== '__main__':
    books = Libary([
        'Python','Rich dad poor dad','Harry Potter'
    ], "Let's Upskill")
    user_name = input("Welcome to our library! Please enter your name:")
    while True:
        print(
            f"nHello {user_name}, welcome to the {books.name}"
        )