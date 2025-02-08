import random

class MusicAlbum:
    def __init__(self, title: str, artist: str, release_year: int, genre: str, tracklist: list):
        self.title = title  
        self.artist = artist  
        self.release_year = release_year 
        self.genre = genre  
        self.tracklist = tracklist

    def play_random_track(self):
        random_track_number = random.randint(1, len(self.tracklist)) 
        random_track = self.tracklist[random_track_number - 1] 
        print(f"Воспроизводится трек {random_track_number}: {random_track}")

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