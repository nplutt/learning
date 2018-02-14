class Song(object):
    def __init__(self, name, album):
        self.name = name
        self.album = album


class Album(object):
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist


class Artist(object):
    def __init__(self, name):
        self.name = name


class CD(object):
    def __init__(self, songs=[]):
        self.songs = songs

    def add_song(self, song):
        pass


class Player(object):
    def __init__(self, cd):
        self.cd = cd
        self.song_index = 0
        self.song = self.cd.songs[self.song_index]

    def get_display_info(self):
        pass

    def next_song(self):
        pass

    def previous_song(self):
        pass

    def pause_song(self):
        pass