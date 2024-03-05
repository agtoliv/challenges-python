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

print("a) A sequência representa os números impares, e completando o próximo elemento, a sequência fica:",odd_numbers)

#b)
even_numbers = []

ib = 2
countb = 0

while countb < 5:
    if ib % 2 == 0:
        even_numbers.append(ib)
        countb += 1
    ib += 2

print("b) A sequência representa os números pares, e completando o próximo elemento, a sequência fica:",even_numbers)


#c)
square_numbers = []