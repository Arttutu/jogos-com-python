import random
import re


class jogo:

    def bem_vindo(self):
        print("********************************")
        print("Bem vindo ao jogo de Pedra Papel Tesoura")
        print("********************************")

    def escolha_do_oponente(self):
        with open("PedraPapelTesoura") as arquivo:
            elemento = []
            for linha in arquivo:
                elemento.append(linha)
                acao_do_oponente = random.choice(elemento)

            return acao_do_oponente

    def minha_escolha(self):
        escolha = str(input("O que vc joga ? pedra, papel ou tesoura\n"))
        self.validacao(escolha)

        return escolha

    def validacao(self, validacao_escolha):
        valida = re.compile(f"(pedra)")
        valida2 = re.compile(f"(tesoura)")
        valida3 = re.compile(f"(papel)")
        encontra_elemento = valida.match(validacao_escolha)
        encontra_elemento2 = valida2.match(validacao_escolha)
        encontra_elemento3 = valida3.match(validacao_escolha)

        if encontra_elemento or encontra_elemento2 or encontra_elemento3:
            pass
        else:
            print("Esse não é a forma correta de jogar!!!")
            print("Jogue Denovo")
            self.minha_escolha()

    def calcular_resultado(self, sua_escolha, escolha_oponente):

        if escolha_oponente == 'tesoura':

            if sua_escolha == 'pedra':

                return 'vc ganhou'

            elif sua_escolha == 'papel':

                return 'vc perdeu'

            else:
                return 'vc empatou'
        elif escolha_oponente == "pedra":

            if sua_escolha == 'pedra':
                return 'vc empatou'

            elif sua_escolha == 'papel':

                return 'vc ganhou'
            else:

                return 'vc perdeu'

        elif escolha_oponente == "papel":

            if sua_escolha == 'pedra':
                return 'vc perdeu'

            elif sua_escolha == 'papel':
                return 'vc empatou'

            else:
                return 'vc ganhou'

    def imprime_acao(self,minha_escolha, escolha_oponente):
        print(f'vc jogou {minha_escolha}')
        print(f'o oponente jogou {escolha_oponente}')



jogo = jogo()
jogo.bem_vindo()
eu = jogo.minha_escolha().strip()
oponente = jogo.escolha_do_oponente().strip()
jogo.imprime_acao(eu, oponente)
resultado = jogo.calcular_resultado(eu, oponente)
print(resultado)
