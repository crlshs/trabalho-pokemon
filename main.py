import pygame
import moviepy.editor
from pygame.locals import *
from sys import exit
from os import getcwd
from Funcoes_jogo import *
from random import choice
from listas_objetos import musicas_inicio

#get cwd serve para armazenar o diretório do arquivo atual
diretorio_atual = getcwd()
clock = pygame.time.Clock()

pygame.init()

# imagens do jogo #
icone = pygame.image.load(diretorio_atual + '\imagens\Outros\icon.png')
wallpaper_inicio = pygame.image.load(diretorio_atual + '\imagens\Outros\wallpaper inicio.jpg')


# icone e legenda do jogo #
pygame.display.set_icon(icone)
pygame.display.set_caption("Trabalho Pokemon - Carlos, Nicolas & Erica")

# criando os botoes iniciais
x = (1366 - 400) / 2

listar = Botao("listar", (diretorio_atual + "\imagens\Botoes\Listar Pokemons.png"), x-250, 240)
cadastrar = Botao("cadastrar", (diretorio_atual + "\imagens\Botoes\Cadastrar Pokemons.png"), x+250, 240)
batalhar = Botao("batalhar", (diretorio_atual + "\imagens\Botoes\Batalhar.png"), x-250, 450)
sair = Botao("sair", (diretorio_atual + "\imagens\Botoes\Sair.png"), x+250, 450)
botoes = [listar, cadastrar, batalhar, sair]

logo = pygame.image.load(diretorio_atual + "\imagens\Outros\logo.png")

# rodando o vídeo antes de começar o jogo #
video = moviepy.editor.VideoFileClip(diretorio_atual + "\\video\\abertura.mp4")
video.preview()


# iniciar a musica de fundo do jogo #
song = choice(musicas_inicio)
pygame.mixer.init()
pygame.mixer.music.load(song.get_diretorio())
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

tela = pygame.display.set_mode((1366,768))

# loop principal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        video.close()
        tela.blit(wallpaper_inicio, (0,0))
        tela.blit(logo, (x, 10))

        if event.type == pygame.MOUSEBUTTONDOWN:
            posicao_mouse = pygame.mouse.get_pos()
            for botao in botoes:

                if botao.clicado(posicao_mouse) == (True, "listar"):
                    listar_pokemons_treinadores()

                if botao.clicado(posicao_mouse) == (True, "cadastrar"):
                    cadastrar_pokemon()

                if botao.clicado(posicao_mouse) == (True, "batalhar"):
                    batalha()

                if botao.clicado(posicao_mouse) == (True, "sair"):
                    pygame.quit()
                    exit()

        elif event.type == pygame.USEREVENT:
            song = choice(musicas_inicio)
            pygame.mixer.music.load(song.get_diretorio())
            pygame.mixer.music.play()

        for botao in botoes:
            tela.blit(botao.imagem, botao.rect)

    pygame.display.update()
    clock.tick(60)