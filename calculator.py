def menu():
    select = 'n'
    while select != '0':
        select = input("\n" +
                       " Python Calculator ".center(50, '#') +
                       "\n\nOperações:\n"
                       "1 - Adição\n"
                       "2 - Subtração\n"
                       "3 - Multiplicação\n"
                       "4 - Divisão\n"
                       "0 - Sair\n\n"
                       "Escolha uma opção (1/2/3/4/0): ")

        if select == '1':
            print('\nAdição')
            operators = getOperators()
            printExpression(select, *operators)
            print(sum(convertArrayToFloat(operators)))
        elif select == '2':
            print('\nSubtração')
            operators = getOperators()
            printExpression(select, *operators)
            print(subtraction(*convertArrayToFloat(operators)))
        elif select == '3':
            print('\nMultiplicação')
            operators = getOperators()
            printExpression(select, *operators)
            print(multiplication(*convertArrayToFloat(operators)))
        elif select == '4':
            print('\nDivisão')
            operators = getOperators()
            printExpression(select, *operators)
            print(division(*convertArrayToFloat(operators)))
        elif select == '0':
            print('\nSair')
        else:
            print('Opção inválida.')


def getOperators():
    operators = []
    operators.append(input('Informe o 1º operando: '))
    operators.append(input('Informe o 2º operando: '))
    i = 2
    while operators[i-1] != 'c':
        operators.append(
            input('Informe o %sº operando (ou "c" para calcular): ' % (i+1)))
        i += 1
    operators.pop()
    return operators


def convertArrayToFloat(list):
    for n in list:
        list.insert(0, float(list.pop()))
    return list


def printExpression(codOp, op1, *ops):
    sinais = ['+', '-', 'x', '÷']
    sinal = sinais[int(codOp) - 1]
    print('\n%s' % op1, end=' ')
    for n in ops:
        print(sinal, n, end=' ')
    print('=', end=' ')


def subtraction(op1, op2, *ops):
    result = op1 - op2
    for n in ops:
        result -= n
    return result


def multiplication(op1, op2, *ops):
    result = op1 * op2
    for n in ops:
        result *= n
    return result


def division(op1, op2, *ops):
    result = op1 / op2
    for n in ops:
        result /= n
    return result


menu()
