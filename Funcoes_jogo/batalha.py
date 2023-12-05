import pygame
import moviepy.editor
from Classes import BotaoAtaque
from .cadastrar import treinadores_copy, pokemons_copy
from .Escolhas import escolhas_pokemons as ep
from listas_objetos import *
from textos_listar import *
from pygame.locals import *
from os import getcwd
from random import choice
from time import sleep

diretorio_atual = getcwd()

wallpaper = pygame.image.load(diretorio_atual + '\imagens\Outros\\fundo batalha.png')

##############

def batalha():
    jogadores = ep.escolha_pokemons()
    jogador1 = jogadores[0]
    jogador2 = jogadores[1]
    if jogador1 == [] : return

    # pokemons treinadores
    for i in treinadores_copy:
        if i.get_nome().casefold() == jogador1[0].casefold(): treinador1 = i
        elif i.get_nome().casefold() == jogador2[0].casefold(): treinador2 = i

    for i in pokemons_copy:
        if i.get_nome_pokemon().casefold() == jogador1[1]: pokemon1_t1 = i
        if i.get_nome_pokemon().casefold() == jogador1[2]: pokemon2_t1 = i
        if i.get_nome_pokemon().casefold() == jogador1[3]: pokemon3_t1 = i

        if i.get_nome_pokemon().casefold() == jogador2[1]: pokemon1_t2 = i
        if i.get_nome_pokemon().casefold() == jogador2[2]: pokemon2_t2 = i
        if i.get_nome_pokemon().casefold() == jogador2[3]: pokemon3_t2 = i

    jogador1 = [treinador1, pokemon1_t1, pokemon2_t1, pokemon3_t1]

    jogador2 = [treinador2, pokemon1_t2, pokemon2_t2, pokemon3_t2]

    for i in range(1, len(jogador1)):
        jogador1[i].reset_hp()
    for i in range(1, len(jogador2)):
        jogador2[i].reset_hp()


    # quem joga primeira
    pokemon_atual_t1 = jogador1[1]
    pokemon_atual_t2 = jogador2[1]

    if int(jogador1[1].get_velocidade()) >=  int(jogador2[1].get_velocidade()): jogando = pokemon_atual_t1

    elif int(jogador1[1].get_velocidade()) <  int(jogador2[1].get_velocidade()): jogando = pokemon_atual_t2

    informacoes_t1 = treinador1.__str__()
    informacoes_t2 = treinador2.__str__()

    texto_evento = "!"
    vez_de = f"Vez de {jogando}!"

    # botoes de ataque
    basico1_p1 = BotaoAtaque("basico1_p1", diretorio_atual + '\imagens\Botoes\Basico 1.png', 0, 440, True)
    basico2_p1 = BotaoAtaque("basico1_p1", diretorio_atual + '\imagens\Botoes\Basico 2.png', 151, 440, False)
    ultimate_p1 = BotaoAtaque("ultimate_p1", diretorio_atual + r'\imagens\Botoes\Ultimate.png', 0, 768-200, False)

    basico1_p2 = BotaoAtaque("basico1_p2", diretorio_atual + '\imagens\Botoes\Basico 1.png', 1066, 440, True)
    basico2_p2 = BotaoAtaque("basico2_p2", diretorio_atual + '\imagens\Botoes\Basico 2.png', 1216, 440, False)
    ultimate_p2 = BotaoAtaque("ultimate_p1", diretorio_atual + r'\imagens\Botoes\Ultimate.png', 1066, 768-200, False)

    # jogadas dos treinadores
    jogadast1 = 0
    jogadast2 = 0

    # textos
    chance_critico = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    chance_errar = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]

    # funcao
    def acabou(quem_ganhou:int):
        if quem_ganhou == 2:
            pokemon_esquerda = pygame.image.load(diretorio_atual + f'\imagens\\Pokemons\\falecido.png')
            tela.blit(pokemon_esquerda, (310,y+321))
            vez_de = f"{treinador2.get_nome()} venceu!"
            vez = fonte_titulo.render(vez_de, True, (255, 0, 0))
            tela.blit(vez, ((683-vez.get_width()/2), 200))
            pygame.display.update()

        elif quem_ganhou == 1:
            pokemon_direita = pygame.image.load(diretorio_atual + f'\imagens\\Pokemons\\falecido.png')
            tela.blit(pokemon_direita, (766,y+321))
            vez_de = f"{treinador1.get_nome()} venceu!"
            vez = fonte_titulo.render(vez_de, True, (255, 0, 0))
            tela.blit(vez, ((683-vez.get_width()/2), 200))
            pygame.display.update()

        pygame.mixer.music.load(diretorio_atual + "\\audio\\vitoria.mp3")
        pygame.mixer.music.play()
        sleep(5)
        return ep.pokemons_usados.clear()

    fonte = pygame.font.Font((diretorio_atual + "\\fontes\\7X7PixelizedRegular-35wp.ttf"), size=16)

    fonte_titulo = pygame.font.Font(((diretorio_atual + "\\fontes\\04B_30__.ttf")), size=32)

    titulo_batalha = f"{treinador1.get_nome()} x {treinador2.get_nome()}"

    y = (768 - 600) / 2

    #musica batalha
    pygame.mixer.init()
    song = choice(musicas_batalha)
    pygame.mixer.music.load(song.get_diretorio())
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()

    #transicao para batalha
    video = moviepy.editor.VideoFileClip(diretorio_atual + "\\video\\transição batalha.mp4")
    video.preview()

    tela = pygame.display.set_mode((1366,768))

    texto_evento = "!"

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            dano_basico1_t1 = pokemon_atual_t1.get_danobasico1()
            dano_basico2_t1 = pokemon_atual_t1.get_danobasico2()
            ultimate_t1 = pokemon_atual_t1.get_ultimate()

            dano_basico1_t2 = pokemon_atual_t2.get_danobasico1()
            dano_basico2_t2 = pokemon_atual_t2.get_danobasico2()
            ultimate_t2 = pokemon_atual_t2.get_ultimate()

            ###########################
            if jogadast1 >=  2:
                basico2_p1.podeusar = True
            if jogadast2 >=  2:
                basico2_p2.podeusar = True

            if jogadast1 >=  4:
                ultimate_p1.podeusar = True 
            if jogadast2 >=  4:             
                ultimate_p2.podeusar = True
            #################################

            if event.type == pygame.USEREVENT:
                song = choice(musicas_batalha)
                pygame.mixer.music.load(song.get_diretorio())
                pygame.mixer.music.play()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if basico1_p1.clicado(posicao_mouse) and jogando == pokemon_atual_t1:
                    jogadast1 += 1
                    if choice(chance_errar) == 1:
                        texto_evento = f"{treinador1.get_nome()} errou!"
                    else:
                        if choice(chance_critico) == 1:
                            pokemon_atual_t2.set_hpatual(dano_basico1_t1 + 30)
                            texto_evento = f"{treinador1.get_nome()} acertou um critico!"
                        else:
                            pokemon_atual_t2.set_hpatual(dano_basico1_t1)
                            texto_evento = f"{treinador1.get_nome()} acertou com exito!"

                    jogando = pokemon_atual_t2

                    if pokemon_atual_t2.get_hpatual() <= 0:
                        jogadast2 = 0
                        del jogador2[1]
                        if len(jogador2) >= 2:
                            pokemon_atual_t2 = jogador2[1]
                            basico2_p2.podeusar = False
                            ultimate_p2.podeusar = False
                            jogando = pokemon_atual_t2
                        else:
                            acabou(1)
                            return

                if basico1_p2.clicado(posicao_mouse) and jogando == pokemon_atual_t2:
                    jogadast2 += 1
                    if choice(chance_errar) == 1:
                        texto_evento = f"{treinador2.get_nome()} errou!"
                    else:
                        if choice(chance_critico) == 1:
                            pokemon_atual_t1.set_hpatual(dano_basico1_t2 + 30)
                            texto_evento = f"{treinador2.get_nome()} acertou um critico!"
                        else:
                            pokemon_atual_t1.set_hpatual(dano_basico1_t2)
                            texto_evento = f"{treinador2.get_nome()} acertou com exito!"
                    jogando = pokemon_atual_t1

                    if pokemon_atual_t1.get_hpatual() <= 0:
                        jogadast1 = 0
                        del jogador1[1]
                        if len(jogador1) >= 2:
                            pokemon_atual_t1 = jogador1[1]
                            basico2_p1.podeusar = False
                            ultimate_p1.podeusar = False
                            jogando = pokemon_atual_t1
                        else:
                            acabou(2)
                            return

                if basico2_p1.clicado(posicao_mouse) and jogando == pokemon_atual_t1 and basico2_p1.podeusar == True:
                    jogadast1 += 1
                    if choice(chance_errar) == 1:
                        texto_evento = f"{treinador1.get_nome()} errou!"
                    else:
                        if choice(chance_critico) == 1:
                            pokemon_atual_t2.set_hpatual(dano_basico2_t1 + 30)
                            texto_evento = f"{treinador1.get_nome()} acertou um critico!"
                        else:
                            pokemon_atual_t2.set_hpatual(dano_basico2_t1)
                            texto_evento = f"{treinador1.get_nome()} acertou com exito!"
                    jogando = pokemon_atual_t2

                    if pokemon_atual_t2.get_hpatual() <= 0:
                        jogadast2 = 0
                        del jogador2[1]
                        if len(jogador2) >= 2:
                            pokemon_atual_t2 = jogador2[1]
                            basico2_p2.podeusar = False
                            ultimate_p2.podeusar = False
                            jogando = pokemon_atual_t2
                        else:
                            acabou(1)
                            return

                if basico2_p2.clicado(posicao_mouse) and jogando == pokemon_atual_t2 and basico2_p2.podeusar == True:
                    jogadast2 += 1
                    if choice(chance_errar) == 1:
                        texto_evento = f"{treinador2.get_nome()} errou!"
                    else:
                        if choice(chance_critico) == 1:
                            pokemon_atual_t1.set_hpatual(dano_basico2_t2 + 30)
                            texto_evento = f"{treinador2.get_nome()} acertou um critico!"
                        else:
                            pokemon_atual_t1.set_hpatual(dano_basico2_t2)
                            texto_evento = f"{treinador2.get_nome()} acertou com exito!"
                    jogando = pokemon_atual_t1

                    if pokemon_atual_t1.get_hpatual() <= 0:
                        jogadast1 = 0
                        del jogador1[1]
                        if len(jogador1) >= 2:
                            pokemon_atual_t1 = jogador1[1]
                            basico2_p1.podeusar = False
                            ultimate_p1.podeusar = False
                            jogando = pokemon_atual_t1
                        else:
                            acabou(2)
                            return

                if ultimate_p1.clicado(posicao_mouse) and jogando == pokemon_atual_t1 and ultimate_p1.podeusar == True:
                    jogadast1 += 1
                    if choice(chance_errar) == 1:
                        texto_evento = f"{treinador1.get_nome()} errou!"
                    else:
                        if choice(chance_critico) == 1:
                            pokemon_atual_t2.set_hpatual(ultimate_t1 + 30)
                            texto_evento = f"{treinador1.get_nome()} acertou um critico!"
                        else:
                            pokemon_atual_t2.set_hpatual(ultimate_t1)
                            texto_evento = f"{treinador1.get_nome()} acertou com exito!"
                    jogando = pokemon_atual_t2

                    if pokemon_atual_t2.get_hpatual() <= 0:
                        jogadast2 = 0
                        del jogador2[1]
                        if len(jogador2) >= 2:
                            pokemon_atual_t2 = jogador2[1]
                            basico2_p2.podeusar = False
                            ultimate_p2.podeusar = False
                            jogando = pokemon_atual_t2
                        else:
                            acabou(1)
                            return

                if ultimate_p2.clicado(posicao_mouse) and jogando == pokemon_atual_t2 and ultimate_p2.podeusar == True:
                    jogadast2 += 1
                    if choice(chance_errar) == 1:
                        texto_evento = f"{treinador2.get_nome()} errou!"
                    else:
                        if choice(chance_critico) == 1:
                            pokemon_atual_t1.set_hpatual(ultimate_t2 + 30)
                            texto_evento = f"{treinador2.get_nome()} acertou um critico!"
                        else:
                            pokemon_atual_t1.set_hpatual(ultimate_t2)
                            texto_evento = f"{treinador2.get_nome()} acertou com exito!"
                    jogando = pokemon_atual_t1

                    if pokemon_atual_t1.get_hpatual() <= 0:
                        jogadast1 = 0
                        del jogador1[1]
                        if len(jogador1) >= 2:
                            pokemon_atual_t1 = jogador1[1]
                            basico2_p1.podeusar = False
                            ultimate_p1.podeusar = False
                            jogando = pokemon_atual_t1
                        else:
                            acabou(2)
                            return

        posicao_mouse = pygame.mouse.get_pos()

        video.close()

        # atualizacoes
        pokemon_atual_t1 = jogador1[1]
        pokemon_atual_t2 = jogador2[1]

        # vidas pokemons
        vida_treinador1 = f"Hp {pokemon_atual_t1.get_nome_pokemon()}: {pokemon_atual_t1.get_hpatual()}"
        vida_treinador2 = f"Hp {pokemon_atual_t2.get_nome_pokemon()}: {pokemon_atual_t2.get_hpatual()}"

        vida_treinador1_natela = fonte.render(vida_treinador1, True, (0, 0, 0), bgcolor=(255, 255, 255))
        vida_treinador2_natela = fonte.render(vida_treinador2, True, (0, 0, 0), bgcolor= (255, 255, 255))
        evento_natela = fonte.render(texto_evento, True, (255, 255, 255))
        vez = fonte_titulo.render(vez_de, True, (255, 0, 0))

        if pokemon_atual_t2 in pokemons: pokemon_direita = pygame.image.load(diretorio_atual + f'\imagens\\Pokemons\{pokemon_atual_t2.get_nome_pokemon()} direita.png')
        else: pokemon_direita = pygame.image.load(diretorio_atual + f'\imagens\\Pokemons\Indefinido.png')

        if pokemon_atual_t1 in pokemons: pokemon_esquerda = pygame.image.load(diretorio_atual + f'\imagens\\Pokemons\{pokemon_atual_t1.get_nome_pokemon()} esquerda.png')
        else: pokemon_esquerda = pygame.image.load(diretorio_atual + f'\imagens\\Pokemons\Indefinido.png')

        # funcao para pegar as habilidades dos pokemons atuais
        def habilidades_atuais():
            habilidades_p1 = ""
            for chave, valor in pokemon_atual_t1.get_ataques().items():
                habilidades_p1 += f"{chave} - {valor}\n"
            habilidades_p1 = habilidades_p1[:-1]

            habilidades_p2 = ""
            for chave, valor in pokemon_atual_t2.get_ataques().items():
                habilidades_p2 += f"{chave} - {valor}\n"
            habilidades_p2 = habilidades_p2[:-1]

            return [habilidades_p1, habilidades_p2]

        habilidade_p1 = habilidades_atuais()[0]
        habilidade_p2 = habilidades_atuais()[1]

        habilidades_p1_natela = [fonte.render(linha, True, (0, 0, 0), (209, 158, 79)) for linha in habilidades_atuais()[0].split("\n")]

        habilidades_p2_natela = [fonte.render(linha, True, (0, 0, 0), (209, 158, 79)) for linha in habilidades_atuais()[1].split("\n")]

        # informacoes treinadores
        imagem_t1 = pygame.image.load(treinador1.get_imagem())
        imagem_t2 = pygame.image.load(treinador2.get_imagem())

        # blits #
        tela.blit(wallpaper, (0,0))
        tela.blit(pokemon_esquerda, (310,y+321))
        tela.blit(pokemon_direita, (766,y+321))

        tela.blit(vida_treinador1_natela, (310, y+250))
        tela.blit(vida_treinador2_natela, (766, y+250))
    
        vez_de = f"Vez de {jogando}!"
        tela.blit(evento_natela, ((683-evento_natela.get_width()/2), 750))
        tela.blit(vez, ((683-vez.get_width()/2), 100))

        informacoes_t1_natela = [fonte.render(linha, True, (255, 255, 255)) for linha in informacoes_t1.split("\n")]

        informacoes_t2_natela = [fonte.render(linha, True, (255, 255, 255)) for linha in informacoes_t2.split("\n")]

        titulo_natela = fonte_titulo.render(titulo_batalha, True, (255, 255, 255))

        for i, line in enumerate(habilidades_p1_natela):
            tela.blit(line, (0, 715-line.get_height() + i*18))

        for i, line in enumerate(habilidades_p2_natela):
            tela.blit(line, (1036, 715-line.get_height() + i*18))
        tela.blit(titulo_natela, ((683-titulo_natela.get_width()/2), 0))

        for i, line in enumerate(informacoes_t1_natela):
            tela.blit(line, (100, 0 + i*14))
        
        for i, line in enumerate(informacoes_t2_natela):
            tela.blit(line, (1000, 0 + i*14))

        tela.blit(imagem_t1, (0, 0))
        tela.blit(imagem_t2, (1266, 0))

        tela.blit(basico1_p1.imagem, basico1_p1.rect)
        tela.blit(basico2_p1.imagem, basico2_p1.rect)
        tela.blit(ultimate_p1.imagem, ultimate_p1.rect)

        tela.blit(basico1_p2.imagem, basico1_p2.rect)
        tela.blit(basico2_p2.imagem, basico2_p2.rect)
        tela.blit(ultimate_p2.imagem, ultimate_p2.rect)

        pygame.display.update()