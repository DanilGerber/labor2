BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# Определяем класс Book
class Book:
    def __init__(self, id_, name, pages):
        self.id = id_  # Идентификатор книги
        self.name = name  # Название книги
        self.pages = pages  # Количество страниц

    def __str__(self):
        return f'Книга "{self.name}"'


# Определяем класс Library
class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            last_book_id = self.books[-1].id  # Получаем id последней книги
            return last_book_id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:  # Если нашли книгу с нужным id
                return index
        raise ValueError("Книги с запрашиваемым id не существует")  # Если не нашли, вызываем ошибку


if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())  # Проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с id = 1
