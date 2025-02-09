#Из модуля random импортируем функцию randint для выбора случайного порядкого номера трека в альбоме
from random import randint

class MusicAlbum:
    """Класс, представляющий музыкальный альбом.

    Этот класс позволяет хранить информацию о музыкальном альбоме, включая название,
    исполнителя, год выпуска, жанр и список треков. Также предоставляет метод для
    воспроизведения случайного трека из альбома.

    Attributes:
        title (str): Название альбома
        artist (str): Исполнитель или группа
        release_year (int): Год выпуска альбома
        genre (str): Жанр альбома
        tracklist (list): Список треков в альбоме
    """

    def __init__(self, title: str, artist: str, release_year: int, genre: str, tracklist: list):
        """Инициализирует экземляр класса MusicAlbum

        Args:
            title (str): Название альбома
            artist (str): Автор
            release_year (int): Год выпуска
            genre (str): Жанр
            tracklist (list): Список треков в альбоме

        Raises:
            ValueError: Невалидное значение.
        """

        if not(isinstance(title, str) and isinstance(artist, str) and isinstance(release_year, int) 
            and isinstance(genre, str) and isinstance(tracklist, list)):
            raise ValueError("Вы ввели невалидные значения")

        self.title = title  
        self.artist = artist  
        self.release_year = release_year 
        self.genre = genre  
        self.tracklist = tracklist

    def play_random_track(self):
        """Включает случайный трек из альбома
        """

        random_track_number = randint(1, len(self.tracklist)) 
        random_track = self.tracklist[random_track_number - 1] 
        print(f"Воспроизводится трек {random_track_number}: {random_track}")


#Проверяем работу программы
album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte", 
                    ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex", 
                     "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo", 
                     "Hallomann"])

print("Название:", album4.title)
print("Исполнитель:", album4.artist)
print("Год:", album4.release_year)
print("Жанр:", album4.genre)
print("Треки:", album4.tracklist)

album4.play_random_track()