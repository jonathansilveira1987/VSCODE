num = int(input("\nDigite um número inteiro: "))

print("\n{} convertido para BINÁRIO é igual a \033[0;32m{}\033[m.\n".format(num, bin(num)[2:]))
print("{} convertido para OCTAL é igual a \033[0;32m{}\033[m.\n".format(num, oct(num)[2:]))
print("{} convertido para HEXADECIMAL é igual a \033[0;32m{}\033[m.\n".format(num, hex(num)[2:]))