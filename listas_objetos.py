from Classes import Treinador, Pokemon, Musica
from os import getcwd

diretorio_atual = getcwd()

# treinadores
Carlos = Treinador("Carlos", "m", 16, "UVA", "2T.I", "Helder", diretorio_atual + r'\imagens\Treinadores\Carlos.jpg')
Nicolas = Treinador("Nicolas", "m", 17, "UVA", "2T.I", "Helder", diretorio_atual + r'\imagens\Treinadores\Nicolas.jpg')
Érica = Treinador("Erica", "f", 17, "UVA", "2T.I", "Helder", diretorio_atual + r'\imagens\Treinadores\Érica.png')

treinadores = [Carlos, Nicolas, Érica]

# pokemons
Chikorita = Pokemon("Chikorita", 45, 45, 45, "Grama", "Grama", {"Minidreno" : 10, "Chicotes de Vinha": 30, "Raio Solar": 70}, "")


Arceus = Pokemon("Arceus", 120, 120, 80, "Normal", "Normal", {"Estrela Tríplica" : 50, "Raio Supremo" : 50, "Super nova Tríplica" : 200}, "")


Mewtwo = Pokemon("Mewtwo", 106, 106, 80, "Psíquico", "Psíquico", {"Choque Psíquico" : 50, "Super Raio Psíquico" : 60, "Pulso Reinante" : 120}, "")


Psyduck = Pokemon("Psyduck", 50, 50, 40, "Aquático", "Aquático", {"Dor de Cabeça" : 10, "Pânico" : 10, "Arranhão" : 50}, "")


Ho_oh = Pokemon("Ho-oh", 106, 106, 60, "Voador", "Fogo", {"Rajada de Fogo" : 45, "Fênix Ardente" : 60, "Chamas Brilhantes" : 160}, "")


Paras = Pokemon("Paras", 35, 35, 20, "Inseto", "Grama", {"Bola de Esporos" : 20, "Arranhar" : 20, "Absorção" : 60}, "")


Butterfree = Pokemon("Butterfree", 60, 60, 50, "Inseto", "Voador", {"Raio Psíquico": 30, "Esporos Atordoantes": 50, "Ataque do Vento" : 80}, "")


Sunflora = Pokemon("Sunflora", 75, 75, 30, "Grama", "Grama", {"Raio Reluzente": 15, "Maldição": 65, "Raio Solar": 70}, "")


Charmander = Pokemon("Charmander", 39, 39, 45, "Fogo", "Fogo", {"Rosnar": 35, "Chama": 49, "Lança-chamas":80}, "")


Pikachu = Pokemon("Pikachu", 15, 15, 70, "Elétrico", "Elétrico", {"Trovão": 40,"Esfera Elétrica": 60, "Choque do Trovão": 90}, "")


Diglett = Pokemon("Diglett", 10, 10, 60, "Grama", "Água", {"Gancho": 10, "Arranhão": 10, "Tapa de Lama": 40}, "")
# vida = 10 - danos = {"Gancho": 10, "Arranhão": 10, "Tapa de Lama": 40}


Ponyta = Pokemon("Ponyta", 50, 50, 60, "Fogo", "Fogo", {"Ataque rápido": 20, "Raio Psíquico": 30, "Lança chamas": 80}, "")


Dewgong = Pokemon("Dewgong", 90, 90, 50, "Água", "Gelo", {"Retorno Glacial": 40, "Surra de Calda": 60, "Raio Aurora": 100}, "")


Seadra = Pokemon("Seadra", 55, 55, 50, "Água", "Água", {"Jato dágua": 10, "Revólver dágua": 40, "Tita Ofuscante": 50}, "")


Moltres = Pokemon("Moltres", 90, 90, 60, "Fogo", "Voador", {"Fúria Ardente": 20, "Asa de fogo": 50, "Aura Ardente": 190}, "")


Seel = Pokemon("Seel", 65, 65, 30, "Água", "Água", {"Ataque de Chifre" : 30, "Cabeçada" : 40, "Chuva Borrifante" : 80}, "")


Entei = Pokemon("Entei", 115, 115, 60, "Fogo", "Fogo", {"Presas de fogo" : 20, "Combustão" : 50, "Crina de Fogo" : 100}, "")


Metang = Pokemon("Metang", 60, 60, 30, "Ferro", "Psíquico", {"Aríete" : 20, "Explosão Magnética" : 60, "Feixe do Núcleo" : 80}, "")


Throh = Pokemon("Throh", 120, 120, 30, "Lutador", "Lutador", {"Bote" : 30, "Arremesso Inverso": 55, "Arremesso Sísmico" : 110}, "")


Giratina = Pokemon("Giratina", 150, 150, 70, "Fantasma", "Dragão", {"Bola das trevas": 40, "Esfera de aura": 60, "Impacto Sombrio" : 130}, "")

pokemons = [Chikorita, Arceus, Mewtwo, Psyduck, Ho_oh, Paras, Butterfree, Sunflora, Charmander, Pikachu, Diglett, Ponyta, Dewgong, Seadra, Moltres, Seel, Entei, Metang, Throh, Giratina]

# musicas
opening = Musica("opening", diretorio_atual + r"\audio\inicial.mp3")

ending = Musica("ending", diretorio_atual + r"\audio\ending.mp3")

lab = Musica("lab", diretorio_atual + r"\audio\lab.mp3")

celadon_city = Musica("celadon city", diretorio_atual + r"\audio\celadon city.mp3")

bicycle = Musica("bicycle", diretorio_atual + r"\audio\bicycle.mp3")

route11 = Musica("route11", diretorio_atual + r"\audio\route11.mp3")

guidepost = Musica("guidepost", diretorio_atual + r"\audio\guidepost.mp3")

musicas_inicio = [opening, ending, lab, celadon_city, bicycle, route11, guidepost]

#####

trainer_battle = Musica("trainer battle", diretorio_atual + r"\audio\trainer battle.mp3")

gym_leader_battle = Musica("gym leader battle", diretorio_atual + r"\audio\gym leader battle.mp3")

wild_pokemon_battle = Musica("wild pokemon battle", diretorio_atual + r"\audio\wild pokemon battle.mp3")

final_rival_battle = Musica("final rival battle", diretorio_atual + r"\audio\final rival battle.mp3")

johto_battle = Musica("johto battle", diretorio_atual + r"\audio\johto battle.mp3")

musicas_batalha = [trainer_battle, gym_leader_battle, wild_pokemon_battle, final_rival_battle, johto_battle, ]