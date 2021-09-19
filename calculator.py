def menu():
    print()
    print(" Python Calculator ".center(50, '#'))

    select = 'n'
    while select != '0':
        select = input("\nOperações:\n"
                       "1 - Adição\n"
                       "2 - Subtração\n"
                       "3 - Multiplicação\n"
                       "4 - Divisão\n"
                       "0 - Sair\n"
                       "Escolha uma opção (1/2/3/4/0): ")

        if select == '1':
            print('\nAdição')
            op = getOp()
            printExpressao(select, *op)
            print(sum(convertArrayToFloat(op)))
        elif select == '2':
            print('\nSubtração')
            op = getOp()
            printExpressao(select, *op)
            print(subtracao(*convertArrayToFloat(op)))
        elif select == '3':
            print('\nMultiplicação')
            op = getOp()
            printExpressao(select, *op)
            print(multiplicacao(*convertArrayToFloat(op)))
        elif select == '4':
            print('\nDivisão')
            op = getOp()
            printExpressao(select, *op)
            print(divisao(*convertArrayToFloat(op)))
        elif select == '0':
            print('\nSair')
        else:
            print('Opção inválida.')


def getOp():
    op = []
    op.append(input('Informe o 1º operando: '))
    op.append(input('Informe o 2º operando: '))
    i = 2
    while op[i-1] != 'c':
        op.append(input('Informe o %sº operando (ou "c" para calcular): ' % (i+1)))
        i += 1
    op.pop()
    return op


def convertArrayToFloat(list):
    for n in list:
        list.insert(0, float(list.pop()))
    return list


def printExpressao(codOp, op1, *ops):
    sinais = ['+', '-', 'x', '÷']
    sinal = sinais[int(codOp) - 1]
    print('\n%s' % op1, end=' ')
    for n in ops:
        print(sinal, n, end=' ')
    print('=', end=' ')


def subtracao(op1, op2, *ops):
    result = op1 - op2
    for n in ops:
        result -= n
    return result


def multiplicacao(op1, op2, *ops):
    result = op1 * op2
    for n in ops:
        result *= n
    return result


def divisao(op1, op2, *ops):
    result = op1 / op2
    for n in ops:
        result /= n
    return result


menu()
