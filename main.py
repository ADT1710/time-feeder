from datetime import datetime, timedelta, time, date
from pymysql import cursors
from define_dia_semana import define_dia_semana
from define_semana import define_semana
from define_mes_nome import define_mes_nome
from define_trimestre import define_trimestre_num, define_trimestre_nome
from define_semestre import define_semestre_num, define_semestre_nome

data_inicial = datetime.strptime('01/01/2000', '%d/%m/%Y')
data_final = datetime.strptime('31/12/2022', '%d/%m/%Y')

diferenca = (data_final - data_inicial).days

for dia in range(diferenca):
    data = data_inicial + timedelta(dia+1)

    dia_semana = define_dia_semana(data.weekday())
    semana = define_semana(data.day)

    mes_num = data.month
    mes_nome = define_mes_nome(mes_num)

    ano = data.year

    trimestre_num = define_trimestre_num(mes_num)
    trimestre_nome = define_trimestre_nome(trimestre_num)

    semestre_num = define_semestre_num(int(trimestre_num))
    semestre_nome = define_semestre_nome(semestre_num)

    cod_dia = data.strftime('%Y%m%d')
    dia_mes = data.strftime('%m%d')
    mes_ano = data.strftime('%Y%m')

    data_formatada = data.strftime("%Y-%m-%d")

    print(f'{cod_dia} | {dia_mes} | {mes_ano} |{data_formatada} | {dia_semana} | {semana} | {mes_num} - {mes_nome} | {trimestre_num} - {trimestre_nome} | {semestre_num} | {semestre_nome}')