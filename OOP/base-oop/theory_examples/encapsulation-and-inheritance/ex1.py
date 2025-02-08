# Импортируем модуль random для работы со случайными числами
import random

# Создаем класс MusicAlbum, представляющий музыкальный альбом
class MusicAlbum:
    # Конструктор класса, принимающий название, исполнителя, год выпуска, жанр и список треков
    def __init__(self, title: str, artist: str, release_year: int, genre: str, tracklist: list):
        self.title = title  # Инициализация названия альбома
        self.artist = artist  # Инициализация исполнителя
        self.release_year = release_year  # Инициализация года выпуска
        self.genre = genre  # Инициализация жанра
        self.tracklist = tracklist  # Инициализация списка треков

    # Метод для воспроизведения случайного трека из альбома
    def play_random_track(self):
        # Генерируем случайный номер трека от 1 до количества треков в альбоме
        random_track_number = random.randint(1, len(self.tracklist))
        # Получаем трек по случайному номеру (индекс = номер - 1)
        random_track = self.tracklist[random_track_number - 1]
        # Выводим информацию о воспроизводимом треке
        print(f"Воспроизводится трек {random_track_number}: {random_track}")

# Создаем экземпляр класса MusicAlbum с данными альбома "Deutschland" группы Rammstein
album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte", 
                    ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex", 
                     "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo", 
                     "Hallomann"])

# Выводим информацию о созданном альбоме
print("Название:", album4.title)
print("Исполнитель:", album4.artist)
print("Год:", album4.release_year)
print("Жанр:", album4.genre)
print("Треки:", album4.tracklist)

# Воспроизводим случайный трек из альбома
album4.play_random_track()