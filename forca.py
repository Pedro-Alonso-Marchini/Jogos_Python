# forca.py
import random

def jogar():
    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letra_acertada = inicializa_letra_acertada(palavra_secreta)
    print(letra_acertada)

    enforcou = False
    acertou = False
    erros = 0
    conta = len(palavra_secreta)
    letras_erradas = []

    print("A palavra possui {} letras".format(conta))

    while (not acertou and not enforcou):

        chute = chute_usuario()

        if (chute in palavra_secreta):
            marca_chute(chute, letra_acertada, palavra_secreta)

        else:
            erros += 1
            print("Você errou! Ainda restam {} tentativas".format(7 - erros))
            desenha_forca(erros)

        if (chute not in palavra_secreta):
            letras_erradas.append(chute)
            print("Letras que você ja tentou: {}".format(letras_erradas))

        enforcou = erros == 7
        acertou = "_" not in letra_acertada
        print(letra_acertada)

    if (acertou):
        palavra_certa_mensagem(palavra_secreta)
    else:
        palavra_errada_mensagem(palavra_secreta)

def palavra_errada_mensagem(palavra_secreta):
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("Você perdeu!! A palavra era {}".format(palavra_secreta))

def palavra_certa_mensagem(palavra_secreta):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("Você ganhou!! A palavra era {}".format(palavra_secreta))

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letra_acertada(palavra):
    return ["_" for letra in palavra]

def chute_usuario():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute(chute, letra_acertada, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letra_acertada[index] = letra
        index += 1

if(__name__ == "__main__"):
    jogar()