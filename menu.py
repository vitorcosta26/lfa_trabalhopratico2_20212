def menu(opcoes, msg_inicio=None, opcao='',
         msg_opcao_invalida='\033[31m' + '\nOpção inválida! Escolha novamente!' + '\033[0;0m'):
    if msg_inicio is not None:
        print(msg_inicio)

    # Imprimir opções
    for i in range(len(opcoes)):
        print(f"{[i + 1]} {opcoes[i]}")

    try:
        opcao_escolhida = int(input(opcao))
        if opcao_escolhida in range(1, len(opcoes) + 1):
            return opcoes[opcao_escolhida - 1]
        else:
            raise msg_opcao_invalida
    except:
        print(msg_opcao_invalida)
        return menu(opcoes, msg_inicio, opcao, msg_opcao_invalida)