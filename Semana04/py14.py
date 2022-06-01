import os
import random
import matplotlib 

try:
    os.mkdir('teste')
except:
    pass

os.chdir(os.getcwd() + '/teste')

for i in range(10):
    with open(random.choice(('teste-', 'testando-', 'nome-', 'arquivo-')) + str(random.randint(1, 10)) + '.txt', 'a') as f:
        f.write('Rafael')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_num = f_name.split('-')
    f_num.zfill(2)
    novo_formato = '{}-{}{}'.format(f_num, f_title, f_ext)
    os.rename(f, novo_formato)
    