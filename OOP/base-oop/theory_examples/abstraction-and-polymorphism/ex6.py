class Movie:
    def __init__(self, title: str, director: str):
        self.title = title
        self.director = director

    def play(self):
        print(f"Собираемся смотреть фильм '{self.title}' реж. {self.director}.")

class Horror(Movie):
    def play(self):
        print(f"Включаем фильм ужасов '{self.title}' реж. {self.director}.")

class Action(Movie):
    def play(self):
        print(f"Включаем боевик '{self.title}' реж. {self.director}.")

class Romance(Movie):
    def play(self):
        print(f"Включаем мелодраму '{self.title}' реж. {self.director}.")

class Drama(Movie):
    def play(self):
        print(f"Включаем драму '{self.title}' реж. {self.director}.")

class Comedy(Movie):
    def play(self):
        print(f"Включаем комедию '{self.title}' реж. {self.director}.")

class FilmCatalogue:
    def __init__(self):
        self.films_list = []

    def add_movie(self, film: Movie):
        self.films_list.append(film)

    def play_all_movies(self):
        for film in self.films_list:
            film.play()

    def search_movies_by_genre(self, genre: type):
        return [film for film in self.films_list if isinstance(film, genre)]

    def play_movies_by_genre(self, genre: type):
        for film in self.search_movies_by_genre(genre):
            film.play()

my_catalogue = FilmCatalogue()

my_catalogue.add_movie(Drama("Крестный отец", "Френсис Ф. Коппола"))
my_catalogue.add_movie(Comedy("Ночные игры", "Джон Фрэнсис Дейли, Джонатан М. Голдштейн"))
my_catalogue.add_movie(Horror("Дракула Брэма Стокера", "Френсис Ф. Коппола"))
my_catalogue.add_movie(Action("Крушение", "Жан-Франсуа Рише"))
my_catalogue.add_movie(Romance("Честная куртизанка", "Маршалл Херсковиц"))

my_catalogue.play_all_movies()

print(f"\nНайдены фильмы ужасов:")
for movie in my_catalogue.search_movies_by_genre(Horror):
    print(movie.title)

print(f"\nЗапускаем фильм из жанра 'Мелодрамы':")
my_catalogue.play_movies_by_genre(Romance)