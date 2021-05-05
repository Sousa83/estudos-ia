from random import *

w1 = random()
w2 = random()
wBias = 0.3

bias = 1
error = 1

next = 1

while next != 0:
    e1 = int(input("Digite a entrada 1 \n> "))
    e2 = int(input("Digite a entrada 2 \n> "))

    perceptron = (w1 * e1) + (w2 * e2) + (wBias * bias)

    if perceptron < 0:
        resultC = 0
    elif perceptron >= 0:
        resultC = 1

    if e1 == 1 and e2 == 1:
        resultE = 1
    else:
        resultE = 0

    error = resultE - resultC

    print(f'p1: {w1}\np2: {w2}\npb: {wBias}')
    print(f'error: {error}\n')

    w1 = w1 + (0.1 * e1 * error)
    w2 = w2 + (0.1 * e2 * error)
    wBias = wBias + (0.1 * bias * error)

    print(f'resultado esperado: {resultE}\nresultado calculado: {resultC}')

    next = int(input('Deseja inserir mais um dado? 1 (s), 2 (n) \n>'))
