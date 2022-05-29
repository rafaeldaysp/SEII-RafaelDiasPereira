def sqr(num):
    return num*num

def func(*args, **kwargs):
    print(args)
    print(kwargs)

x = sqr(2)
print(x)

tupla = (1, 2, 3)
dic = {'Nome': 'Rafael', 'Curso': 'Automação'}
func(*tupla, **dic)