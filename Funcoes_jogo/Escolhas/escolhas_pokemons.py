import pygame
from Classes import Botao
from listas_objetos import *
from textos_listar import *
from pygame.locals import *
from os import getcwd

diretorio_atual = getcwd()

################################

def verifica_pokemon(digitado:str):
    from ..cadastrar import pokemons_copy
    digitado = digitado.casefold()
    if digitado == "": return
    for p in pokemons_copy:
        if p.get_nome_pokemon().casefold() == digitado:
            return True
    return False

def verifica_treinador(digitado:str):
    from ..cadastrar import treinadores_copy
    digitado = digitado.casefold()
    if digitado == "": return
    for t in treinadores_copy:
        if t.get_nome().casefold() == digitado:
            return True
    return False

pokemons_usados = []

###############################

def escolha_pokemons():
    x = (1366 - 400) / 2
    y = (768 - 100) / 2

    voltar = Botao("voltar", (diretorio_atual + "\imagens\\Botoes\Voltar.png"), x, 560)

    wallpaper_inicio = pygame.image.load(diretorio_atual + '\imagens\Outros\wallpaper inicio.jpg')

    fonte = pygame.font.Font((diretorio_atual + "\\fontes\\7X7PixelizedRegular-35wp.ttf"), size=28)

    fonte_titulo = pygame.font.Font(((diretorio_atual + "\\fontes\\04B_30__.ttf")), size=28)

    seta = pygame.image.load(diretorio_atual + '\imagens\Outros\seta input.png')

    retangulo_teste = pygame.rect.Rect(x, y, 400, 50)

    ativo = False
    texto_digitado = ""
    cor_inativa = pygame.Color('lightskyblue3')
    cor_ativa = pygame.Color((209, 158, 79))
    cor = cor_inativa

    orientacao_input = "Digite o nome do treinador 1!"
    alerta = ""

    contador_palavras = 0

    jogador1 = []
    jogador2 = []

    window = pygame.display.set_mode((1366,768))

    texto_confirmado = ""

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        
            elif event.type == KEYDOWN and ativo:
                if event.key == pygame.K_RETURN:
                    texto_confirmado = texto_digitado
                    texto_digitado = ""
                    contador_palavras += 1

                elif event.key == pygame.K_BACKSPACE:
                    texto_digitado = texto_digitado[:-1]
                else:
                    texto_digitado += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if retangulo_teste.collidepoint(event.pos):
                    ativo = not ativo
                else:
                    ativo = False
                posicao_mouse = pygame.mouse.get_pos()
                if voltar.clicado(posicao_mouse) == (True, "voltar"):
                    return [[], []]

                cor = cor_ativa if ativo else cor_inativa

        window.blit(wallpaper_inicio, (0, 0))

        texto_aparecendo_natela = fonte.render(texto_digitado, True, (255, 255, 255))

        pygame.draw.rect(window, cor, retangulo_teste)

        window.blit(texto_aparecendo_natela, (retangulo_teste.x + 5, retangulo_teste.y + 5))

        retangulo_teste.w = texto_aparecendo_natela.get_width() + 15

        orientacao_input_natela = fonte_titulo.render(orientacao_input, True, (255, 255, 255))
        window.blit(orientacao_input_natela, (200, 200))

        alerta_natela = fonte_titulo.render(alerta, True, (255, 0, 0))
        window.blit(alerta_natela, (0, 400))

        window.blit(seta, (390,y))

        window.blit(voltar.imagem, voltar.rect)

        if contador_palavras == 1 and verifica_treinador(texto_confirmado):
            jogador1.append(texto_confirmado)
            texto_confirmado = ""
            orientacao_input = "Digite o nome do pokemon 1 do jogador"
            alerta = ""
        elif contador_palavras == 1 and verifica_treinador(texto_confirmado) == False:
            alerta = "esse treinador nao foi registrado!"
            texto_confirmado = ""
            contador_palavras -= 1

        if contador_palavras == 2 and verifica_pokemon(texto_confirmado) and texto_confirmado.casefold() not in pokemons_usados:
            jogador1.append(texto_confirmado)
            pokemons_usados.append(texto_confirmado.casefold())
            texto_confirmado = ""
            orientacao_input = "Digite o nome do pokemon 2 do jogador"
            alerta = ""
        elif contador_palavras == 2 and verifica_pokemon(texto_confirmado) == False or texto_confirmado.casefold() in pokemons_usados:
            alerta = "esse pokemon nao foi registrado ou ja foi escolhido!"
            texto_confirmado = ""
            contador_palavras -= 1

        if contador_palavras == 3 and verifica_pokemon(texto_confirmado) and texto_confirmado.casefold() not in pokemons_usados:
            jogador1.append(texto_confirmado)
            pokemons_usados.append(texto_confirmado.casefold())
            texto_confirmado = ""
            orientacao_input = "Digite o nome do pokemon 3 do jogador"
            alerta = ""
        elif contador_palavras == 3 and verifica_pokemon(texto_confirmado) == False or texto_confirmado.casefold() in pokemons_usados:
            alerta = "esse pokemon nao foi registrado ou ja foi escolhido!"
            texto_confirmado = ""
            contador_palavras -= 1

        if contador_palavras == 4 and verifica_pokemon(texto_confirmado) and texto_confirmado.casefold() not in pokemons_usados:
            jogador1.append(texto_confirmado)
            pokemons_usados.append(texto_confirmado.casefold())
            texto_confirmado = ""
            orientacao_input = "Digite o nome do treinador 2!"
            alerta = ""
        elif contador_palavras == 4 and verifica_pokemon(texto_confirmado) == False or texto_confirmado.casefold() in pokemons_usados:
            alerta = "esse pokemon nao foi registrado ou ja foi escolhido!"
            texto_confirmado = ""
            contador_palavras -= 1
        
        if contador_palavras == 5 and verifica_treinador(texto_confirmado) and texto_confirmado.casefold() not in pokemons_usados:
            jogador2.append(texto_confirmado)
            pokemons_usados.append(texto_confirmado.casefold())
            texto_confirmado = ""
            orientacao_input = "Digite o nome do pokemon 1 do jogador"
            alerta = ""
        elif contador_palavras == 5 and verifica_treinador(texto_confirmado) == False:
            alerta = "esse treinador nao foi registrado!"
            texto_confirmado = ""
            contador_palavras -= 1
        
        if contador_palavras == 6 and verifica_pokemon(texto_confirmado) and texto_confirmado.casefold() not in pokemons_usados:
            jogador2.append(texto_confirmado)
            pokemons_usados.append(texto_confirmado.casefold())
            texto_confirmado = ""
            orientacao_input = "Digite o nome do pokemon 2 do jogador"
            alerta = ""
        elif contador_palavras == 6 and verifica_pokemon(texto_confirmado) == False or texto_confirmado.casefold() in pokemons_usados:
            alerta = "esse pokemon nao foi registrado ou ja foi escolhido!"
            texto_confirmado = ""
            contador_palavras -= 1

        if contador_palavras == 7 and verifica_pokemon(texto_confirmado) and texto_confirmado.casefold() not in pokemons_usados:
            jogador2.append(texto_confirmado)
            pokemons_usados.append(texto_confirmado.casefold())
            texto_confirmado = ""
            orientacao_input = "Digite o nome do pokemon 3 do jogador"
            alerta = ""
        elif contador_palavras == 7 and verifica_pokemon(texto_confirmado) == False or texto_confirmado.casefold() in pokemons_usados:
            alerta = "esse pokemon nao foi registrado ou ja foi escolhido!"
            texto_confirmado = ""
            contador_palavras -= 1

        if contador_palavras == 8 and verifica_pokemon(texto_confirmado) and texto_confirmado.casefold() not in pokemons_usados:
            jogador2.append(texto_confirmado)
            pokemons_usados.append(texto_confirmado.casefold())
            texto_confirmado = ""
            orientacao_input = ""
            alerta = ""
            return [jogador1, jogador2]
        elif contador_palavras == 8 and verifica_pokemon(texto_confirmado) == False or texto_confirmado.casefold() in pokemons_usados:
            alerta = "esse pokemon nao foi registrado ou ja foi escolhido!"
            texto_confirmado = ""
            contador_palavras -= 1

        pygame.display.update()