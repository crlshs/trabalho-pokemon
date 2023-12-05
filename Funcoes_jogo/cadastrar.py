import pygame
from Classes import Treinador, Pokemon, Botao
from .Escolhas import escolhas_cadastro as ec
from listas_objetos import *
from textos_listar import *
from pygame.locals import *
from os import getcwd
from time import sleep

pokemons_copy = []
treinadores_copy = []
for i in pokemons: pokemons_copy.append(i)
for i in treinadores: treinadores_copy.append(i)

diretorio_atual = getcwd()

#################################################

def cadastrar_pokemon():
    rodando = True

    x = (1366 - 400) / 2
    y = (768 - 100) / 2

    fonte = pygame.font.Font((diretorio_atual + "\\fontes\\7X7PixelizedRegular-35wp.ttf"), size=28)

    fonte_titulo = pygame.font.Font(((diretorio_atual + "\\fontes\\04B_30__.ttf")), size=28)

    wallpaper_inicio = pygame.image.load(diretorio_atual + '\imagens\Outros\wallpaper inicio.jpg')

    seta = pygame.image.load(diretorio_atual + '\imagens\Outros\seta input.png')

    retangulo_input = pygame.rect.Rect(x, y, 400, 50)

    ativo = False
    texto_digitado = ""
    cor_inativa = pygame.Color('lightskyblue3')
    cor_ativa = pygame.Color((209, 158, 79))
    cor = cor_inativa

    contador_palavras = 0

    treinador_adicionar = []
    pokemon_adicionar = []

    escolha = ec.escolha_cadastro()

    if escolha == "adicionar pokemon":
        modo = "adicionar pokemon"
        orientacao_input = "Digite o nome do Pokemon!"
    elif escolha == "adicionar treinador":
        modo = "adicionar treinador"
        orientacao_input = "Digite o nome do Treinador a ser adicionado!"
    elif escolha == "voltar":
        modo = "voltar"
        orientacao_input = "tchau"
        rodando = False

    window = pygame.display.set_mode((1366,768))

    while rodando:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN and ativo:
                if event.key == pygame.K_RETURN:
                    print(texto_digitado)
                    contador_palavras+=1

                    if modo == "adicionar pokemon":
                        pokemon_adicionar.append(texto_digitado)
                    elif modo == "adicionar treinador":
                        treinador_adicionar.append(texto_digitado)

                    texto_digitado = ''

                elif event.key == pygame.K_BACKSPACE:
                    texto_digitado = texto_digitado[:-1]
                else:
                    texto_digitado += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if retangulo_input.collidepoint(event.pos):
                    ativo = not ativo
                else:
                    ativo = False
                cor = cor_ativa if ativo else cor_inativa

        texto_aparecendo_natela = fonte.render(texto_digitado, True, (255, 255, 255))

        window.blit(wallpaper_inicio, (0, 0))
        pygame.draw.rect(window, cor, retangulo_input)

        window.blit(texto_aparecendo_natela, (retangulo_input.x + 5, retangulo_input.y + 5))

        retangulo_input.w = texto_aparecendo_natela.get_width() + 15

        orientacao_input_natela = fonte_titulo.render(orientacao_input, True, (255, 255, 255))
        window.blit(orientacao_input_natela, (200, 200))

        window.blit(seta, (390,y))

        match modo:
            # caso adicionar pokemon
            case "adicionar pokemon":
                orientacoes = {
                    0: "Digite o nome do pokemon!",
                    1: "Digite o HP do pokemon!",
                    2: "Digite a velocidade do pokemon!",
                    3: "Digite o Tipo 1 do pokemon!",
                    4: "Digite o Tipo 2 do pokemon!",
                    5: "Digite o nome do ataque 1 (basico) do pokemon!",
                    6: "Digite o dano do ataque!",
                    7: "Digite o nome do ataque 2 (basico) do pokemon!",
                    8: "Digite o dano do ataque!",
                    9: "Digite o nome da ultimate do pokemon!",
                    10: "Digite o dano da ultimate!"
                }

                if contador_palavras == 11:
                    print(pokemon_adicionar)

                    nome_ataque_valor_ataque_dict = {
                    pokemon_adicionar[5] : int(pokemon_adicionar[6]),
                    pokemon_adicionar[7] : int(pokemon_adicionar[8]),
                    pokemon_adicionar[9] : int(pokemon_adicionar[10])
                    }

                    p_adicionado = Pokemon(
                            pokemon_adicionar[0],
                            int(pokemon_adicionar[1]),
                            int(pokemon_adicionar[1]),
                            int(pokemon_adicionar[2]),
                            pokemon_adicionar[3],
                            pokemon_adicionar[4],
                            nome_ataque_valor_ataque_dict,
                            (diretorio_atual + '\imagens\Pokemons\Indefinido.png')
                            )

                    pokemons_copy.append(p_adicionado)
                    rodando = False
                    break

                orientacao_input = orientacoes.get(contador_palavras, "")

            # caso adicionar treinador
            case "adicionar treinador":
                orientacoes = {
                    0: "Digite o nome do treinador!",
                    1: "m para masculino - f para feminino!",
                    2: "Digite a idade do treinador!",
                    3: "Digite a região do treinador!",
                    4: "Digite a equipe do treinador!",
                    5: "Digite o orientador do treinador!"
                    }

                if len(treinador_adicionar) > 2:
                    if treinador_adicionar[1] == "m".casefold():
                        imagem_treinador = diretorio_atual + r'\imagens\Treinadores\menino.png'
                    elif treinador_adicionar[1] == "f".casefold():
                        imagem_treinador = diretorio_atual + r'\imagens\Treinadores\menina.png'
                    else:
                        imagem_treinador = diretorio_atual + r'\imagens\Treinadores\neutre.png'


                if contador_palavras == 6:
                    print(treinador_adicionar)
                    t_adionado = Treinador(*treinador_adicionar[:6], imagem_treinador)
                    treinadores_copy.append(t_adionado)
                    rodando = False
                    break

                orientacao_input = orientacoes.get(contador_palavras, "")

        pygame.display.update()