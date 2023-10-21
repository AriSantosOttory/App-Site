#C:\Users\bemol\AppData\Local\Programs\Python\Python311\
import pymysql
def criar():
    print('Escolheu Criar')
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="bd_00")
    cursor = connection.cursor()
    ArtistTableSql = """ CREATE TABLE Artistas(
    Id INT(20) PRIMARY KEY AUTO_INCREMENT,
    nome CHA(20) NOT NULL,
    musica CHA(20))"""
    cursor.execute(ArtistTableSql)
    connection.close()
    print('Tabela Criada com Sucesso!')

def inserir():
    print('Escolheu inserir')
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="bd_00")
    cursor = connection.cursor()
    insert1 ="INSERIR INTO Artistas(nome,musica) VALUES('Quin Barreiros','Cabritinha');"
    insert2 ="INSERIR INTO Artistas(nome,musica) VALUES('Zé Cabra','São Lagrimas');"
    insert3 ="INSERIR INTO Artistas(nome,musica) VALUES('Azeitonas','não sei o nome');"
    cursor.execute(insert1)
    cursor.execute(insert2)
    cursor.execute(insert3)
    connection.commit()
    connection.close()

def listar():
    print('Escolheu listar')
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="bd_00")
    cursor = connection.cursor()
    retrive = 'Select + from Artistas; *' #instrução para obter dados
    cursor.execute(retrive) #instrução ara executar comando
    row = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()
    connection.close()


def procurar():
    print('Escolheu procurar')
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="bd_00")
    cursor = connection.cursor()
    nome_artista = input("Digite o nome do artista que deseja procurar: ")
    query = f"SELECT * FROM Artistas WHERE nome = '{nome_artista}';"
    cursor.execute(query)
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Artista não encontrado.")
    else:
        for row in rows:
            print("ID:", row[0])
            print("Nome:", row[1])
            print("Música:", row[2])

    connection.close()


def alterar():
    print('Escolheu alterar')
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="bd_00")
    cursor = connection.cursor()
    id_artista = int(input("Digite o ID do artista que deseja alterar: "))
    novo_nome = input("Digite o novo nome do artista: ")
    nova_musica = input("Digite a nova música do artista: ")
    query = f"UPDATE Artistas SET nome = '{novo_nome}', musica = '{nova_musica}' WHERE Id = {id_artista};"
    cursor.execute(query)
    connection.commit()
    print("Artista alterado com sucesso.")
    connection.close()


def apagar():
    print('Escolheu apagar')
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="bd_00")
    cursor = connection.cursor()
    id_artista = int(input("Digite o ID do artista que deseja apagar: "))
    query = f"DELETE FROM Artistas WHERE Id = {id_artista};"
    cursor.execute(query)
    connection.commit()
    print("Artista apagado com sucesso.")
    connection.close()


def sair():
    print('Encerrando o programa.')

#MENU
if __name__ == '__main__':
    opcao = -1
    while opcao != 0:
        print('###PROGRAMA PARA GETÃO DE ARTISTAS###')
        print('1 - Criar a base de dados')
        print('2 - Inserir Artistas')
        print('3 - Lista Artistas')
        print('4 - Procurar Artista')
        print('5 - Alterar Artista')
        print('6 - Eliminar Artista')
        print('0 - Sair')
        opcao = int(input('Escolha uma das Seguintes Opções'))
        if opcao == 1:
            criar()
        if opcao == 2:
            inserir()
        if opcao == 3:
            listar()
        if opcao == 4:
            procurar()
        if opcao == 5:
            alterar()
        if opcao == 6:
            apagar()
        if opcao == 0:
            sair()