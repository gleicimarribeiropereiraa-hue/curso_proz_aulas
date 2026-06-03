'''
Projeto 01 - Crie um simulador de corridas de Uber. - Baseado na distancia em KM e
no horário(considere 24 horas como 13, 14, 19 20 etc). Calcule o valor pago por corrida.
Se for horário de pico entre 17 e 19 o valor tem uma taxa extra de R$2.50 por KM.
(valor base R$3.00 por km)
'''

def calcula_valor_corrida(distancia:float,horario:int):
    valor_base:float =3.00
    if 17<=horario <=19:
        valor_total:float = distancia *(valor_base + 2.50)
    elif 0<= horario <= 6:
        valor_total:float = distancia * (valor_base + 4.00)

    else:
        valor_total:float =distancia * valor_base
    return valor_total

def inicio():
    distancia:float =float(input("Digite a distancia da corrida em KM: "))
    horario:int =int(input("Digite o horário da corrida (0-23): "))
    valor_corrida:float =calcula_valor_corrida(distancia,horario)
    print(f"O valor total da corrida é: R${valor_corrida:.2f}")

inicio()

