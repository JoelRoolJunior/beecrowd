# Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. 
# Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela 
# mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada 
# for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, 
# o programa deve imprimir a mensagem "Aluno em exame.".

# No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a 
# mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a 
# média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 
# ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após 
# ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.

# Entrada
# A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

# Saída
# Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a 
# descrição do problema. Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error".

def media(notas,pesos):
    total = 0
    for i,j in zip(notas,pesos):
        total +=i*j
    media = total/sum(pesos)
    return media

def status(media):
    status = None
    if media >= 7.0:
        status = 'Aluno aprovado.'
    elif media >= 5 and media < 6.9:
        status = 'Aluno em exame.'
    elif media < 5.0:
        status = 'Aluno reprovado.'

    return status

def nota_exame(nota,media):
    nova_media = (nota+media)/2
    return nova_media

def status_exame(media):
    status = None
    if media >= 5:
        status = 'Aluno aprovado.'
    elif media < 5:
        status = 'Aluno reprovado.'
    return status

n1, n2, n3, n4 = list(map(float,input().split(' ')))

notas = [n1, n2, n3, n4]
pesos = [2 , 3 , 4 , 1]

media = media(notas,pesos)
status = status(media)

print(f'Media: {media:.1f}')
print(status)

if status == 'Aluno em exame.':
    nota = float(input())
    media = nota_exame(nota,media)
    status = status_exame(media)

    print(f'Nota do exame: {nota:.1f}')
    print(status)
    print(f'Media final: {media:.1f}')
