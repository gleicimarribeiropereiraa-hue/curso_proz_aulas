'''
1 Crie uma lista de produtos e mostre todos eles
2 Crie uma lista de números inteiros e some todos os pares
3 Crie uma lista de produtos e verifique se um determinado produto está na lista
'''

produtos: list= ['café','açúcar','queijo','pão','farinha']

for i in produtos:
    print(i," \n")
    
numeros:list =[1,2,3,4,5,6,]
soma :int = 0
for n in numeros:
    if n > 0 and n % 2 ==0:
        soma += n
        print(f"{soma}\n")
        
        

produtos_2: list= ['café','açúcar','queijo','pão','farinha']

produto_exist = "Refrigerante"
encontrado = False
for p in produtos_2:
    if p == produto_exist:
        encontrado =True
    break


if encontrado:
    print(f"O produto {produto_exist} consta na lista")
else:
    print(f"O produto {produto_exist} NÃO consta na lista")