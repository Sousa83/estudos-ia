from random import *

w1 = random()
w2 = random()

e1 = int(input("Digite a entrada 1 \n> "))
e2 = int(input("Digite a entrada 2 \n> "))

error = 1

while error != 0:
    if e1 == 1 and e2 == 1:
        resultE = 1
    else:
        resultE = 0

    perceptron = (w1 * e1) + (w2 * e2)

    if perceptron < 1:
        resultC = 0
    elif perceptron >= 1:
        resultC = 1

    print(f'result: {resultC}')

    error = resultE - resultC

    print(f'p1: {w1}\np2: {w2}')

    w1 = w1 + (0.1 * e1 * error)
    w2 = w2 + (0.1 * e2 * error)
    print(f'error: {error}\n')
