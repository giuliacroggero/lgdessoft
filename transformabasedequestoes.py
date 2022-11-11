def transforma_base(questoes):
    dic2 = {}
    lista1 = []
    lista2 = []
    lista3 = []
    i = 0
    for i in range(len(questoes)):
        v=questoes[i]['nivel']
        if v== 'facil':
            lista1.append(questoes[i])
            dic2['facil'] = lista1 
        elif v== 'medio':
            lista2.append(questoes[i])
            dic2['medio'] = lista2
        elif v== 'dificil':
            lista3.append(questoes[i])
            dic2['dificil'] = lista3 
    return dic2