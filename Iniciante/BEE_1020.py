# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. 
# Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. 
# Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Imprima a saída conforme exemplo fornecido.

def ageDays2ageYears(age_days):
    yars = age_days//365
    aux = age_days%365
    months = aux//30
    aux = aux%30
    days = aux
    return(yars,months,days)


idade_em_dias = int(input())

conversao = ageDays2ageYears(idade_em_dias)

print(f'{conversao[0]} ano(s)')
print(f'{conversao[1]} mes(es)')
print(f'{conversao[2]} dia(s)')