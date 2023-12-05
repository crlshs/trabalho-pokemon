from .animal import Animal
from pygame import mixer_music

class Musica(Animal):
    def __init__(self, nome_musica:str, diretorio:str):
        super().__init__(nome_musica)
        self._diretorio = diretorio

    def get_diretorio(self):
        return self._diretorio

    def get_surface(self):
        return mixer_music.load(self._diretorio)