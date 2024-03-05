"""""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

def is_in_fibonacci(testNumber):
    if testNumber == 0:
        return True  
    a, b = 0, 1
    while a < testNumber:
        a, b = b, a + b
    return a == testNumber

testNumber = int(input("Digite o número para ver se está na sequência de Fibonacci: "))

if is_in_fibonacci(testNumber):
    print(f"O número {testNumber} está na sequência de Fibonacci")
else:
    print(f"O número {testNumber} não está na sequência de Fibonacci")




