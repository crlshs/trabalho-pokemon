import pygame
from Classes import Botao
from listas_objetos import *
from textos_listar import *
from pygame.locals import *
from os import getcwd

diretorio_atual = getcwd()

def escolha_cadastro():
    x = (1366 - 400) / 2

    voltar = Botao("voltar", (diretorio_atual + "\imagens\Botoes\Voltar.png"), x, 560)

    wallpaper_inicio = pygame.image.load(diretorio_atual + '\imagens\Outros\wallpaper inicio.jpg')

    adicionar_pokemon = Botao("adicionar pokemon", diretorio_atual + "\imagens\Botoes\Pokemon.png", x, 240)
    adicionar_treinador = Botao("adicionar treinador", diretorio_atual + "\imagens\Botoes\Treinador.png", x, 400)

    botoes = [voltar, adicionar_pokemon, adicionar_treinador]

    window = pygame.display.set_mode((1366,768))

    rodando = True

    while rodando:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                posicao_mouse = pygame.mouse.get_pos()
                for botao in botoes:
                    if botao.clicado(posicao_mouse)[0]:
                        return botao.clicado(posicao_mouse)[1]

        window.blit(wallpaper_inicio, (0, 0))

        for botao in botoes:
            window.blit(botao.imagem, botao.rect)

        pygame.display.update()