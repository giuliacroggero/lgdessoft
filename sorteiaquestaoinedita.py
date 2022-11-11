import random
def sorteia_questao(questoes,nivel):
    questoes[nivel]
    return random.choice(questoes[nivel])
def sorteia_questao_inedita(questoes,nivel, questoes_sorteadas):
    y = sorteia_questao(questoes,nivel)
    if y not in questoes_sorteadas:
        questoes_sorteadas.append(y)
    return y