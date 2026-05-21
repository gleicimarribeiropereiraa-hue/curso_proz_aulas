'''
5 ler numero inteiro n.Escrever a soma de todos os numeros pare de 2 até n.
'''

n: int = int(input("Digite o valor de n: "))

soma:int = 0

contador:int = 2

while contador< n:
    
    if contador % 2 == 0:
       soma = soma + contador
    
    contador +=2
print(f"a soma dos pares até {n}  é igual a {soma}")