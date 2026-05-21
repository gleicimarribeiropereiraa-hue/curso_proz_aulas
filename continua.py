continua: str = 's'

saldo: float = 0.0

while continua == "s":

    opt: str = input(
        "Digite A: Sacar | B: Depositar | C: Saldo: "
    )

    match opt.upper():

        case 'A':
            valor_saque: float = float(
                input("Digite o valor do saque: ")
            )

            saldo = saldo - valor_saque

            print("Saque realizado com sucesso")

        case 'B':
            valor_deposito: float = float(
                input("Digite o valor do depósito: ")
            )

            saldo = saldo + valor_deposito

            print("Depósito realizado com sucesso")

        case 'C':
            print(f"O saldo atual é {saldo}")

        case _:
            print("Opção inválida")

    continua = input(
        "Pressione s para continuar: "
    ).lower()

print("Programa encerrado")