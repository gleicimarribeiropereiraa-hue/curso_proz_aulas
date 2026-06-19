'''
CREATE TABLE Hospede(
id:int pk  NN
nome:varchar(255) NN
documento: varchar(255) NN Unique
data_de_nascimento:date
telefone:varchar(255))
_ _ _ _ _ _ _ _ _ _ __ _ _ _ _ _
CREATE TABLE Quarto(
id:int pk
tipo:varchar(100)
status: bool
numero: varchar(100))
_ _ _ _ _ _ _ _ _ _ _

CREATE TABLE Reserva(
id:int pk
data_reserva: date
hospede_id:int FK
quarto_id:int fk

'''


'''

RH
CREATE TABLE Colaborador (
id: int pk
nome:varchar(200)
matricula:varchar(255)
setor: varchar(255)
data_nascimento : date  (idade)
id_cargo:int fk )
__ _ _ _ _ _ _ _ _ _ 

CREATE TABLE Cargo (
id:int pk
nome: varchar(100)
codigo:varchar(255)
descrição: text
valor:Float)


'''