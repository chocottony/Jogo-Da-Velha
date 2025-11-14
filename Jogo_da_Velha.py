import os
import random
from colorama import Fore, Back, Style #estilo e coisas a mais

jogarNovamente = "Sim"
jogadas = 0
quemJoga = 2 #1 igual CPU 2 igual jogador
maxjogadas = 9
vit = "Não"
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def tela():
    global tabuleiro
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  " + tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2])
    print("   -----------")
    print("1:  " + tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2])
    print("   -----------")
    print("2:  " + tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2])
    print("Número de Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogadasJogador1():
    global jogadas
    global quemJoga
    global vit
    global maxjogadas
    global tabuleiro
    if quemJoga == 2 and jogadas < maxjogadas:
        try:
            l = int(input("Linha.: "))
            c = int(input("Coluna: "))
            while tabuleiro[l][c] != " ":
                l = int(input("Linha.: "))
                c = int(input("Coluna: "))

            tabuleiro[l][c] = ("X")
            quemJoga = 1
            jogadas += 1
        except:
            print("Linha e ou coluna inválida!")
            os.system("pause")

def jogadasJogador2():
    global jogadas
    global quemJoga
    global vit
    global maxjogadas
    global tabuleiro
    if quemJoga == 1 and jogadas < maxjogadas:
        try:
            l = int(input("Linha.: "))
            c = int(input("Coluna: "))
            while tabuleiro[l][c] != " ":
                l = int(input("Linha.: "))
                c = int(input("Coluna: "))

            tabuleiro[l][c] = ("O")
            quemJoga = 2
            jogadas += 1
        except:
            print("Linha e ou coluna inválida!")
            os.system("pause")

'''def jogadasCPU():
    global jogadas
    global quemJoga
    global vit
    global maxjogadas
    global tabuleiro
    if quemJoga == 1 and jogadas < maxjogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while tabuleiro[l][c] != " ":
            l = random.randrange(0,3)
            c = random.randrange(0,3)

        tabuleiro[l][c] = ("O")
        quemJoga = 2
        jogadas += 1'''

def verificarVitoria():
    global tabuleiro
    vitoria = "Não"
    simbolos = ["X", "O"]

    for s in simbolos:
        vitoria = "Não"

        #Verifica Linha
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if(tabuleiro[il][ic] == s):
                    soma += 1
                ic += 1
            if (soma == 3):
                vitoria = s
                break
            il += 1
        if (vitoria != "Não"):
            break

        #Verifica Coluna
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if(tabuleiro[il][ic] == s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if (vitoria != "Não"):
            break
    
        #Verificar Diagonal 1
        soma = 0
        idiag = 0

        while idiag < 3:
            if(tabuleiro[idiag][idiag] == s):
                soma += 1
            idiag += 1
        if (soma == 3):
            vitoria = s
            break

        #Verifica Diagonal 2
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if(tabuleiro[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if (soma == 3):
            vitoria = s
            break
    return vitoria

def redefinir():
    global tabuleiro
    global jogadas
    global quemJoga
    global maxjogadas
    global vit

    jogadas = 0
    quemJoga = 2 
    maxjogadas = 9
    vit = "Não"
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

while(jogarNovamente == "Sim" or "sim"):
    
    redefinir()
    while True:
        tela()

        #em caso de dois jogadores
        if (quemJoga == 2):
            jogadasJogador1()
        else:
            jogadasJogador2()
        
        #em caso de jogador contra CPU
        '''jogadasJogador1()
        jogadasCPU()'''
        
        tela()
        vit = verificarVitoria()

        if(vit != "Não") or (jogadas >= maxjogadas):
            break

    print(Fore.RED + "Fim de Jogo" + Fore.YELLOW)
    if (vit == "X" or vit == "O"):
        print("Resultado: Jogador " + vit + " venceu!")
    else:
        print("Resultado: Empate")

    jogarNovamente = input(Fore.BLUE + "Jogar novamente? [Sim/Não]" + Fore.RESET)  
    if jogarNovamente != "Sim" and jogarNovamente != "sim":
        break