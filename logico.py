'''
CREATE TABLE(Hóspede
id:int pk  NN
nome:varchar(255) NN
documento: varchar(255) NN Unique
data_de_nascimento:date
telefone:varchar(255))
_ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _
CREATE TABLE(Quarto
id:int pk
tipo:varchar(100)
status: bool
numero: varchar(100))
_ _ _ _ _ _ _ _ _ _ _

CREATE TABLE (Reserva
id:int pk
data_reseva: date
hospede_id:int FK
quarto_id:int fk
numero:varchar(100)

'''


'''
CREATE TABLE (Colaborador
id: int pk
nome:varchar(200)
matricula:varchar(255)
setor: varchar(255)
data_nascimento : date  (idade)
id_cargo)
__ _ _ _ _ _ _ _ _ _ 

CREATE TABLE (Cargo
id:int pk
codigo:varchar(255)
descrição: text
nome: varchar(100)
valor:Float)


'''