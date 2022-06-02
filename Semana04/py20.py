try:
    f = open('teste.txt')
except:
    print('Arquivo não encontrado')
else:
    print(f.read())
    f.close()
finally:
    print('Fim do programa')