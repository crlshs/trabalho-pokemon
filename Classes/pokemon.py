from .animal import Animal

class Pokemon(Animal):
    def __init__(self, nome_pokemon:str, hp_total:int, hp_atual:int, velocidade:int, tipo1:str, tipo2:str, nome_ataque_valor_ataque:dict, imagem:str):
        super().__init__(nome_pokemon)
        self._hp_total = hp_total
        self._hp_atual = hp_atual
        self._velocidade = velocidade
        self._tipo1 = tipo1
        self._tipo2 = tipo2
        self._nome_ataque_valor_ataque = nome_ataque_valor_ataque
        self._imagem = imagem

    # gets #
    def get_nome_pokemon(self):
        return super().__str__()
    def get_hptotal(self):
        return self._hp_total
    def get_hpatual(self):
        return int(self._hp_atual)
    def get_velocidade(self):
        return self._velocidade
    def get_tipo1(self):
        return self._tipo1
    def get_tipo2(self):
        return self._tipo2
    def get_ataques(self):
        return self._nome_ataque_valor_ataque
    def get_danobasico1(self):
        return list(self._nome_ataque_valor_ataque.values())[0]
    def get_danobasico2(self):
        return list(self._nome_ataque_valor_ataque.values())[1]
    def get_ultimate(self):
        return list(self._nome_ataque_valor_ataque.values())[2]

    # sets #
    def set_hpatual(self, dano:int):
        self._hp_atual -= dano

    def reset_hp(self):
        self._hp_atual = self._hp_total

        total = ""
        for chave, valor in self._nome_ataque_valor_ataque.items():
            total += f"nome ataque: {chave} - dano: {valor} "
        return total
    
    def set_imagem(self, diretorio:str):
        self._imagem = diretorio

    # def __str__(self):
    #     def informacoes_ataques():
    #         total = ""
    #         for chave, valor in self._nome_ataque_valor_ataque.items():
    #             total += f"\nnome ataque: {chave} - dano: {valor} "
    #         return total

    #     return f"nome do pokémon: {super().__str__()}\nHP total: {self._hp_total}\nHP atual: {self._hp_atual}\velocidade: {self._velocidade}\ntipo1: {self._tipo1}\ntipo2: {self._tipo2}{informacoes_ataques()}"