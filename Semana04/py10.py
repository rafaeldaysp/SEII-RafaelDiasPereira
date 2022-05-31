import os
from datetime import datetime

os.chdir('/home/rafael/Documents/semb2/Semana04')

os.mkdir('pasta-teste')

print(os.getcwd())

print(os.listdir())

os.rmdir('pasta-teste')

file_path = os.environ.get('HOME') + '/teste.txt'

print(file_path)

print(datetime.fromtimestamp(os.stat(file_path).st_mtime))