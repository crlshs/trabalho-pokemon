class Animal:
    def __init__(self, nome_animal:str):
        self.nome = nome_animal

    def __str__(self):
        return self.nome