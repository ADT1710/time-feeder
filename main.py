from datetime import datetime, timedelta, time, date
from pymysql import cursors

data_inicial = datetime.strptime('01/01/2000', '%d/%m/%Y')
data_final = datetime.strptime('31/12/2022', '%d/%m/%Y')

diferenca = (data_final - data_inicial).days

for dia in range(diferenca):
    print(data_inicial + timedelta(dia+1))