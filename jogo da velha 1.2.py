from random import randint
from time import sleep

Tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cont = score = 0
jogo = True
ganhou = perdeu = velha = False


def clear():
    lines = 130
    print("\n" * lines)


def linha(x=28):
    print('-=' * x)


# FUNÇÃO PARA MOSTRAR O COMEÇO DO JOGO
def menu():
    linha()
    print(input('>>> PRESSIONE ENTER PARA COMEÇAR <<<'.center(55)))
    linha()
    clear()


# FUNÇÃO PARA MOSTRAR A TABELA
def table():
    linha()
    print(f'>>> TABELA <<<'.center(55))
    linha()
    print(f'   {Tabela[0]} / {Tabela[1]} / {Tabela[2]}' .center(53))
    print(f'   {Tabela[3]} / {Tabela[4]} / {Tabela[5]}'.center(53))
    print(f'   {Tabela[6]} / {Tabela[7]} / {Tabela[8]}'.center(53))
    linha()


# FUNÇÃO PARA A JOGADA DO CPU
def validation_cpu():
    ok = False
    while True:
        n = str(randint(1, 9))
        if n.isnumeric() and int(n) < 10 > 0 and int(n) in Tabela:
            Tabela[int(n) - 1] = 'O'
            ok = True
            print(f'O computador jogou na casa {n}')
        if ok:
            break


def validation_player(frase):
    ok = False
    while True:
        n = str(input(frase))
        if n.isnumeric() and int(n) < 10 > 0 and int(n) in Tabela:
            num = int(n)
            Tabela[num - 1] = 'X'
            print(f'O Player jogou na casa {n}')
            ok = True
        else:
            print('\033[;31mERRO !!! DIGITE UM NUMERO VALIDO.\033[m')
        if ok:
            break


# JOGO
menu()
table()
# ESTRUTURA DE REPETIÇÃO PARA REINICIALIZAÇÃO DO JOGO
while jogo:

    validation_player('Digite um numero: ')
    validation_cpu()

    # VALIDAÇÃO DA VITORIA / VELHA / CONTADOR
    if jogo:
        cont += 1
        # CONDIÇÃO DE VITORIA DO PLAYER

        if Tabela[0] == 'X' and Tabela[1] == 'X' and Tabela[2] == 'X':
            ganhou = True
        if Tabela[3] == 'X' and Tabela[4] == 'X' and Tabela[5] == 'X':
            ganhou = True
        if Tabela[6] == 'X' and Tabela[7] == 'X' and Tabela[8] == 'X':
            ganhou = True
        if Tabela[0] == 'X' and Tabela[3] == 'X' and Tabela[6] == 'X':
            ganhou = True
        if Tabela[1] == 'X' and Tabela[4] == 'X' and Tabela[7] == 'X':
            ganhou = True
        if Tabela[2] == 'X' and Tabela[5] == 'X' and Tabela[8] == 'X':
            ganhou = True
        if Tabela[0] == 'X' and Tabela[4] == 'X' and Tabela[8] == 'X':
            ganhou = True
        if Tabela[6] == 'X' and Tabela[4] == 'X' and Tabela[2] == 'X':
            ganhou = True
        if cont == 9:
            velha = True

    # SE O PLAYER PERDER
    if perdeu:
        table()
        print('Mais sorte da proxima vez !!!'
              f'Sua pontuação foi de {score}.')
        linha()
        continuacao = str(input('Você quer continuar jogando ? [S/N]')).strip().upper()
        linha()
        while True:
            if continuacao == 'S':
                linha()
                print('SUA PONTUAÇÃO FOI REINICIADA')
                linha()
                jogo = True
                ganhou = perdeu = velha = False
                cont = 0
                Tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                break

            elif continuacao == 'N':
                jogo = False
                break

            else:
                print('\033[;31mERRO !!! DIGITE UM COMANDO VALIDO [S/N]:\033[m')
                continuacao = str(input('Você quer continuar jogando ? [S/N]')).strip().upper()

    # SE O PLAYER GANHAR
    if ganhou:
        score += 1
        table()
        print('Parabens você ganhou !!!')
        continuacao = str(input('Você quer continuar jogando ? [S/N]:')).strip().upper()
        linha()
        while True:
            if continuacao == 'S':
                ganhou = perdeu = velha = False
                cont = 0
                Tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                break

            elif continuacao == 'N':
                jogo = False
                break

            else:
                print('\033[;31mERRO !!! DIGITE UM COMANDO VALIDO [S/N]:\033[m')
                continuacao = str(input('Você quer continuar jogando ? [S/N]')).strip().upper()

    # VALIDAÇÃO DA VITORIA / VELHA
    if jogo:
        if Tabela[0] == 'O' and Tabela[1] == 'O' and Tabela[2] == 'O':
            perdeu = True
        if Tabela[3] == 'O' and Tabela[4] == 'O' and Tabela[5] == 'O':
            perdeu = True
        if Tabela[6] == 'O' and Tabela[7] == 'O' and Tabela[8] == 'O':
            perdeu = True
        if Tabela[0] == 'O' and Tabela[3] == 'O' and Tabela[6] == 'O':
            perdeu = True
        if Tabela[1] == 'O' and Tabela[4] == 'O' and Tabela[7] == 'O':
            perdeu = True
        if Tabela[2] == 'O' and Tabela[5] == 'O' and Tabela[8] == 'O':
            perdeu = True
        if Tabela[0] == 'O' and Tabela[4] == 'O' and Tabela[8] == 'O':
            perdeu = True
        if Tabela[6] == 'O' and Tabela[4] == 'O' and Tabela[2] == 'O':
            perdeu = True
        if cont == 9:
            velha = True

    # SE O JOGO DER VELHA
    if velha:
        print('DEU VELHA... REINICIANDO JOGO')
        continuacao = str(input('Você quer continuar jogando ? [S/N]')).strip().upper()
        linha()
        while True:
            if continuacao == 'S':
                jogo = True
                ganhou = perdeu = velha = False
                cont = 0
                Tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                break

            elif continuacao == 'N':
                jogo = False
                break

            else:
                print('\033[;31mERRO !!! DIGITE UM COMANDO VALIDO [S/N]:\033[m')
                continuacao = str(input('Você quer continuar jogando ? [S/N]')).strip().upper()
    sleep(0.5)
    table()

clear()
linha()
print(f'Sua pontuação foi de {score}')
print('Fim do programa... Obrigado por jogar ^^')
linha()
