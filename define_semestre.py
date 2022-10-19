def define_semestre_num(trimestre):
    if trimestre == 1 or trimestre == 2:
        return '1'
    else:
        return '2'

def define_semestre_nome(semestre):
    if semestre == "1":
        return 'Primeiro'
    else:
        return 'Segundo'