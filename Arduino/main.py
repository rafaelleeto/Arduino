import serial
import time
from banco import Banco

PORTA = "COM4"
ARDUINO  = serial.Serial(PORTA,9600,timeout=1)
time.sleep(2)

ALUNO = "Rafael Italiano"
LED = 1 
banco = Banco()
banco.criar_tabela()



while True:
    comando = input("Digite\n0-Sair Do Programa\n1-Ligar LED\n2-Desligar  LED")
    match comando:
        case "1":
            ARDUINO.write(b'1')
            banco.inserir_ou_atualizar_estado(ALUNO,LED,"ligado")
            print("LED LIGADO!")
        case "2":
            ARDUINO.write(b'2')
            banco.inserir_ou_atualizar_estado(ALUNO,LED,"desligado")
            print("LED DESLIGADO")
        case "3":
            banco.listar()
        
        case "4":
            banco.ler_estado(ALUNO)
        case "0":
            break
    