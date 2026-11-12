class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)

book1 = Book("Python Basics", "Mehak")
book2 = Book("IoT Projects", "Kaveeta Kumari")
book3 = Book("Data Science", "Noor Amina")

book1.display_info()
book2.display_info()
book3.display_info()