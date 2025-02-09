class Movie:
    """Базовый класс для фильма."""
    
    def __init__(self, title: str, director: str):
        """Инициализирует фильм с заданным названием и режиссером."""
        self.title = title
        self.director = director

    def play(self):
        """Выводит сообщение о просмотре фильма."""
        print(f"Собираемся смотреть фильм '{self.title}' реж. {self.director}.")

class Horror(Movie):
    """Класс для фильмов ужасов."""
    
    def play(self):
        """Включает фильм ужасов."""
        print(f"Включаем фильм ужасов '{self.title}' реж. {self.director}.")
        
class Action(Movie):
    """Класс для боевиков."""
    
    def play(self):
        """Включает боевик."""
        print(f"Включаем боевик '{self.title}' реж. {self.director}.")
        
class Romance(Movie):
    """Класс для мелодрам."""
    
    def play(self):
        """Включает мелодраму."""
        print(f"Включаем мелодраму '{self.title}' реж. {self.director}.")
        
class Drama(Movie):
    """Класс для драм."""
    
    def play(self):
        """Включает драму."""
        print(f"Включаем драму '{self.title}' реж. {self.director}.")
        
class Comedy(Movie):
    """Класс для комедий."""
    
    def play(self):
        """Включает комедию."""
        print(f"Включаем комедию '{self.title}' реж. {self.director}.")

class FilmCatalogue:
    """Класс для каталога фильмов."""
    
    def __init__(self):
        """Инициализирует пустой список фильмов."""
        self.films_list = []

    def add_movie(self, film: Movie):
        """Добавляет фильм в каталог."""
        self.films_list.append(film)

    def play_all_movies(self):
        """Запускает воспроизведение всех фильмов из каталога."""
        for film in self.films_list:
            film.play()

    def search_movies_by_genre(self, genre: type):
        """Ищет фильмы по жанру."""
        return [film for film in self.films_list if isinstance(film, genre)]

    def play_movies_by_genre(self, genre: type):
        """Запускает воспроизведение фильмов определенного жанра."""
        for film in self.search_movies_by_genre(genre):
            film.play()


# Создание экземпляра каталога фильмов
my_catalogue = FilmCatalogue()

# Добавление фильмов в каталог
my_catalogue.add_movie(Drama("Крестный отец", "Френсис Ф. Коппола"))
my_catalogue.add_movie(Comedy("Ночные игры", "Джон Фрэнсис Дейли, Джонатан М. Голдштейн"))
my_catalogue.add_movie(Horror("Дракула Брэма Стокера", "Френсис Ф. Коппола"))
my_catalogue.add_movie(Action("Крушение", "Жан-Франсуа Рише"))
my_catalogue.add_movie(Romance("Честная куртизанка", "Маршалл Херсковиц"))

# Воспроизведение всех фильмов
my_catalogue.play_all_movies()

# Поиск фильмов ужасов
print(f"\nНайдены фильмы ужасов:")
for movie in my_catalogue.search_movies_by_genre(Horror):
    print(movie.title)

# Воспроизведение фильмов из жанра мелодрамы
print(f"\nЗапускаем фильм из жанра 'Мелодрамы':")
my_catalogue.play_movies_by_genre(Romance)
