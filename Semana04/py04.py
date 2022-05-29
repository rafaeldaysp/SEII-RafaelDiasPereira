nome = ['Rafael', 'Dias', 'Pereira']

nome.insert(1, 'Days')

str = ['Hello', 'World']
nome.append(str)
print(nome)

nome.extend(str)
print(nome)

nome.remove(str)
nome.remove('Dias')
print(nome)

nome.pop()
nome.pop()
print(nome)

nome.reverse()
print(nome)

nome.sort()
print(nome)

print(nome.index('Days'))

for index, palavra in enumerate(nome):
    print(index, palavra)

nome_str = ' '.join(nome)
print(nome_str)

nome_list = nome_str.split(' ')
print(nome)

tupla = ('Rafael', 'Days')
print(tupla)

set = {'Rafael', 'Dias', 'Pereira'}
set2 = {'Rafael', 'Days', 'Pereira'}
print(set.intersection(set2))
print(set.difference(set2))
print(set.union(set2))

