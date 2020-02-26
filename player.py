import os.path
import sys

if sys.version_info[0] < 3:
    sys.path.append(os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'Lib', 'python2'))
    import pygame
else:
    sys.path.append(os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'Lib', 'python3'))
    import pygame


this = sys.modules[__name__]


class Player(object):

    def __init__(self):
        self.volume = 100
        # initially the music is OFF
        self.music_playing = False
        # init all the sound stuff
        # give myself a large buffer, as well (last value), otherwise playback stutters
        pygame.mixer.init(44100, -16, True, 4096)

    def start_next_song(self, file_name):
        # turn of song events...
        pygame.mixer.music.set_endevent()
        pygame.mixer.music.load(file_name)
        # when new music is loaded, the volume param is reset. Fix it
        pygame.mixer.music.set_volume((float)((float)(self.volume) / 100.0))
        pygame.mixer.music.play()
        # set an endevent to catch it
        pygame.mixer.music.set_endevent(SONG_END)
        self.music_playing = True
        return True

    def set_volume(self, new_volume):
        """Sets and inits new volume level"""
        # must be within range 0-100
        if new_volume < 0:
            self.volume = 0
        elif new_volume > 100:
            self.volume = 100
        else:
            self.volume = new_volume
        pygame.mixer.music.set_volume((float)((float)(self.volume) / 100.0))
        return True

    def get_volume(self):
        """Returns value of current volume"""
        return self.volume

    def stop_music(self):
        """Simply stops the current music"""
        # turn off events as well
        pygame.mixer.music.set_endevent()
        pygame.mixer.music.pause()
        self.music_playing = False
        return True

    def start_music(self):
        """Turns music back on"""
        pygame.mixer.music.set_endevent(SONG_END)
        pygame.mixer.music.unpause()
        self.music_playing = True
        return True

    def get_pos(self):
        pos = pygame.mixer.music.get_pos()
        return pos


SONG_END = 2514
player = Player()
