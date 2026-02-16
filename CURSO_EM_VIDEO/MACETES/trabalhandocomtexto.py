# Inversão de Texto.
while True:
    
    txt = str(input('\033[0;32m\nDigite o texto: \033[m'))[::-1]
    print(txt)   
    resp = " "
    while resp not in "10":
        resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break
    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")


# Maiúsculas & Minúsculas.
texto = input('Digite algo: ')
# texto = "Aprendendo Python na disciplina de linguagem de programação."
print(f"texto = {texto}")
print(f"Tamanho do texto = {len(texto)}\n")

palavras = texto.split()
palavras = texto.upper()
print(f"palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")


# Tamanho do texto.
texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 3 primeiras letras são: {texto[0:3]}")


# Análise Completa de Nome.
n = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome letras maiúsculas é: {}.".format(n.upper()))
print("Seu nome em letras minúsculas é {}.".format(n.lower()))
print("Seu nome tem {} letras.".format(len(n)-n.count(" ")))
# print("Seu primeiro nome tem {} letras.".format(n.find(" ")))
separa = n.split()
print("Seu primeiro nome é {} e tem {} letras.\n".format(separa[0], len(separa[0])))


# Primeiro Nome e Último Sobrenome.
n = str(input("Digite seu nome completo: ")).strip()
n = n.split()
print("Prazer em te conhecer {}!".format(n[0]))
print("Seu primeiro nome é {}.".format(n[0]))
print("Seu último nome é: {}\n".format(n[len(n)-1]))


# Análise de Letra Específica.
frase = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase.".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A útima letra A apareceu na posição {}\n".format(frase.rfind("A")+1))

arquivo = open("bancodedados.txt", "a")
file = input('Digite algo: ')
arquivo.write(file)

# Lendo o arquivo criado:
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()

# Acrescentando texto ao arquivo criado, usando o modo de acesso 'a'
print("\n")
texto = input("Digite uma frase para acrescentar ao arquivo:\n")
arquivo = open('arq01.txt','a')
arquivo.write(texto + "\n")
print("Opera��o conclu�da no arquivo " + arquivo.name + " usando o modo de acesso " + arquivo.mode)
arquivo.close()

print("\nTexto alterado:")
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()

# Acrescentando texto ao in�cio do arquivo, usando o modo 'r+'
print("\n")
texto = input("Digite um titulo para acrescentar ao arquivo:\n")
arquivo = open('arq01.txt','r+')
arquivo.seek(0)
arquivo.write(texto + '\n')
arquivo.close()

print("\nTexto alterado:")
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()

arquivo = open("bancodedados.txt", "a")
file = input('Digite algo: ')
arquivo.write(file)


# solution...?
arquivo = open("texto.txt", "a")

frases = list()
frases.append("TreinaWeb \n")
frases.append("Python \n")
frases.append("Arquivos \n")
frases.append("Django \n")

arquivo.writelines(frases)