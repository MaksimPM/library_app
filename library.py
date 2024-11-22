import json
from typing import List, Dict


class Book:
    """Класс, представляющий книгу."""

    def __init__(self, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = id(self)
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> Dict:
        """Преобразует объект книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        """Создает объект книги из словаря."""
        book = Book(data["title"], data["author"], data["year"], data["status"])
        book.id = data["id"]
        return book


class Library:
    """Класс, представляющий библиотеку."""

    def __init__(self, storage_file: str):
        self.storage_file = storage_file
        self.books: List[Book] = self._load_books()

    def _load_books(self) -> List[Book]:
        """Загружает книги из файла."""
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as file:
                return [Book.from_dict(book) for book in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_books(self) -> None:
        """Сохраняет книги в файл."""
        with open(self.storage_file, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> Book:
        """Добавляет новую книгу в библиотеку."""
        book = Book(title, author, year)
        self.books.append(book)
        self._save_books()
        return book

    def remove_book(self, book_id: int) -> bool:
        """Удаляет книгу по ID."""
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self._save_books()
                return True
        return False

    def search_books(self, query: str) -> List[Book]:
        """Ищет книги по названию, автору или году."""
        return [book for book in self.books if query.lower() in str(book.to_dict()).lower()]

    def display_books(self) -> List[Dict]:
        """Возвращает список всех книг."""
        return [book.to_dict() for book in self.books]

    def update_status(self, book_id: int, status: str) -> bool:
        """Изменяет статус книги по ID."""
        for book in self.books:
            if book.id == book_id:
                book.status = status
                self._save_books()
                return True
        return False
