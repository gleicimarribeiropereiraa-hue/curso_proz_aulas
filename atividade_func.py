'''
Crie um programa que para calculo de area de figuras,sue programa deve calcular  triangulo,quadrado,retangulo e circulo.Cada um desses calculos deve ficar em uma função especifica.Permita ao usuário escolher o que calcular .
Pesquise sobre  a formula do calculo de cada figura
'''
def calcula_triangulo():
#Calculo de area do triangulo  base x altura  /2
    base:int= int(input("Digite o valor da base: "))
    altura:int= int(input("Digite o valor da altura: "))
    area= base * altura / 2
    print(area)
    

def calcula_quadrado():
#area= multiplicar a medida do lado por ele mesmo
    lado:int= int(input("Informe o valor do lado: "))
    area= lado * lado 
    print(area)
    

def calcula_retangulo():
#area = base x altura
    base:int= int(input("Digite o valor da base: "))
    altura:int= int(input("Digite o valor da altura: "))
    area= base * altura 
    print(f"O valor da área é:{area}")

    
def calcula_circulo():
#area = π * raio**2 
    PI:float = 3.14
    raio :int =int(input("Informe valor do raio: "))
    area = PI * raio ** 2 
    print(area)


while True:
    opcao : str =input("Diga o que deseja  calcular  area  A triangulo | B quadrado | C retangulo | D circulo | S para sair ").upper()
    match(opcao):
        case "A":
            print("Calculando área do triangulo:")
            calcula_triangulo()
        case "B":  
            print("Calculando área do quadrado:")
            calcula_quadrado()
        case "C":
            print("Calculando área do retangulo:")
            calcula_retangulo()
        case "D":
            print("Calculando área do circulo:")
            calcula_circulo()
        case "S":
            print("Saindo da calculadora")
            break