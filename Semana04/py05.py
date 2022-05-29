dicionario = {'Nome': 'Rafael', 'Idade': 21, 'Curso': 'SEMB2'}
print(dicionario)

dicionario['telefone'] = '34991504641'
print(dicionario.get('Telefone'))

dicionario.update({'Nome': 'Rafael Days'})
print(dicionario)

del dicionario['Idade']
print(dicionario)

print(len(dicionario))
print(dicionario.keys())
print(dicionario.values())

for key, value in dicionario.items():
    print(f'{key}: {value}')
    
