'''função :trecho de código que agrupa uma lógica e pode ser chamado em várias partes do programa.  
função tem nome parâmetros e retorno


'''
'''x:int =int(input("Digite o primeiro número: "))
y:int =int(input("Digite o segundo número: "))

total:int = x + y

if total <=25:
    print(f"O valor é menor que o necessário{total}")
else:
    print("O valor somado")'''

#Declaração ou definição de função
def soma():
    x:int =int(input("Digite o primeiro número: "))
    y:int =int(input("Digite o segundo número : "))
    total:int =x+y
    print(total)

def subtrai():
    x:int =int(input("Digite o primeiro número: "))
    y:int =int(input("Digite o segundo número : "))
    total:int = x - y
    print(total)

def multiplica():
    x:int =int(input("Digite o primeiro número: "))
    y:int =int(input("Digite o segundo número : "))
    total:int = x * y
    print(total)

def divide():
    x:int =int(input("Digite o primeiro número: "))
    y:int =int(input("Digite o segundo número : "))
    total:int = x / y
    print(total)
def exponenciar():
    x:int =int(input("Digite a base: "))
    y:int =int(input("Digite o expoente : "))
    total:int = x ** y
    print(total)
#chamada de função  
'''soma()

subtrai()'''

while True:
    opcao :str =input("Informe + para somar | - para subtrair |* multiplicar | / dividir |^ exponenciar |q para sair")
    match(opcao):
        case "+":
            print("somando dois valores")
            soma()
        case"-":
            print("Subtraindo  numeros")
            subtrai()
        case "*":
            print("Multiplicando numeros")
            multiplica()
        case"/":
            print("Dividindo numeros")
            divide()
        case "^":
            print("Exponenciando numero")
            exponenciar()
        case "q":
            print("Saindo da Calculadora")
    break