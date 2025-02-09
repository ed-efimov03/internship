class Publisher:
    """Класс, представляющий издательство.

    Этот класс хранит информацию об издательстве.
    Также предоставляет методы для получения информации и публикации.

    Attributes:
        name (str): Название издательства
        location (str): Месторасположение издательства
    """

    def __init__(self, name: str, location: str):
        """Инициализирует экземляр класса Publisher

        Args:
            name (str): Название издательства
            location (str): Месторасположение издательства

        Raises:
            ValueError: Невалидное значение.
        """

        if not(isinstance(name, str) and isinstance(location, str)):
            raise ValueError("Вы ввели невалидные значения")

        self.name = name
        self.location = location

    def get_info(self) -> str:
        """Возвращает информацию об издателе

        Returns:
            info (str): Информация о книге
        """

        return f"Название издательства: {self.name}, Расположение издательства: {self.location}"

    def publish(self, message: str):
        """Имитирует процесс подготовки к публикации

        Args:
            message (str): Сообщение

        Raises:
            ValueError: Невалидное значение.
        """

        if not isinstance(message, str):
            raise ValueError("Вы ввели невалидные значения")

        print(f"Готовим {message} к публикации в {self.name} ({self.location})")

class BookPublisher(Publisher):
    """Класс, представляющий издательство книг.

    Наследуется от Publisher и добавляет количество авторов.

    Attributes:
        name (str): Название издательства
        location (str): Месторасположение издательства
        num_authors (int): Кол-во авторов
    """

    def __init__(self, name: str, location: str, num_authors: int):
        """Инициализирует экземляр класса BookPublisher

        Args:
            name (str): Название издательства
            location (str): Месторасположение издательства
            num_authors (int): Кол-во авторов

        Raises:
            ValueError: Невалидное значение.
        """

        if not(isinstance(name, str) and isinstance(location, str) and isinstance(num_authors, int)):
            raise ValueError("Вы ввели невалидные значения")

        super().__init__(name, location)
        self.num_authors = num_authors

    def publish(self, title: str, author: str):
        """Имитирует процесс подготовки к публикации книги

        Args:
            title (str): Название книги
            author (str): Автор книги

        Raises:
            ValueError: Невалидное значение.
        """

        if not (isinstance(title, str) and isinstance(author, str)):
            raise ValueError("Вы ввели невалидные значения")

        print(f"Передаем рукопись '{title}', написанную автором {author} в издательство {self.name} ({self.location})")

class NewspaperPublisher(Publisher):
    """Класс, представляющий издательство газет.

    Наследуется от Publisher и добавляет количество страниц.

    Attributes:
        name (str): Название издательства
        location (str): Месторасположение издательства
        num_pages (int): Кол-во страниц
    """

    def __init__(self, name: str, location: str, num_pages: int):
        """Инициализирует экземляр класса NewspaperPublisher

        Args:
            name (str): Название издательства
            location (str): Месторасположение издательства
            num_pages (int): Кол-во страниц

        Raises:
            ValueError: Невалидное значение.
        """

        if not(isinstance(name, str) and isinstance(location, str) and isinstance(num_pages, int)):
            raise ValueError("Вы ввели невалидные значения")

        super().__init__(name, location)
        self.num_pages = num_pages

    def publish(self, headline: str):
        """Имитирует процесс подготовки к публикации газеты

        Args:
            headline (str): Название газеты

        Raises:
            ValueError: Невалидное значение.
        """

        if not isinstance(headline, str):
            raise ValueError("Вы ввели невалидные значения")

        print(f'Печатаем свежий номер со статьей "{headline}" на главной странице в издательстве {self.name} ({self.location})')


#Проверяем работу программы
publisher = Publisher("АБВГД Пресс", "Москва")
publisher.publish("Справочник писателя")

book_publisher = BookPublisher("Важные Книги", "Самара", 52)
book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
newspaper_publisher.publish("Новая версия Midjourney будет платной")