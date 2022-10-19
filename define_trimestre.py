def define_trimestre_num(mes):
    mes = str(mes)
    if mes in ['1','2','3']:
        return '1'
    elif mes in ['4','5','6']:
        return '2'
    elif mes in ['7','8','9']:
        return '3'
    elif mes in ['10','11','12']:
        return '4'

def define_trimestre_nome(trimestre):
    nomes = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto']
    return nomes[int(trimestre)-1]