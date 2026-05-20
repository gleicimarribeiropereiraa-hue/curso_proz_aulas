'''
Criar um programa que dê 5 chances para o usuário acertar o número

'''
chances :int = 5
numero_secreto :int =81
while chances >= 0:
    escolha :int = int(input("Informe o Número: "))
    chances = chances -1
    if numero_secreto == escolha:
       print("Parabéns acertou")
       break
    else:
        print(f"Numero errado, tente outra vez! você tem {chances} chances")
print("Fim do programa")