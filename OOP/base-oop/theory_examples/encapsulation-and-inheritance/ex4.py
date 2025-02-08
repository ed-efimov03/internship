class Publisher:
    # Инициализация издательства с его названием и местоположением
    def __init__(self, name: str, location: str):
        self.name = name  # Название издательства
        self.location = location  # Местоположение издательства

    # Метод для получения информации об издательстве
    def get_info(self):
        return f"Название издательства: {self.name}, Расположение издательства: {self.location}"

    # Метод для публикации сообщения
    def publish(self, message: str):
        print(f"Готовим {message} к публикации в {self.name} ({self.location})")  # Выводим информацию о подготовке публикации

class BookPublisher(Publisher):
    # Инициализация специализированного издательства для книг с дополнительным параметром: количество авторов
    def __init__(self, name: str, location: str, num_authors: int):
        super().__init__(name, location)  # Вызов конструктора родительского класса
        self.num_authors = num_authors  # Количество авторов

    # Метод для публикации книги с указанием названия и автора
    def publish(self, title: str, author: str):
        print(f"Передаем рукопись '{title}', написанную автором {author} в издательство {self.name} ({self.location})")  # Выводим информацию о передаче рукописи

class NewspaperPublisher(Publisher):
    # Инициализация специализированного издательства для газет с дополнительным параметром: количество страниц
    def __init__(self, name: str, location: str, num_pages: int):
        super().__init__(name, location)  # Вызов конструктора родительского класса
        self.num_pages = num_pages  # Количество страниц в газете

    # Метод для публикации свежего номера с заголовком
    def publish(self, headline: str):
        print(f'Печатаем свежий номер со статьей "{headline}" на главной странице в издательстве {self.name} ({self.location})')  # Выводим информацию о публикации статьи

# Создаем объект общего издательства
publisher = Publisher("АБВГД Пресс", "Москва")
publisher.publish("Справочник писателя")  # Публикуем сообщение в общем издательстве

# Создаем объект издательства для книг
book_publisher = BookPublisher("Важные Книги", "Самара", 52)
book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")  # Публикуем книгу в издательстве

# Создаем объект издательства для газет
newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
newspaper_publisher.publish("Новая версия Midjourney будет платной")  # Публикуем статью в газете
