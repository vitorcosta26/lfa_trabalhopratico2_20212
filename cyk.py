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
        tabela_subcadeia = [[set() for l in range(len(self.palavra) - letra)] for letra in range(len(self.palavra))]

        for i, letra in enumerate(self.palavra):
            for terminal in self.terminais:
                if terminal[1] == letra:
                    tabela[0][i].add(terminal[0])
                    tabela_subcadeia[0][i].add(letra)
                elif len(tabela_subcadeia[0][i]) == 0 and terminal[1] != letra:
                    tabela_subcadeia[0][i].add(letra)

        for i in range(1, len(self.palavra)):
            for j in range(len(self.palavra) - i):
                for k in range(i):
                    regras_subcadeia = set()

                    for primeira_regra in tabela_subcadeia[k][j]:
                        for segunda_regra in tabela_subcadeia[i - k - 1][j + k + 1]:
                            if str.islower(primeira_regra):
                                for regra in self.terminais:
                                    if regra[1] == primeira_regra:
                                        primeira_regra = regra[0]
                            elif str.isupper(primeira_regra):
                                for regra in self.nao_terminais:
                                    if regra[1] == primeira_regra:
                                        primeira_regra = regra[0]
                            if str.islower(segunda_regra):
                                for regra in self.terminais:
                                    if regra[1] == segunda_regra:
                                        segunda_regra = regra[0]
                            elif str.isupper(segunda_regra):
                                for regra in self.nao_terminais:
                                    if regra[1] == segunda_regra:
                                        segunda_regra = regra[0]
                            regras_subcadeia.add(primeira_regra + segunda_regra)
                    combinacoes = regras_subcadeia

                    for combinacao in combinacoes:
                        for regra in self.regras:
                            if regra[1] == combinacao:
                                tabela[i][j].add(regra[0])
                                tabela_subcadeia[i][j].add(regra[0])

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
