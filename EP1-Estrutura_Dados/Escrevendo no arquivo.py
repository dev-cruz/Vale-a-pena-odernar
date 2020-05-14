arq = open('Ep1-Douglas_JoãoCruz.txt','w')
arq.write(" ------------------------EP1 ------------------------\n")
arq.write(" Aluno: Douglas Henrique Teixeira Barboza\n"
                   "\tJoão Victor Cruz")
arq.close()

arq = open('Ep1-Douglas_JoãoCruz.txt','r')
for line in arq:
    line = line.rstrip()
    print(line)
arq.close()
