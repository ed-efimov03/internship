# Определяем класс Movie, представляющий общий интерфейс для всех фильмов
class Movie:
    def __init__(self, title: str, director: str):
        self.title = title  # Название фильма
        self.director = director  # Имя режиссера

    # Метод для воспроизведения фильма
    def play(self):
        print(f"Собираемся смотреть фильм '{self.title}' реж. {self.director}.")


# Определяем подклассы для различных жанров фильмов, наследуемые от Movie

# Класс фильмов ужасов
class Horror(Movie):
    def play(self):
        print(f"Включаем фильм ужасов '{self.title}' реж. {self.director}.")

# Класс боевиков
class Action(Movie):
    def play(self):
        print(f"Включаем боевик '{self.title}' реж. {self.director}.")

# Класс мелодрам
class Romance(Movie):
    def play(self):
        print(f"Включаем мелодраму '{self.title}' реж. {self.director}.")

# Класс драм
class Drama(Movie):
    def play(self):
        print(f"Включаем драму '{self.title}' реж. {self.director}.")

# Класс комедий
class Comedy(Movie):
    def play(self):
        print(f"Включаем комедию '{self.title}' реж. {self.director}.")


# Класс каталога фильмов, содержащий список фильмов и методы работы с ними
class FilmCatalogue:
    def __init__(self):
        self.films_list = []  # Список фильмов в каталоге

    # Метод для добавления фильма в каталог
    def add_movie(self, film: Movie):
        self.films_list.append(film)

    # Метод для воспроизведения всех фильмов в каталоге
    def play_all_movies(self):
        for film in self.films_list:
            film.play()

    # Метод для поиска фильмов по жанру
    def search_movies_by_genre(self, genre: type):
        return [film for film in self.films_list if isinstance(film, genre)]

    # Метод для воспроизведения фильмов определенного жанра
    def play_movies_by_genre(self, genre: type):
        for film in self.search_movies_by_genre(genre):
            film.play()


# Создание экземпляра каталога фильмов
my_catalogue = FilmCatalogue()

# Добавление различных фильмов в каталог
my_catalogue.add_movie(Drama("Крестный отец", "Френсис Ф. Коппола"))
my_catalogue.add_movie(Comedy("Ночные игры", "Джон Фрэнсис Дейли, Джонатан М. Голдштейн"))
my_catalogue.add_movie(Horror("Дракула Брэма Стокера", "Френсис Ф. Коппола"))
my_catalogue.add_movie(Action("Крушение", "Жан-Франсуа Рише"))
my_catalogue.add_movie(Romance("Честная куртизанка", "Маршалл Херсковиц"))

# Воспроизведение всех фильмов в каталоге
my_catalogue.play_all_movies()

# Поиск и вывод списка фильмов ужасов
print(f"\nНайдены фильмы ужасов:")
for movie in my_catalogue.search_movies_by_genre(Horror):
    print(movie.title)

# Воспроизведение всех фильмов жанра "Мелодрамы"
print(f"\nЗапускаем фильм из жанра 'Мелодрамы':")
my_catalogue.play_movies_by_genre(Romance)
