lista = [3, 2, 1, -4, -6, 5]
print(sorted(lista))
print(sorted(lista, reverse=True, key=abs))

class Objeto():
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    def __repr__(self) -> str:
        return f'({self.nome}, {self.idade}, {self.curso})'


user1 = Objeto('rafael', '21', 'automação')
user2 = Objeto('days', '21', 'controle')
user3 = Objeto('dias', '21', 'engenharia')
usuarios = [user1, user2, user3]


print(sorted(usuarios, key=lambda user: user.nome))

from operator import attrgetter

print(sorted(usuarios, key=attrgetter('curso')))

