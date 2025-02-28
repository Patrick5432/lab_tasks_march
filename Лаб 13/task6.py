class Book:
    def __init__(self, author, title, publisher, year, number_of_pages):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Автор - {self.author} - Название - {self.title} (Публикация: {self.publisher}, Год: {self.year})"


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def get_books_by_publisher(self, publisher):
        return [book for book in self.books if book.publisher.lower() == publisher.lower()]

    def get_books_after_year(self, year):
        return [book for book in self.books if book.year > year]

    def print_books(self, books):
        for book in books:
            print(book)


# Пример использования
bm = BookManager()
bm.add_book(Book("Шестопал", "Сумеречный страх", "Книжный1", 2005, 100))
bm.add_book(Book("Глинко", "Восстание зени", "Книжный2", 2010, 150))
bm.add_book(Book("Харламов", "Улун", "Книжный3", 1998, 200))

print("Книги автора Шестопала:")
bm.print_books(bm.get_books_by_author("Шестопал"))

print("\nКниги публикации книжный2:")
bm.print_books(bm.get_books_by_publisher("Книжный2"))

print("\nКниги выпуска после 2005:")
bm.print_books(bm.get_books_after_year(2005))