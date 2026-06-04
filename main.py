'''
Criar uma forma de armazenar dados
nome |telefone |email
'''

def gravar_dados(nome:str,telefone:str,email:str):
# r->read =ler w->write ,a->adicionar 
    with open("contatos.txt","a")as arquivo:
        arquivo.write(f"{nome} | {telefone}  | {email}\n")
        
        print("Informações Gravadas")
    
    
    
def ler_dados():
    with open("contatos.txt","r") as arquivo:
        dados:list[str]= arquivo.readlines()
        for i in dados:
            print(i)
       
while True:
    opc = input("\nEscolha  \nA=>gravar | \nB->ler dados \nQ=>Sair: ").upper()
    match(opc):
        case "A":
            print("Você escolheu gravar dados  ")
            nome:str = input("Informe o nome : ")
            telefone:str = input("Informe o telefone : ")
            email:str =input("Informe o email: ")     
            gravar_dados(nome,telefone,email)
        case "B":
            print("Você escolheu gravar dados")
            ler_dados()
            
        case "Q":
            print("Encerrando o programa")
            break



'''  gravar_dados(nome,telefone,email)
    ler_dados()'''
