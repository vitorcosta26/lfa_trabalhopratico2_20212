class Gramatica:
    
    # Construtor
    def __init__(self, arquivo):
        self.gramatica, s_i, t, n_t = self.ler_gramatica(arquivo)
        self.simbolo_inicial = s_i
        self.terminais = t
        self.nao_terminais = n_t

    # Ler arquivo e salvar a gramática em memória
    @staticmethod
    def ler_gramatica(arquivo):

        with open(arquivo + '.txt', 'r') as gramatica:
            gramatica = gramatica.read().splitlines()

        simbolo_inicial = gramatica[0][0]
        terminais = []
        nao_terminais = []
        for linha in gramatica:
            regra, producao = linha.split("=>")
            producao = producao.split("|")

            for simbolo in producao:
                if str.islower(simbolo):
                    terminais.append([regra, simbolo])
                if if str.isupper(simbolo):
                    nao_terminais.append([regra, simbolo])

        return gramatica, simbolo_inicial, terminais, nao_terminais
