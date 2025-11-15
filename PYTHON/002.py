# Validação de dados
palavra = input("\nDigite algo (letras e espaços): ")
if palavra.replace(" ", "").isalpha():
    print(f"\nVocê digitou: {palavra}")
else:
    print("\nÉ permitido apenas digitação de letras, aplicação encerrada!")






'''

while True:
    palavra = input("\nDigite algo (apenas letras e espaços): ")
    if palavra.replace(" ", "").isalpha():
        print(f"\nVocê digitou: {palavra}\n")
        break
    else:
        print("\nÉ permitido apenas digitação de letras, tente novamente!")


while True:
    try:
        numero = int(input("\nDigite um número inteiro: "))
        print(f"\nO número digitado foi: {numero}")
        break
    except ValueError:
        print("\nPor favor, digite um número inteiro válido.") 
print()



'''