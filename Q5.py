"""""
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def inverter_string(s):
    string_invertida = ''  
    for i in range(len(s) - 1, -1, -1):  
        string_invertida += s[i]  
    return string_invertida


s = input("Digite uma string para ser invertida: ")

string_invertida = inverter_string(s)

print("String invertida:", string_invertida)
