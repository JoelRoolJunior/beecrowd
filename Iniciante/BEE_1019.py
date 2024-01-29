# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no 
# formato horas:minutos:segundos.

# Entrada
# O arquivo de entrada contém um valor inteiro N.

# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

def seconds2hms(seconds):
    h = seconds//(60*60)
    aux = seconds%(60*60)
    m = aux//60
    aux = aux%60
    return(f'{h}:{m}:{aux}')

tempo_evento = int(input()) #em segundos

print(seconds2hms(tempo_evento))
