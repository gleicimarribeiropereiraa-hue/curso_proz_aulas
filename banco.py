'''Criar o sistema de um banco'''


saldo: float = 1000.0
senha_secreta :str = "12578"
print("Bem vindo ao BanKline")

def valida_senha(senha_digitada:float):
    global senha_secreta
    if senha_digitada == senha_secreta:
        return True
    else:
        return False

def consulta_saldo():
        
        print(f"O seu saldo atual é :{saldo:.2f}")

def sacar(valor_saque:float):
    global saldo
    if valor_saque > saldo:
    
        print(f"Saldo insuficiente  seu slado atual é : {saldo:.2f}")
    else:
        saldo = saldo  - valor_saque
        print(f"Saque realizado com sucesso: {valor_saque:.2f}")
        print(f"Saldo atualizado de {saldo:.2f}")

def depositar(valor_deposito: float):
    global saldo
    if valor_deposito != 0.0:
        saldo = valor_deposito + saldo
        print(f"saldo atualizado {saldo:.2f}")
    else:
        saldo = valor_deposito + saldo
        print(f"Seu saldo atual é de {saldo:.2f}")

def transferir(valor_transferir:float):
    global saldo
    if valor_transferir == 0.0:
        print(f"O valor não pode ser  0.")
    else:
        saldo = saldo - valor_transferir  
        print(f"Seu saldo atual é de  {saldo:.2f}")
        


''''sacar(200) 
consulta_saldo()
depositar(1300)
consulta_saldo()
transferir(150)
consulta_saldo()'''
print("Banco SkyBank")
print("==="*40)


while True:
    senha_digitada :str =input("Informe a senha: ")
    if valida_senha(senha_digitada):
        opcao :str = input("Selecione uma das opçoes:\n1 1->Consulta saldo \n 2->Sacar \n  3-> Transferir \n  4->Depositar \n  5-> Sair :")
        match (opcao):
            case "1":
                print("Você escolheu consultar saldo: ")
                consulta_saldo()
                print(f"{saldo}")
            case "2":
                print("Você escolheu Sacar")
                valor_saque:float = float(input("Informe o valor do Saque: "))
                sacar(valor_saque)
                consulta_saldo()
            case"3":
                print("Você escolheu Transferir :")
                valor_transferir:float = float(input("Informe o valor da transferência: "))
                transferir(valor_transferir)
                consulta_saldo
            case "4":
                print("Você escolheu Depositar")
                valor_deposito:float = float(input("Informe o valor de Depósito"))
                depositar(valor_deposito)
                consulta_saldo()
            case"5":
                print("Você escolheu sair")
                break
            case _:
                print("Opção inválida!")
else:
    print("Senha Invalida Acesso Negado")