'''
Dicionário
'''

produtos: dict= {"Maçã":"5.60","Laranja":"4.89","abacaxi":"10.00"}


fruta:str =input("Informe a fruta: ")
print(f"O valor da {fruta} é de {produtos.get(fruta)}")



