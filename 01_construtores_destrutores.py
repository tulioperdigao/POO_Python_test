class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo instância da classe...")

    def falar(self):
        print("auau")

def criar_cachorro():
    c = Cachorro("Zeus", "Preto", False)
    print(c.nome)

c = Cachorro("Chappie", "amarelo")
c.falar()

criar_cachorro()