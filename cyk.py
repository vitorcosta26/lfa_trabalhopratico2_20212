from collections import defaultdict

class CYK:

    def __init__(self, simbolo_inicial, regras, nao_terminais, terminais, palavra):
        self.simbolo_inicial = simbolo_inicial
        self.regras = regras
        self.nao_terminais = nao_terminais
        self.terminais = terminais
        self.palavra = palavra
        self.cyk, self.tabela = self.algoritmo_cyk()

    def algoritmo_cyk(self):

        tabela = [[set() for l in range(len(self.palavra) - letra)] for letra in range(len(self.palavra))]
        tabela_subcadeia = defaultdict(set)

        for i in range(1, len(self.palavra) + 1):

            for j in range(len(self.palavra) + 1 - i):
                subcadeia = self.palavra[j:j+i]
                
                if len(subcadeia) == 1:
                
                    for regra_terminal in self.terminais:
                        if regra_terminal[1] == subcadeia:
                            tabela[i - 1][j].add(regra_terminal[0])
                            tabela_subcadeia[subcadeia].add(regra_terminal[0])

                else:

                    regras_subcadeia = set()
                    
                    for k in range(i - 1):

                        producao_1 = tabela_subcadeia[subcadeia[:k + 1]]
                        producao_2 = tabela_subcadeia[subcadeia[k + 1:]]

                        for producao in [l + m for l in producao_1 for m in producao_2]:

                            for regra_nao_terminal in self.nao_terminais:
                                if producao == regra_nao_terminal[1]:
                                    tabela[i - 1][j].add(regra_nao_terminal[0])
                                    regras_subcadeia.add(regra_nao_terminal[0])
                    
                    tabela_subcadeia[subcadeia] = regras_subcadeia
        


        if self.simbolo_inicial in tabela[len(self.palavra) - 1][0]:
            return True, tabela
        else:
            return False, tabela

    def imprimir_cyk(self):

        print(f"{'-' * 10}")
        print("| Tabela |")
        print(f"{'-' * 10}")
        for i, celula in enumerate(self.tabela[::-1]):
            print('\n({:^3})'.format(len(self.tabela) - i), end=" ")
            for regras in celula:
                print('[{:^10}]'.format(' | '.join(regras)), end=" ")

        if self.cyk:
            saida = f'A palavra \'{self.palavra}\' pertence a gramática!'
            cor = '\033[32m'
        else:
            saida = f'A palavra \'{self.palavra}\' não pertence a gramática!'
            cor = '\033[31m'

        print('\n{:^6}'.format('w = '), end="")
        for letra in self.palavra:
            print('[' + cor + '{:^10}'.format(letra) + '\033[0;0m]', end=" ")

        x = len(saida)
        print(f"\n{'-' * x}")
        print(cor + saida + '\033[0;0m')
        print(f"{'-' * x}")
