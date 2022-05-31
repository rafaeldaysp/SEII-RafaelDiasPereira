
with open('teste.txt', 'w') as f:
    f.write('Rafael Days\n')
    f.write('hello world')
    print(f.mode)

with open('teste.txt', 'r') as f:
    conteudo = f.read(6)
    print(conteudo)
    conteudo = f.read()
    print(conteudo)
    print(f.tell())
    f.seek(0)
    print(f.read(6))
    
with open('teste.txt', 'r') as f:
    with open('teste2_copy.txt', 'w') as f2:
        for linha in f.read():
            f2.write(linha)