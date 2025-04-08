import mysql.connector

class Banco:
    def conectar(self):
        return mysql.connector.connect(
            host = "paparella.com.br",
            user = "paparell_aluno_1",
            password = "@Senai2025",
            database = "paparell_python"
        )
    def criar_tabela(self):
        conexao = self.conectar()
        cursor=conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS leds (id INT AUTO_INCREMENT PRIMARY KEY,
                       aluno VARCHAR(255) NOT NULL, led INT NOT NULL, estado VARCHAR (255) NOT NULL ) ''')
        conexao.commit()
        cursor.close()
        conexao.close()
    
    def inserir_ou_atualizar_estado(self,aluno,led,estado):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(''' SELECT id FROM leds WHERE aluno = %s''',(aluno,))
        id = cursor.fetchone()
        if id:
            cursor.execute(''' UPDATE leds SET estado = %s WHERE id = %s''',(estado,id[0]))
            print(f"Estado do LED do Aluno: {aluno }, atualizado com sucesso")
        else:    
            cursor.execute(''' INSERT INTO leds (aluno,led,estado) VALUES (%s,%s,%s)''',(aluno,led,estado))
            print(f"Estado do LED do Aluno: {aluno }, atualizado com sucesso")
        conexao.commit()
        cursor.close()
        conexao.close()
        
    def listar(self):
        conexao = self.conectar()
        cursor=conexao.cursor()
        cursor.execute('''SELECT * FROM leds''')
        listas=cursor.fetchall()
        for lista in listas:
            print(f"ID: {lista[0]} | Aluno : {lista[1]} | Estado: {lista[2]}")
        
        conexao.commit()
        cursor.close()
        conexao.close()
    
    def ler_estado(self,aluno):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(''' SELECT estado FROM leds where aluno=%s''',(aluno,))
        estado = cursor.fetchall()
        for i in estado:
            print(i)
