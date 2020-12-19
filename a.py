import math
# Questão 1
count = 0
for i in range(1, 5000001, 1):
    if i%49 == 0 and i%37 == 0 and i%2 == 0:
        count +=1
print(count)

# Questão 2

x = []
for i in range(10):
    if i%2 == 0:
        X = 3**i + 7*(math.factorial(i))
    else:
        X = 2**i + 4*math.log(i)
    x.append(X)
num = 0
soma = 0
posicao = 0
count = 0
for a in x:
    soma += a
    if a > num:
        num = a
        posicao = count
    count += 1
media = soma / 10
print('o maior número está na posição {0}'.format(posicao))
print('a média é {0:.2f}'.format(media))

# Questão 3
aluno_1 = 5
aluno_2 = 6
aluno_3 = 1
aluno_4 = 8
aluno_5 = 10
li = [aluno_1, aluno_2, aluno_3, aluno_4, aluno_5]
dici = {}
for i in range(1, 6):
    print('a nota do aluno {0} é {1}'.format(i, li[i-1]))
    dici['aluno {0}'.format(i)] = li[i-1]
c = 0
n = ''
for j,i in dici.items():
    if i > c:
        c = i
        n = j

print('o nome é: {0} e a nota foi: {1}'.format(n, c))


