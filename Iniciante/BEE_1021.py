# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. 
# A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
# A seguir mostre a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

# Saída
# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

# Obs: Utilize ponto (.) para separar a parte decimal.

def min_qtd_dinheiro(cedulas:list,valor:float):
    aux = valor
    for i in cedulas:
        if i > 1:
            if i == cedulas[0]:
                print('NOTAS:')
            print(f'{int(aux/i)} nota(s) de R$ {i:.2f}')
            aux = round(aux%i,2)
        elif  0 < i <= 1:
            if i == 1.0:
                print('MOEDAS:')   
            print(f'{int(aux/i)} moeda(s) de R$ {i:.2f}')
            aux = round(aux%i,2)


cedulas = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]
valor = float(input())
min_qtd_dinheiro(cedulas,valor)