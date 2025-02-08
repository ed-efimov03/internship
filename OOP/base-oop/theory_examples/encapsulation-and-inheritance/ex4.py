class Publisher:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

    def get_info(self):
        return f"Название издательства: {self.name}, Расположение издательства: {self.location}"

    def publish(self, message: str):
        print(f"Готовим {message} к публикации в {self.name} ({self.location})")

class BookPublisher(Publisher):
    def __init__(self, name: str, location: str, num_authors: int):
        super().__init__(name, location)
        self.num_authors = num_authors

    def publish(self, title: str, author: str):
        print(f"Передаем рукопись '{title}', написанную автором {author} в издательство {self.name} ({self.location})")

class NewspaperPublisher(Publisher):
    def __init__(self, name: str, location: str, num_pages: int):
        super().__init__(name, location)
        self.num_pages = num_pages

    def publish(self, headline: str):
        print(f'Печатаем свежий номер со статьей "{headline}" на главной странице в издательстве {self.name} ({self.location})')

publisher = Publisher("АБВГД Пресс", "Москва")
publisher.publish("Справочник писателя")

book_publisher = BookPublisher("Важные Книги", "Самара", 52)
book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
newspaper_publisher.publish("Новая версия Midjourney будет платной")