"""""
3) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____
"""
#a)
odd_numbers = []

i = 1
count = 0

while count < 5:
    if i % 2 != 0:
        odd_numbers.append(i)  
        count += 1
    i += 2

print("a) A sequência representa os números ímpares, completando o próximo elemento, a sequência fica:",odd_numbers)

#b)
square_two = []
ib = 1
countb = 0

while countb < 7:
    two = 2**ib
    square_two.append(two)
    countb += 1
    ib += 1

print("b) A sequência representa os quadrados do número 2, completando o próximo elemento, a sequência fica:",square_two)


#c)
square_numbers = []

ic = 0
countc = 0

while countc < 8:
    square = ic**2
    square_numbers.append(square)
    countc += 1
    ic += 1

print("c) A sequência representa os números inteiros ao quadrado, completando o próximo elemento:",square_numbers)


#d)
even_numbers = []

ib = 2
countb = 0

while countb < 7:
    if ib % 2 == 0:
        even_numbers.append(ib)
        countb += 1
    ib += 2

even_square_numbers = []

for x in even_numbers[:5]:
        even_square_numbers.append(x**2)

print("d) A sequência representa os números pares ao quadrado, completando o próximo elemento:",even_square_numbers)

#e)
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    fib_sequence = [1, 1]
    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)

    return fib_sequence

fib_sequence = fibonacci(7)
print("e) Os números representam a sequencia de Fibonnacci, completando o próximo elemento, a sequência fica:",fib_sequence)

#f)
print("f) A sequencia representa os números que começam com a letra D, no português brasileiro, completando a sequência: [2, 10, 12, 16, 17, 18, 19, 200]")
