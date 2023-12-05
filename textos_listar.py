from listas_objetos import *

texto_legenda_pokemon = f"Nome:\nHP:\nSpeed:\nTipo 1:\nTipo 2:"

def texto_informacoes_pokemons(texto:int, pokemons:list):
    texto1 = ""
    texto2 = ""
    texto3 = ""

    nomes = ""
    hp_totais = ""
    velocidades = ""
    tipos1 = ""
    tipos2 = ""
    largura = 12

    for p in range (0, 10):
        nomes += f"{pokemons[p].get_nome_pokemon():<{largura}}"
        hp_totais += f"{pokemons[p].get_hptotal():<{largura}}"
        velocidades += f"{pokemons[p].get_velocidade():<{largura}}"
        tipos1 += f"{pokemons[p].get_tipo1():<{largura}}"
        tipos2 += f"{pokemons[p].get_tipo2():<{largura}}"

    texto1 = f"{nomes}\n{hp_totais}\n{velocidades}\n{tipos1}\n{tipos2}"

    nomes = ""
    hp_totais = ""
    velocidades = ""
    tipos1 = ""
    tipos2 = ""

    for p in range (19, 9, -1):
        nomes += f"{pokemons[p].get_nome_pokemon():<{largura}}"
        hp_totais += f"{pokemons[p].get_hptotal():<{largura}}"
        velocidades += f"{pokemons[p].get_velocidade():<{largura}}"
        tipos1 += f"{pokemons[p].get_tipo1():<{largura}}"
        tipos2 += f"{pokemons[p].get_tipo2():<{largura}}"

    texto2 = f"{nomes}\n{hp_totais}\n{velocidades}\n{tipos1}\n{tipos2}"

    nomes = ""
    hp_totais = ""
    velocidades = ""
    tipos1 = ""
    tipos2 = ""

    if len(pokemons) > 20:
        for p in range (20, (len(pokemons))):
            nomes += f"{pokemons[p].get_nome_pokemon():<{largura}}"
            hp_totais += f"{pokemons[p].get_hptotal():<{largura}}"
            velocidades += f"{pokemons[p].get_velocidade():<{largura}}"
            tipos1 += f"{pokemons[p].get_tipo1():<{largura}}"
            tipos2 += f"{pokemons[p].get_tipo2():<{largura}}"

        texto3 = f"{nomes}\n{hp_totais}\n{velocidades}\n{tipos1}\n{tipos2}"

    match texto:
        case 1: return texto1
        case 2: return texto2
        case 3: return texto3

texto_legenda_treinador = f"Nome:\nIdade:\nEquipe:\nRegião:\nOrientador:"

def texto_informacoes_treinadores(treinadores:list):
    texto = ""
    nomes = ""
    idades = ""
    regiao = ""
    equipes = ""
    orientador = ""
    largura = 12

    for t in treinadores:
        nomes += f"{t.get_nome():<{largura}}"
        idades += f"{t.get_idade():<{largura}}"
        equipes += f"{t.get_equipe():<{largura}}"
        regiao += f"{t.get_regiao():<{largura}}"
        orientador += f"{t.get_orientador():<{largura}}"

    texto = f"{nomes}\n{idades}\n{equipes}\n{regiao}\n{orientador}"

    return texto