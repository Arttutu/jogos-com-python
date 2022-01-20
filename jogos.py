import adivinhacao2
import forca
def jogar():
    print("**********************************")
    print("******** Escolha o seu jogo ******")
    print("**********************************")

    print("[1] Adivinhação, [2] forca")
    jogo = int(input("Qual o jogo ? "))

    if (jogo == 1):
        print(" jogando Adivinhação")
        adivinhacao2.jogar()

    elif (jogo == 2):
        print(" jogando forca")
        forca.jogar()

if(__name__== "__main__"):
    jogar()