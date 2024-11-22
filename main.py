from library import Library


def main():
    library = Library("storage.json")

    print("Добро пожаловать в систему управления библиотекой!")
    while True:
        print("\nДоступные команды:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выйти")

        command = input("Введите команду: ")
        if command == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора: ")
            year = int(input("Введите год издания: "))
            book = library.add_book(title, author, year)
            print(f"Книга добавлена: {book.to_dict()}")
        elif command == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            if library.remove_book(book_id):
                print("Книга удалена.")
            else:
                print("Книга с таким ID не найдена.")
        elif command == "3":
            query = input("Введите название, автора или год для поиска: ")
            results = library.search_books(query)
            if results:
                for book in results:
                    print(book.to_dict())
            else:
                print("Книги не найдены.")
        elif command == "4":
            books = library.display_books()
            for book in books:
                print(book)
        elif command == "5":
            book_id = int(input("Введите ID книги: "))
            status = input("Введите новый статус (в наличии/выдана): ")
            if library.update_status(book_id, status):
                print("Статус обновлен.")
            else:
                print("Книга с таким ID не найдена.")
        elif command == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
