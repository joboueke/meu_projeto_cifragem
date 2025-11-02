import base64
import os

# Caminho relativo do arquivo de texto
CAMINHO_ARQUIVO = "meutexto.txt"

# Verifica se o arquivo existe antes de continuar
if not os.path.exists(CAMINHO_ARQUIVO):
    print(f"Arquivo '{CAMINHO_ARQUIVO}' não encontrado! Coloque-o na mesma pasta do script.")
    exit()

# Lê o conteúdo do arquivo
with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivoTexto:
    texto = arquivoTexto.read()


def cifragemPorInversao(texto):
    textoEmLista = texto.split()    
    listaTextoInvertido = []

    for palavra in reversed(textoEmLista):
        palavraInvertida = palavra[::-1]
        listaTextoInvertido.append(palavraInvertida)

    textoInvertido = " ".join(listaTextoInvertido)

    with open("Meu Texto Invertido.txt", "a", encoding="utf-8") as textoInvertidoTXT:
        textoInvertidoTXT.write(textoInvertido + "\n")

    print("Texto invertido gerado em 'Meu Texto Invertido.txt'")


def cifragemPorDeslocamento(texto):
    alfabeto = {letra: idx for idx, letra in enumerate('abcdefghijklmnopqrstuvwxyz')}
    alfabeto_invertido = {idx: letra for letra, idx in alfabeto.items()}

    textoEmMinuscula = texto.lower()
    listaDeslocada = []

    while True:
        try:
            deslocamento = int(input("Insira o número de letras a serem deslocadas (0 a 25): "))
            if 0 <= deslocamento <= 25:
                break
            else:
                print("Valor inválido! O número de deslocamentos deve ser entre 0 e 25.")
        except ValueError:
            print("Por favor, insira um número válido.")

    for i in textoEmMinuscula:
        if i in alfabeto:
            posicao = alfabeto[i]
            novaPosicao = (posicao + deslocamento) % 26
            listaDeslocada.append(alfabeto_invertido[novaPosicao])
        else:
            listaDeslocada.append(i)

    textoDeslocado = ''.join(listaDeslocada)

    with open("Meu Texto Deslocado.txt", "a", encoding="utf-8") as textoDeslocadoTXT:
        textoDeslocadoTXT.write(textoDeslocado + "\n")

    print(f"Texto deslocado salvo em 'Meu Texto Deslocado.txt'")
    print(f"Texto cifrado: {textoDeslocado}")


def mascaraSubstituicao():
    with open(CAMINHO_ARQUIVO, "rb") as arquivoOriginalTXT:
        conteudoOriginal = arquivoOriginalTXT.read()
        textoMascarado = base64.b64encode(conteudoOriginal)
        textoDesmascarado = base64.b64decode(textoMascarado)

    textoMascaradoString = textoMascarado.decode("utf-8")

    with open("Meu Texto Mascarado.txt", "a", encoding="utf-8") as textoMascaradoTXT:
        textoMascaradoTXT.write(textoMascaradoString + "\n")

    print("Texto mascarado salvo em 'Meu Texto Mascarado.txt'")
    print(f"Texto original: {conteudoOriginal}")
    print(f"Texto mascarado (base64): {textoMascarado}")
    print(f"Texto desmascarado: {textoDesmascarado}")


def meuMenu():
    while True:
        try:
            opcao = int(input(
                "\n-------------------------------\n"
                "Selecione a opção de cifragem desejada:\n\n"
                "1 - Cifragem por inversão\n"
                "2 - Cifragem por deslocamento\n"
                "3 - Cifragem por substituição (Base64)\n"
                "4 - Sair\n\n"
                "Insira a opção escolhida: "
            ))

            if opcao == 1:
                cifragemPorInversao(texto)
            elif opcao == 2:
                cifragemPorDeslocamento(texto)
            elif opcao == 3:
                mascaraSubstituicao()
            elif opcao == 4:
                print("👋 Adeus!")
                break
            else:
                print("Opção inválida. Escolha entre 1 e 4.")
        except ValueError:
            print("Por favor, insira apenas números de 1 a 4.")


if __name__ == "__main__":
    meuMenu()
