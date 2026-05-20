'''
1- Faça um programa ,utilizando while ,que mostre na tela os numero de 0  a 100.
2- Faça um programa ,utilizando while ,que mostre na tela os numero de 0  a N em que N é definido pelo usuario
3- Faça um programa ,utilizando while ,que mostre na tela  todos os numero pares de 0  a 100.
4-Desenvolva um programa que exibe a  tabuada do número 5
'''


'''1
cont= 0 
while cont <=100:
    cont = cont + 1
    print(f"Estamos no {cont}")
'''
'''#2
cont= 0 
N:int = int(input("Digite o valor de N: "))

while cont <=N:
    
    print(f"Estamos no {cont}")
    cont = cont + 1
    '''

'''#3 valores par 
cont= 0

while cont <=100:

     if cont % 2 ==0
        
        print(f"{cont}")
        cont = cont + 2
     
'''

#For 4
numero= 1
contador=0
'''for i in range(1, 11):

    print(f"{numero} x {i} = {numero * i}")'''
    
'''while contador <=10:
    tabuada:int = numero * contador
    print(f"{numero} X {contador} = {tabuada}")
    contador =contador+1
    '''

while numero < 10:
    contador=0
    while contador <=10:
        print(f"Tabuada do {numero}")
        tabuada:int = numero * contador
        print(f"{numero} X {contador} = {tabuada}\n ")
        contador =contador+1
    numero= numero+1