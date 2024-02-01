# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. 
# A seguir, calcule e mostre o valor da conta a pagar.

# CODIGO  ESPECIFICAÇÃO       PREÇO
# 1       cachorro quente     4.00
# 2       X-Salada            4.50
# 3       X-Bancon            5.00
# 4       Torrada simples     2.00
# 5       Refrigerante        1.50

# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

def comanda(codigo,quantidade):
    precos = {1:4.00,
              2:4.50,
              3:5.00,
              4:2.00,
              5:1.50}
    total = precos[codigo]*quantidade    
    return total

codigo,quantidade = list(map(int,input().split(' ')))

print(f'Total: R$ {comanda(codigo,quantidade):.2f}')
