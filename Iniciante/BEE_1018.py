# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. 
# Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

def min_qtd_cedulas(cedulas:list,valor:float):
    print(valor)
    aux = valor
    for i in cedulas:
        print(f'{int(aux/i)} nota(s) de R$ {i},00')
        aux = aux%i


cedulas = [100,50,20,10,5,2,1]
valor = int(input())
min_qtd_cedulas(cedulas,valor)
