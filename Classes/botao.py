import pygame

class Botao:
    def __init__(self, nome_botao:str, diretorio:str, x:int, y:int):
        self.nome_botao = nome_botao
        self.imagem = pygame.image.load(diretorio)
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)

    def clicado(self, posicao_mouse):
        return self.rect.collidepoint(posicao_mouse), self.nome_botao