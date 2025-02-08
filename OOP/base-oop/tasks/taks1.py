class Book:
    def __init__(self, title: str, author: str, year_release: int):
        self.title = ' '.join(word.capitalize() for word in title.split())
        self.author = ' '.join(word.capitalize() for word in author.split())
        self.year_release = year_release

    """Выводит информацию о книге."""
    def show_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год выпуска: {self.year_release}")

    """Сравнивает книги по заголовку, автору и году выпуска."""
    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title, self.author, self.year_release) == (other.title, other.author, other.year_release)
        
    """Возвращает уникальный хеш-код для книги."""    
    def __hash__(self):
        return hash((self.title, self.author, self.year_release))

class Library:
    def __init__(self):
        self.books_list = dict()

    def add_book(self, new_book: Book):
        """Добавляет книгу в библиотеку, увеличивая её количество, если такая уже есть."""
        self.books_list[new_book] = self.books_list.get(new_book, 0) + 1 

    def show_books(self):
        """Выводит список книг и их количество."""
        if not self.books_list:
            print("В библиотеке пока нет книг.\n")
            return
        print("Список имеющихся книг:")
        for book, count in self.books_list.items():
            book.show_info()
            print(f"Кол-во книг в наличии: {count}")
            print()

class Reader:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def take_book(self, book: Book, lib: Library):
        """Позволяет читателю взять книгу, если она есть в наличии."""
        if lib.books_list.get(book, 0) > 0:  # Проверяем, есть ли книга в библиотеке
            lib.books_list[book] -= 1
            print(f"{self.name} {self.surname} взял книгу '{book.title}' ({book.author}). Приятного чтения!\n")
        else:
            print(f"Книга '{book.title}' сейчас отсутствует в библиотеке.\n")

    def return_book(self, book: Book, lib: Library):
        if book in lib.books_list:
            lib.books_list[book] += 1
            print("Спасибо за возрат книги\n")
        else:
            print("Данной книги нет в реестре\n")




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