from cyk import CYK

class Gramatica:
    
    # Construtor
    def __init__(self, arquivo):
        self.gramatica, s_i, r, n_t, t = self.ler_gramatica(arquivo)
        self.simbolo_inicial = s_i
        self.regras = r
        self.nao_terminais = n_t
        self.terminais = t

    # Ler arquivo e salvar a gramática em memória
    @staticmethod
    def ler_gramatica(arquivo):

        with open(arquivo + '.txt', 'r') as gramatica:
            gramatica = gramatica.read().splitlines()

        simbolo_inicial = gramatica[0][0]
        regras = []
        terminais = []
        nao_terminais = []
        for linha in gramatica:
            regra, producao = linha.split(" => ")
            producao = producao.split(" | ")

            for letra in producao:
                regras.append([regra, letra])
                if not str.islower(letra):
                    nao_terminais.append([regra, letra])
                if str.islower(letra):
                    terminais.append([regra, letra])

        return gramatica, simbolo_inicial, regras, nao_terminais, terminais

    #Impressões terminal 
    def imprimir_gramatica(self):
        print(f"{'-' * 25}")

        for regra in self.gramatica:
            print(regra)

    def testr_palavra_cyk(self, palavra):

        teste = CYK(self.simbolo_inicial, self.regras, self.nao_terminais, self.terminais, palavra)
        teste.algoritmo_cyk()
        teste.imprimir_cyk()
