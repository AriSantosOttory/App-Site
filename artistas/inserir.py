#!C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\python.exe

import sys
sys.path.append("C:\\Users\\Professor\\PycharmProjects\\bd_01\\venv\\Lib\\site-packages")
import pymysql

print("Content-Type: text/html\n\n")
import cgi
form = cgi.FieldStorage()

nome=form.getvalue("nome")
musica=form.getvalue("musica")
#print("Name in form: ",form.getvalue("nome"))
#print("Musica in form: ",form.getvalue("musica"))

connection = pymysql.connect(host="localhost", user="root", passwd="", database="bd_00")
cursor = connection.cursor()
insert = "INSERT INTO artistas(nome, musica) VALUES('"+nome+"', '"+musica+"');"
#print(insert)
cursor.execute(insert)
connection.commit()
connection.close()

print("<h1> Dados inseridos com sucesso</h1>")
print("<h3>Nome: "+form.getvalue("nome")+"<br>")
print("Musica: "+form.getvalue("musica")+"</h3>")
print('<br/><a href="index.html" target="_self">Voltar ao inicio</a>')


