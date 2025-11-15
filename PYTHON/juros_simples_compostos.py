# função principal do programa
def main():
  principal = 2000.00
  taxa = 0.03
  meses = 3
    
  montante = principal * pow((1 + taxa), meses)  
  juros = montante - principal
  
  print("O total de juros a ser pago é:", juros)
  print("O montante a ser pago é:", montante) 
   
if __name__== "__main__":
  main()

# função principal do programa
def main():
  principal = 2000.00
  taxa = 0.03
  meses = 3
  anterior = 0.0
  
  for i in range(1, meses + 1):
    montante = principal * pow((1 + taxa), i)
    juros = montante - principal - anterior
        
    anterior += juros
  
    print("Mês:", i ," - Montante:", montante, "- Juros:", juros)
   
if __name__== "__main__":
  main()

# método principal
def main():
  # um vetor de inteiros contendo sete elementos
  valores = [4, 5, 1, 8, 2, 2, 10]
     
  # o primeiro passo é criar uma variável que vai receber a soma
  # dos valores dos elementos
  soma = 0
 
  # agora vamos usar uma laço for para percorrer todos os elementos
  # do vetor, obter o valor do elemento atual e adicionar ao valor atual
  # da variável soma
  for valor in valores:
    soma = soma + valor
   
  # vamos exibir a soma dos valores do vetor
  print("A soma dos valores do vetor é: {0}".format(soma))
     
if __name__== "__main__":
  main()

# método recursivo que recebe um valor inteiro e o exibe na ordem
# inversa
def exibirInverso(valor):
  # a parada da recursividade é o valor igual a 0
  if valor != 0:
    print(valor % 10, end ="")
    valor = valor // 10
    exibirInverso(valor) # efetua uma nova chamada recursiva
 
# método principal
def main():
  # solicita um valor inteiro ao usuário
  numero = int(input("Informe um valor inteiro: "))
  # exibe o valor na ordem invertida
  print("O valor invertido é: ", end =" ")
  exibirInverso(numero)
   
if __name__== "__main__":
  main()

# função principal do programa
def main():
  # vamos pedir para o usuário informar a força em newtons
  forca = float(input("Força em newtons: "))
 
  # vamos pedir a variação da velocidade em metros por segundo
  velocidade = float(input("Variação da velocidade em metros por segundo: "))
 
  # vamos pedir a variação do tempo em segundos
  tempo = float(input("Variação do tempo em segundos: "))
 
  # agora calculamos a acelaração
  aceleracao = velocidade / tempo
 
  # agora que já temos a aceleracao, podemos calcular a massa
  massa = forca / aceleracao
 
  # e mostramos o resultado
  print("A massa em quilos é: {0}".format(massa))
 
if __name__== "__main__":
  main()

# método principal
def main():
  # vamos solicitar que o usuário informe um ano
  ano = int(input("Informe o ano: "))
     
  # vamos verificar se o ano informado é bissexto
  if(((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0)):
    print("\nO ano informado é bissexto.\n")
  else:
    print("\nO ano informado não é bissexto.\n");
 
if __name__== "__main__":
  main()

# função principal do programa
def main():
  # vamos declarar e construir dois vetores de 10 inteiros
  vetor_a = [0 for x in range(10)]
  vetor_b = [0 for x in range(10)]
 
  # agora vamos pedir para o usuário informar os valores
  # dos elementos do vetor A
  for i in range(len(vetor_a)):
    vetor_a[i] = int(input("Valor do %d.o elemento: " % ((i + 1))))
     
  # vamos construir o vetor B
  for i in range(len(vetor_b)):
    # o índice atual é par?
    if i % 2 == 0:
      vetor_b[i] = vetor_a[i] * 3
    else:
      vetor_b[i] = vetor_a[i] * 2
       
  # vamos mostrar os elementos do vetor A
  print("\nElementos do vetor A:\n")
  for i in range(len(vetor_a)):
    print("%d,  " % vetor_a[i], end=' ')
 
  # vamos mostrar os elementos do vetor B
  print("\n\nElementos do vetor B:\n")
  for i in range(len(vetor_b)):
    print("%d,  " % vetor_b[i], end=' ')
 
if __name__== "__main__":
  main()

# método que recebe dois inteiros e retorna a soma como um número inteiro
def somar(a, b):
  soma = a + b # soma os dois números
  return soma # retorna a soma para o método chamador
 
# função principal do programa
def main():
  # vamos pedir ao usuário que informe dois valores inteiros
  n1 = int(input("Informe o primeiro número: "))
  n2 = int(input("Informe o segundo número: "))
   
  # vamos efetuar uma chamada ao método somar() e obter seu retorno
  resultado = somar(n1, n2)
     
  # finalmente mostramos o resultado
  print("A soma dos dois números é: {0}".format(resultado))
   
if __name__== "__main__":
  main()

# função principal do programa
def main():
  # vamos pedir para o usuário informar uma letra, símbolo ou pontuação
  caractere = input("Informe um caractere: ")
     
  # agora vamos obter o código ASCII correspondente
  codigo = ord(caractere)
     
  # e mostramos o resultado
  print("Você informou o caractere: {0}".format(caractere))
  print("O código ASCII correspondente é: {0}".format(codigo))
     
if __name__== "__main__":
  main()

# método que recebe duas palavras e retorna
# verdadeiro se uma palavra for anagrama da
# outra
def anagramas(palavra1, palavra2):
  # o primeiro passo é verificar se os comprimentos das duas
  # palavras são iguais
  if(len(palavra1) != len(palavra2)):
    return False 
 
  # agora criamos dois dictionaries para as frequencias de
  # cada uma das palavras
  freq_p1 = {}
  freq_p2 = {}
 
  # agora registramos as frequências de letras na primeira
  # palavra
  for letra in palavra1:
    # a letra já está no dicionário?
    if letra in freq_p1:
      freq_p1[letra] += 1 # aumenta a frequêcia desta letra
    else:
      freq_p1[letra] = 1 # ainda não estava no dicionário
 
  # agora registramos as frequências de letras na segunda
  # palavra
  for letra in palavra2:
    # a letra já está no dicionário?
    if letra in freq_p2:
      freq_p2[letra] += 1 # aumenta a frequêcia desta letra
    else:
      freq_p2[letra] = 1 # ainda não estava no dicionário 
 
  # registradas as frequências de letras das duas palavras,
  # chegou a hora de compararmos os dois dicionários
  for chave in freq_p1:
    # esta chave não está no segundo dicionário ou
    # possui valores diferentes?
    if chave not in freq_p2  or freq_p1[chave] != freq_p2[chave]:
      return False 
   
  # se chegou até aqui então uma palavra é anagrama da outra
  return True 
 
def main():
  # vamos ler duas palavras e verificar se uma é anagrama da outra
  palavra1 = input("Informe a primeira palavra: ")
  palavra2 = input("Informe a segunda palavra: ")
 
  # vamos chamar o método que faz a verificação
  if(anagramas(palavra1, palavra2)):
    print("As duas palavras são anagramas")
  else:
    print("As duas palavras não são anagramas")
 
if __name__== "__main__":
  main()

# vamos importar o módulo Math
import math
 
# método principal
def main():
  # vamos pedir para o usuário informar um número inteiro
  numero = int(input("Informe um número inteiro: "))
     
  # vamos obter a quantidade (-1) de dígitos no número informado
  quant = int(math.log10(numero))
  primeiro_digito = (int)(numero / pow(10, quant))
  ultimo_digito = numero % 10
     
  # soma o primeiro e o último dígito
  soma = primeiro_digito + ultimo_digito
     
  # mostra o resultado
  print("A soma do primeiro e do último dígito é: {0}".format(soma))
   
if __name__== "__main__":
  main()

# Calcular o valor da corrida de um táxi em Python
 
# função principal do programa
def main():
  # vamos solicitar a distância da corrida em quilômetros
  distancia_km = int(input("Distância da corrida (km): "))
   
  # sabemos que o valor fixo é R$ 5,00
  valor_fixo = 5.0
 
  # sabemos também que o valor por quilõmetro rodado é R$ 1,50
  valor_km_rodado = 1.5
 
  # então já podemos calcular o valor da corrida
  valor_corrida = valor_fixo + (distancia_km * valor_km_rodado)
 
  # e mostramos o resultado
  print("O valor da corrida foi: R$ {0}".format(valor_corrida))
   
if __name__== "__main__":
  main()

