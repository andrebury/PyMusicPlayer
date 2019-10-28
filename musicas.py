import pygame
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH


class musicas:

    def __init__(self):
        pygame.mixer.init()

        # realdir = os.path.realpath(listofsongs[index])
        # audio = ID3(realdir)
        # print(audio['TIT2'].text[0])
        # print(audio)


    def nextsong(self, listofsongs, index):
        self.paraamusica()
        pygame.mixer.music.load(listofsongs[index])

        pygame.mixer.music.play()
        print("next")

    def prevsong(self, listofsongs, index):
        self.paraamusica()
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()

    def stopsong(self):
        pygame.mixer.music.pause()

    def playsong(self, listofsongs, index):
        if pygame.mixer.music.get_busy() == 1:
            pygame.mixer.music.unpause()
        else:
            self.paraamusica()
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()

    def paraamusica(self):
        pygame.mixer.music.stop()
    

    def salvaID3(self, artista, album, titulo, musicaatual):
        try:
            mp3 = MP3File(musicaatual)
            mp3.artist = artista
            mp3.song = titulo
            mp3.album = album
            print(artista + ' - ' + album + ' ' + ' ' + titulo)
            mp3.save()
            
        except Exception as inst:
            print(type(inst))            
            print(artista + ' - ' + album + ' ' + ' ' + titulo)


    def pegaTagsID3(self, musicaatual):

        try:
            print("entrando na pegatagsid3 " + musicaatual)
            mp3 = MP3File(musicaatual)
            tags = mp3.get_tags()            
            return tags

        except:
            print("erro")
            # tag = mutagen.File(listofsongs[index], easy=True)
            # tag.add_tags()