"""
1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?
"""

INDICE = int(13)
SOMA = int(0)
K = int(0)

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
    
print("Ao final do processamento, o valor de SOMA será =",SOMA,)