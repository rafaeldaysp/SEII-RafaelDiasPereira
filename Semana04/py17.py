import datetime

data = datetime.date.today()

print('{}/{}/{}'.format(data.day, data.month, data.year))

tempo = datetime.timedelta(days=2)

alarme = data + tempo

print(f'Alarme definido para o dia {alarme}, para daqui {tempo.total_seconds()/float(60^2)} horas')


