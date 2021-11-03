from menu import menu
from gramatica import Gramatica

# Opções de Menu
cadastrar = 'Cadastrar gramática'
imprimir_gramatica = 'Imprimir gramática'
imprimir_informacoes = 'Imprimir informações sobre a gramática'
testar = 'Testar palavra'
sair = 'Sair'

# Tupla com as opções
opcoes = (cadastrar, imprimir_gramatica, imprimir_informacoes, testar, sair)

# Mensagens do menu
inicio = '\nEscolha uma das opções de gráfico abaixo\n'
opcao = '\nDigite a opção escolhida: '

# Menu
resposta = menu(opcoes, inicio, opcao)
while resposta != sair:

    if resposta == cadastrar:
        print('\n= Cadastrar gramática =\n')
        nome_arquivo = input('Digite o nome do arquivo, sem o \'.txt\': ')
        gramatica = Gramatica(nome_arquivo)

    elif resposta == imprimir_gramatica:
        print('\n= Imprimir gramática =\n')
        gramatica.imprimir_gramatica()

    elif resposta == imprimir_informacoes:
        print('\n= Imprimir informações sobre a gramática =\n')
        gramatica.imprimir_informacoes()

    elif resposta == testar:
        print('\n= Testar palavra =\n')
        palavra = input('Digite a palavra: ')
        gramatica.testr_palavra_cyk(palavra)

    resposta = menu(opcoes, inicio, opcao)

print('\n= Saindo =')
