class Book:
    page_material = "Бумага"
    presence_of_text = True

    def __init__(self, book_title, author, number_of_pages, ISBN, reserved=False):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.reserved = reserved

    def get_info_reserved(self):
        info = (
            f"Название: {self.book_title}, Автор: {self.author}, страниц: {self.number_of_pages}, "
            f"материал: {self.page_material}"
        )
        if self.reserved:
            info += ', зарезервировано'
        return info


book_one = Book("Lord of the Rings", "John Ronald Reuel Tolkien", 200, "978-3-1245-6789-0", True)
book_two = Book("Alice in Wonderland", "Lewis Carroll", 300, "978-1-8765-4321-7", False)
book_three = Book("Harry Potter", "JK Rowling", 400, "978-5-9012-3456-8", False)
book_four = Book("Don Quixote", "Miguel de Cervantes", 500, "978-0-4567-8912-3", False)
book_five = Book("A tale of two cities", "Charles Dickens", 600, "978-7-2345-6789-4", False)

all_books = [book_one, book_two, book_three, book_four, book_five]
for book in all_books:
    print(book.get_info_reserved())


class SchoolBook(Book):

    def __init__(self, subject, school_class, book_title, author,
                 number_of_pages, ISBN, reserved=False, availability_of_tasks=False):
        super().__init__(book_title, author, number_of_pages, ISBN, reserved)
        self.subject = subject
        self.school_class = school_class
        self.availability_of_tasks = availability_of_tasks

    def git_info_reserved_school(self):
        info = super().get_info_reserved()
        info += f", предмет: {self.subject}, класс: {self.school_class}"
        return info


math_book = SchoolBook(
    "Алгебра", 7, "Алгебра 7-ой класс", "Geneva Brossky",
    40, "978-7-2345-6789-4", True, True
)
chemistry = SchoolBook(
    "Химия", 10, "Химия 10-ый класс", "Pavel Potri",
    50, "978-7-2345-6789-4", False, True
)
physics = SchoolBook(
    "Биология", 6, "Биология 6-ой класс", "Fedor Bonch",
    20, "978-7-2345-6789-4", False, False
)

school_books = [math_book, chemistry, physics]
for book in school_books:
    print(book.git_info_reserved_school())
