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
        return f'Книга "{self.name}"'  # Возвращаем строку с названием книги

    def __repr__(self):
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'  # Возвращаем строку для инициализации


if __name__ == '__main__':
    # Инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    for book in list_books:
        print(book)  # Проверяем метод str

    print(list_books)  # Проверяем метод repr
