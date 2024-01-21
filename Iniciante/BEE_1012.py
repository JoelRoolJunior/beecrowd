# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.
# Entrada
# O arquivo de entrada contém três valores com um dígito após o ponto decimal.

# Saída
# O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com 
# mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos 
# após o ponto decimal.
valores = input().split(' ')
a,b,c = float(valores[0]), float(valores[1]), float(valores[2])

def area_triangulo(base, altura):
    return (base*altura)/2

def area_circulo(raio):
    PI = 3.14159
    return PI*raio**2

def area_trapezio(base_maior,base_menor,altura):
    return ((base_maior + base_menor)*altura)/2

def area_quadrado(lado):
    return lado**2

def area_retangulo(comprimento,altura):
    return comprimento*altura

print(f'TRIANGULO: {area_triangulo(a,c):.3f}')
print(f'CIRCULO: {area_circulo(c):.3f}')
print(f'TRAPEZIO: {area_trapezio(a,b,c):.3f}')
print(f'QUADRADO: {area_quadrado(b):.3f}')
print(f'RETANGULO: {area_retangulo(a,b):.3f}')
