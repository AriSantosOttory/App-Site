#!C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\python.exe

import sys
sys.path.append("C:\\Users\\Professor\\PycharmProjects\\bd_01\\venv\\Lib\\site-packages")
import pymysql
print("Content-Type: text/html\n\n")

print('<h1>Listagem de Artistas</h1>')
connection = pymysql.connect(host="localhost", user="root", passwd="", database="bd_00")
cursor = connection.cursor()
# instrução para obter os dados
retrive = "Select * from Artistas;"
# execução da instrução
cursor.execute(retrive)
rows = cursor.fetchall()
i=0
print('<table border="1">')
print('<tr><th>Id</th><th>Artista</th><th>Musica</th></tr>')

for row in rows:
    print('<tr>')
    print('<td>',row[0],'</td><td>',row[1],'</td><td>',row[2],'</td>')
    i=i+1
    print('</tr>')

print('<tr><th colspan="3">Total de registos na bd => ',i,'</th></tr>')
print('</table>')

# termina a conexão e fecha-a
connection.commit()
connection.close()
print('<br/><a href="index.html" target="_self">Voltar ao inicio</a>')
