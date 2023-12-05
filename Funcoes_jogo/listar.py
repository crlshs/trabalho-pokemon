import pygame
from Classes import Botao
from textos_listar import *
from pygame.locals import *
from os import getcwd
from .cadastrar import pokemons_copy, treinadores_copy

diretorio_atual = getcwd()

####################################################

def listar_pokemons_treinadores():

    pygame.font.init()

    wallpaper_inicio = pygame.image.load(diretorio_atual + '\imagens\Outros\wallpaper inicio.jpg')

    fonte = pygame.font.Font((diretorio_atual + "\\fontes\\7X7PixelizedRegular-35wp.ttf"), size=14)

    fonte_titulo = pygame.font.Font((diretorio_atual + "\\fontes\\04B_30__.ttf"), size=48)

    fundo_lista_pokemons = pygame.image.load(diretorio_atual + "\imagens\Outros\Fundo lista pokemons.png")

    fundo_lista_treinadores = pygame.image.load(diretorio_atual + "\imagens\Outros\Fundo lista treinadores.png")

    pokemons_1 = [fonte.render(linha, True, (255, 255, 255)) for linha in texto_informacoes_pokemons(1, pokemons_copy).split("\n")]

    pokemons_2 = [fonte.render(linha, True, (255, 255, 255)) for linha in texto_informacoes_pokemons(2, pokemons_copy).split("\n")]

    pokemons_3 = [fonte.render(linha, True, (255, 255, 255)) for linha in texto_informacoes_pokemons(3, pokemons_copy).split("\n")]
    
    texto_treinadores = [fonte.render(linha, True, (255, 255, 255)) for linha in texto_informacoes_treinadores(treinadores_copy).split("\n")]

    texto_titulo_pokemon = fonte_titulo.render("Pokemons", True, color=(0, 0, 0))
    texto_titulo_treinadores = fonte_titulo.render("Treinadores", True, color=(0, 0, 0))

    legenda_pokemons = [fonte.render(linha, True, color=(255,255,255)) for linha in texto_legenda_pokemon.split("\n")]
    legenda_treinadores = [fonte.render(linha, True, color=(255, 255, 255)) for linha in texto_legenda_treinador.split("\n")]

    voltar = Botao("voltar", (diretorio_atual + "\imagens\Botoes\Voltar.png"), ((1366 - 400) / 2), 560)

    rodando = True

    window = pygame.display.set_mode((1366,768))

    while rodando:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posicao_mouse = pygame.mouse.get_pos()
                if voltar.clicado(posicao_mouse) == (True, "voltar"):
                        rodando = False
                        break

            # desenha as imagens na tela - wallpaper e fundos lista
            window.blit(wallpaper_inicio, (0, 0))
            window.blit(fundo_lista_pokemons, (0, 60))
            window.blit(fundo_lista_treinadores, (0, 420))

            for i, line in enumerate(legenda_pokemons):
                window.blit(line, (0, 60 + i*14))
                window.blit(line, (0, 150 + i*14))
                window.blit(line, (0, 240 + i*14))

            # desenhando os textos na tela
            for i, line in enumerate(legenda_treinadores):
                window.blit(line, (0, 430 + i*14))

            for i, line in enumerate(texto_treinadores):
                window.blit(line, (135, 430 + i*14))

            for i, line in enumerate(pokemons_1):
                window.blit(line, (100, 60 + i*14))

            for i, line in enumerate(pokemons_2):
                window.blit(line, (100, 150 + i*14))

            for i, line in enumerate(pokemons_3):
                window.blit(line, (100, 240 + i*14))    

            window.blit(texto_titulo_pokemon, (((1366 - 400) / 2),0))
            window.blit(texto_titulo_treinadores, (((1366 - 400) / 2),360))

            # desenha o botão de voltar na tela
            window.blit(voltar.imagem, voltar.rect)

        pygame.display.update()