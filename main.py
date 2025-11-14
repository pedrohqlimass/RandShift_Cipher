from funcoes import *

continuar = True

while continuar != False:

    desenha_logo()

    texto = input("\nDigite o texto que será codificado: ")

    codificador_randomico = random_excesso()

    resultado_criptografado = criptografia(texto, codificador_randomico)

    resposta = input("\nGostaria de ver a mensagem criptografada? | 1 - SIM | 2 - NÃO |\n")

    if resposta == "1":
        print("\nMensagem criptografada:", resultado_criptografado)
        resposta = input("\nGostaria de descriptografar a mensagem? | 1 - SIM | 2 - NÃO |\n")

        if resposta == "1":
            resultado = descriptografia(resultado_criptografado, codificador_randomico)
            print("\nMensagem descriptografada:", resultado)

            continuar = input("\nGostaria de continuar criptografando? | 1 - SIM | 2 - NÃO |\n")
            continuar = (continuar == "1")

        else:
            print("Até breve!")
            continuar = False

    else:
        resposta = input("\nGostaria de descriptografar a mensagem? | 1 - SIM | 2 - NÃO |\n")

        if resposta == "1":
            resultado = descriptografia(resultado_criptografado, codificador_randomico)
            print("\nMensagem descriptografada:", resultado)

            continuar = input("\nGostaria de continuar criptografando? | 1 - SIM | 2 - NÃO |\n")
            continuar = (continuar == "1")

        else:
            print("Até breve!")
            continuar = False
