import sqlite3

connection = sqlite3.connect('banco.db')#nome do banco de dados

cursor = connection.cursor()

criaTabela = "CREATE TABLE IF NOT EXISTS hoteis (hotelId text PRIMARY KEY,\
     nome text, estrelas real, diaria real, cidade text)"

criaHotel = "INSERT INTO hoteis VALUES ('alpha', 'Alpha Hotel', 4.3, 345.40,'Rio de Janeiro')"

cursor.execute(criaTabela)
cursor.execute(criaHotel)
connection.commit()
connection.close()