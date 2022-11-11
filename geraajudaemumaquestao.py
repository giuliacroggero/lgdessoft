import random
def gera_ajuda(dicquestao):
    correta = dicquestao['correta']
    erradas = 'ABCD'.replace(correta, '')
    qntd = random.choice([1,2])
    if qntd == 1:
        sorteio = random.choice(erradas)
        dicop = dicquestao['opcoes']
        sorteado = dicop[sorteio]
        return 'DICA:\nOpções certamente erradas: ' + sorteado
    else:
        sorteio = random.choice(erradas)
        dicop = dicquestao['opcoes']
        sorteado = dicop[sorteio]
        erradas = erradas.replace(sorteio, '')
        sorteio = random.choice(erradas)
        sorteado2 = dicop[sorteio]
        return 'DICA:\nOpções certamente erradas: ' + sorteado + ' | '  + sorteado2
    
