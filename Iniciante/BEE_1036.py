# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, 
# mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

# Entrada
# Leia três valores de ponto flutuante (double) A, B e C.

# Saída
# Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, 
# imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. 
# Imprima sempre o final de linha após cada mensagem.
import math

def delta_bhaskara(a,b,c):
    delta = b**2 - 4*a*c
    return delta

def bhaskara(a,b,c):
    delta = delta_bhaskara(a,b,c)
    if delta < 0 or a == 0:
        print('Impossivel calcular')
    else:
        r1 = (-b +math.sqrt(delta))/(2*a)
        r2 = (-b -math.sqrt(delta))/(2*a)
        print(f'R1 = {r1:.5f}')
        print(f'R2 = {r2:.5f}')

a, b, c = list(map(float,input().split()))
bhaskara(a, b, c)