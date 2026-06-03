'''Projeto 02 - Sistema de Votação Eletrônica.
Crie um sistema de votação para 3 candidatos, além de votos nulos.Quando o usuário digitar 0 o sistema para o loop e exibe o total de votos
para cada candidato, além de quem ganhou.
'''
def votar():
  candidato1:int = 0
  candidato2:int = 0
  candidato3:int = 0
  voto_nulo:int = 0
  while True:
    votar:str = input("Escolha seu candidato  A->candidato1, B->candidato2, C=>candidato3 ou 0 para encerrar:  ").upper()
    match votar:
      case "A":
        candidato1 = candidato1 +1
      case "B":
        candidato2 = candidato2 + 1
      case "C":
        candidato3 = candidato3 + 1
      case "0":
        break
      case _:
        voto_nulo =  voto_nulo + 1
  print(f"Votos para o candidato A: {candidato1}")
  print(f"Votos para o candidato B: {candidato2}")
  print(f"Votos para o candidato C: {candidato3}")
  print(f"Votos nulos: {voto_nulo}")
  if candidato1 > candidato2 and candidato1 > candidato3:
    print("O vencedor é o candidato A")
  elif candidato2 > candidato1 and candidato2 > candidato3:
    print("O vencedor é o candidato B")
  elif candidato3 > candidato1 and candidato3 > candidato2:
    print("O vencedor é o candidato C")
  else:
    print("Houve um empate entre os candidatos")
votar()
