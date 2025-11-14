import time
import sys

def desenha_logo():
    print(r"""
██████╗  ██████╗ ███╗   ██╗██████╗ ███████╗██╗  ██╗██╗███████╗████████╗ ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔════╝██║  ██║██║██╔════╝╚══██╔══╝██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██████╔╝███████║██╔██╗ ██║██║  ██║███████╗███████║██║█████╗     ██║   ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██╔══██╗██╔══██║██║╚██╗██║██║  ██║╚════██║██╔══██║██║██╔══╝     ██║   ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
██║  ██║██║  ██║██║ ╚████║██████╔╝███████║██║  ██║██║██║        ██║   ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝    ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""")

def random_excesso():
    num = 0
    while num == 0:
        tempo = int(time.time() * 1000000)
        M = 2**31
        X0 = tempo % M
        A = 15
        B = 13
        X1 = (A * X0 + B) % M
        R1 = X1 / M
        num = int(R1 * 100) % 10
    return num

def criar_arquivo_texto(texto):
    arquivo = open('arquivo.txt', 'w', encoding='utf-8')
    arquivo.write(texto)
    arquivo.close()

def inversao_caracteres(lista):
    lista.reverse()
    return ''.join(lista)

def loading():
    for _ in range(3):
        for ponto in "...":
            sys.stdout.write(ponto)
            sys.stdout.flush()
            time.sleep(0.2)
        print()

def criptografia(texto, codificador):
    texto_criptografado = ""
    lista_texto_criptografado = ""

    for caracter in texto:
        if ord(caracter) + codificador >= 127:
            texto_criptografado += chr((ord(caracter) - 95) + codificador)
        else:
            texto_criptografado += chr(ord(caracter) + codificador)

        lista_texto_criptografado = list(texto_criptografado)

    loading()

    resultado_final = inversao_caracteres(lista_texto_criptografado)
    criar_arquivo_texto(resultado_final)
    return resultado_final

def descriptografia(texto, codificador):
    lista_reversa = list(texto)
    lista_reversa.reverse()

    resultado = ""
    for caracter in lista_reversa:
        if ord(caracter) - codificador < 32:
            resultado += chr((ord(caracter) + 95) - codificador)
        else:
            resultado += chr(ord(caracter) - codificador)
    return resultado
