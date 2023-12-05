from .animal import Animal

class Treinador(Animal):
    def __init__(self, nome_treinador:str, genero:str, idade:int, regiao:str, equipe:str, orientador:str, imagem:str):
        super().__init__(nome_treinador)
        self._idade = idade
        self._regiao = regiao
        self._equipe = equipe
        self._orientador = orientador
        self._imagem = imagem

    def __str__(self):
        return f"nome: {super().__str__()}\nidade: {self.get_idade()}\nregião: {self.get_regiao()}\nequipe: {self.get_equipe()}\norientador: {self.get_orientador()}"
    
    # gets #
    def get_nome(self):
        return super().__str__()
    def get_idade(self):
        return self._idade
    def get_regiao(self):
        return self._regiao
    def get_equipe(self):
        return self._equipe
    def get_orientador(self):
        return self._orientador
    def get_imagem(self): 
        return self._imagem