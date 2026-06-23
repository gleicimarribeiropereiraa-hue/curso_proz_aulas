Create Table if NOT EXISTS cliente(
    id INTEGER  PRIMARY KEY AUTOINCREMENT, 
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
  	email VARCHAR(50)
);

Create Table if NOT EXISTS carros(
    id INTEGER   PRIMARY KEY AUTOINCREMENT, 
    modelo VARCHAR(20),
    placa VARCHAR(255) NOT NULL UNIQUE,
  	ano VARCHAR(255) NOT NULL,
  	marca VARCHAR(50)
);

Create Table if NOT EXISTS servicos(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tipo_servico VARCHAR(255),
  custo FLOAT,
  servico_car INTEGER,
  FOREIGN KEY (servico_car) REFERENCES carros(ID));
  
  
INSERT INTO cliente(nome,telefone, email) VALUES ('Paulo','3121242142','p@gmail.com');
INSERT Into  carros(MODELO, PLACA, ANO, MARCA) VALUES('AUDI Q3','4875JH','2025','AUDI');
INSERT INTO  servicos(tipo_servico,custo,servico_car) VALUES('Refeito Motor','5000',1)
