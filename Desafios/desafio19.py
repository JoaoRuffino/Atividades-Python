import random
name1 = input('Digite o nome do(a) primeiro(a) aluno(a): ')
name2 = input('Digite o nome do(a) segundo(a) aluno(a): ')
name3 = input('Digite o nome do(a) terceiro(a) aluno(a): ')
name4 = input('Digite o nome do(a) quarto(a) aluno(a):')

print('O(A) aluno(a) sorteado(a) é {}'.format(random.choice([name1, name2, name3, name4])))