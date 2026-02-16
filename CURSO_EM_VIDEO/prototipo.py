















































'''


















arquivo = open("bancodedados.txt", "a")
file = input('Digite algo: ')
arquivo.write(file)




arquivo = open("texto.txt", "a")

frases = list()
frases.append("TreinaWeb \n")
frases.append("Python \n")
frases.append("Arquivos \n")
frases.append("Django \n")

arquivo.writelines(frases)






































list = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
for i in range(0, 4):
    print(list[i][1], end='')



'''