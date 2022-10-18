def define_semana(dia):
    if dia >= 1 and dia <= 7:
        return 1
    elif dia >= 8 and dia <= 14:
        return 2
    elif dia >= 15 and dia <= 21:
        return 3
    elif dia >= 22:
        return 4