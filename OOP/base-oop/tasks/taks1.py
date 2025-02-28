class Book:
    """Класс, представляющий книгу.

    Этот класс используется для хранения информации о книге, таких как название, автор и год выпуска.

    Атрибуты:
        _title (str): Название книги.
        _author (str): Автор книги.
        _year_release (int): Год выпуска книги.

    Методы:
        show_info: Выводит информацию о книге.
        __eq__: Сравнивает две книги по их атрибутам.
        __hash__: Возвращает хеш-значение для книги.
    """

    def __init__(self, title: str, author: str, year_release: int):
        """Инициализирует объект книги с указанными параметрами.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year_release (int): Год выпуска книги.
        """

        self._title = ' '.join(word.capitalize() for word in title.split())
        self._author = ' '.join(word.capitalize() for word in author.split())
        self._year_release = year_release

    def get_title(self):
        """Геттер для названия книги."""

        return self._title
    
    def get_author(self):
        """Геттер для автора книги."""

        return self._author
    
    def get_year_release(self):
        """Геттер для года выхода книги."""

        return self._year_release

    def show_info(self):
        """Выводит информацию о книге."""

        print(f"Название: {self.get_title()}")
        print(f"Автор: {self.get_author()}")
        print(f"Год выпуска: {self.get_year_release()}")

    def __eq__(self, other):
        """Сравнивает текущую книгу с другой книгой по атрибутам.

        Args:
            other (Book): Другая книга, с которой нужно сравнить.

        Returns:
            bool: True, если книги одинаковые, иначе False.
        """
        
        if isinstance(other, Book):
            return (self.get_title(), self.get_author(), self.get_year_release()) == (other.get_title(), other.get_author(), other.get_year_release())
        
    def __hash__(self):
        """Возвращает хеш-значение для книги.

        Returns:
            int: Хеш-значение книги.
        """

        return hash((self.get_title(), self.get_author(), self.get_year_release()))


class Library:
    """Класс, представляющий библиотеку.

    Этот класс используется для управления коллекцией книг в библиотеке, добавления книг и вывода списка книг.

    Атрибуты:
        books_list (dict): Словарь, содержащий книги и их количество в наличии.

    Методы:
        add_book: Добавляет книгу в библиотеку.
        show_books: Показывает все книги, доступные в библиотеке.
        get_book_count: Возвращает количество доступных экземпляров книги.
        set_book_count: Устанавливает количество экземпляров книги.
    """

    def __init__(self):
        """Инициализирует объект библиотеки с пустым списком книг."""

        self._books_list = dict()

    def get_books_list(self):
        """Возвращает содержимое библиотеки."""

        return self._books_list

    def add_book(self, new_book: Book):
        """Добавляет новую книгу в библиотеку или увеличивает количество уже имеющейся.

        Args:
            new_book (Book): Книга, которую нужно добавить в библиотеку.
        """

        self._books_list[new_book] = self.get_books_list().get(new_book, 0) + 1 

    def get_book_count(self, book: Book):
        """Возвращает количество доступных экземпляров книги.

        Args:
            book (Book): Книга, количество которой нужно получить.

        Returns:
            int: Количество экземпляров книги в библиотеке.
        """

        return self._books_list.get(book, 0)

    def set_book_count(self, book: Book, count: int):
        """Устанавливает количество экземпляров книги в библиотеке.

        Args:
            book (Book): Книга, количество которой нужно установить.
            count (int): Новое количество экземпляров книги.
        """

        if count < 0:
            raise ValueError("Количество книг не может быть отрицательным.")
        self._books_list[book] = count

    def show_books(self):
        """Выводит список всех книг в библиотеке с количеством каждой книги."""

        if not self.get_books_list():
            print("В библиотеке пока нет книг.\n")
            return
        print("Список имеющихся книг:")
        for book, count in self.get_books_list().items():
            book.show_info()
            print(f"Кол-во книг в наличии: {count}")
            print()


class Reader:
    """Класс, представляющий читателя.

    Этот класс используется для управления действиями читателя в библиотеке, такими как взятие книги и ее возврат.

    Атрибуты:
        _name (str): Имя читателя.
        _surname (str): Фамилия читателя.
        _age (int): Возраст читателя.

    Методы:
        get_name: Геттер для имени читателя.
        get_surname: Геттер для фамилии читателя.
        get_age: Геттер для возраста читателя.
        take_book: Читатель берет книгу из библиотеки.
        return_book: Читатель возвращает книгу в библиотеку.
    """

    def __init__(self, name: str, surname: str, age: int):
        """Инициализирует объект читателя с указанными параметрами.

        Args:
            name (str): Имя читателя.
            surname (str): Фамилия читателя.
            age (int): Возраст читателя.
        """

        self._name = name
        self._surname = surname
        self._age = age

    def get_name(self):
        """Геттер для имени читателя."""

        return self._name
    
    def get_surname(self):
        """Геттер для фамилии читателя."""

        return self._surname
    
    def get_age(self):
        """Геттер для возраста читателя."""

        return self._name

    def take_book(self, book: Book, lib: Library):
        """Читатель берет книгу из библиотеки, если она доступна.

        Args:
            book (Book): Книга, которую читатель хочет взять.
            lib (Library): Библиотека, из которой берется книга.
        """

        current_count = lib.get_book_count(book)
        if current_count > 0:  
            lib.set_book_count(book, current_count - 1)
            print(f"{self.get_name()} {self.get_surname()} взял книгу '{book.get_title()}' ({book.get_author()}). Приятного чтения!\n")
        else:
            print(f"Книга '{book.title}' сейчас отсутствует в библиотеке.\n")

    def return_book(self, book: Book, lib: Library):
        """Читатель возвращает книгу в библиотеку.

        Args:
            book (Book): Книга, которую читатель возвращает.
            lib (Library): Библиотека, куда возвращается книга.
        """

        if book in lib.get_books_list():
            current_count = lib.get_book_count(book)
            lib.set_book_count(book, current_count + 1)
            print("Спасибо за возврат книги\n")
        else:
            print("Данной книги нет в реестре\n")


# Пример использования
library1 = Library()

book1 = Book(title="1984", author="George Orwell", year_release=1949)
book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", year_release=1960)
book3 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year_release=1925)
book4 = Book(title="To Kill a Mockingbird", author="Harper Lee", year_release=1960)
book5 = Book(title="To Kill a Mockingbird", author="Harper Lee", year_release=1960)

library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)
library1.add_book(book4)
library1.add_book(book5)

library1.show_books()

reader1 = Reader("Ed", "Efimov", 21)

reader1.take_book(Book(title="To Kill a Mockingbird", author="Harper Lee", year_release=1960), library1)
library1.show_books()

reader1.return_book(Book(title="To Kill a Mockingbird", author="Harper Lee", year_release=1960), library1)
library1.show_books()
