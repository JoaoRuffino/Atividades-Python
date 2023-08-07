import random
name1 = input('Digite o nome do(a) primeiro(a) aluno(a): ')
name2 = input('Digite o nome do(a) segundo(a) aluno(a): ')
name3 = input('Digite o nome do(a) terceiro(a) aluno(a): ')
name4 = input('Digite o nome do(a) quarto(a) aluno(a):')

lista = [name1, name2, name3, name4]

random.shuffle(lista)

print('A ordem de apresentação será {}'.format(lista))