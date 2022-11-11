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

def valida_questao(questoes):
    chaves = ["titulo", "nivel", "opcoes", "correta"]
    dic = {}
    for chave in chaves:
        if chave not in questoes:
            dic[chave] = "nao_encontrado" 
    if "titulo" in questoes:
        questoes['titulo']=questoes['titulo'].strip()
        if questoes['titulo']=='':
            dic["titulo"] = "vazio"      
    if len(questoes.keys()) != 4:
        dic["outro"] = "numero_chaves_invalido"     
    if "nivel" in questoes.keys():
        if questoes["nivel"] not in ['facil', "medio", "dificil"]:
            dic["nivel"] = "valor_errado"            
    if "correta" in questoes.keys():
        if questoes["correta"] not in 'ABCD':
            dic["correta"] = "valor_errado"
    if "opcoes" in questoes.keys():
        if len(questoes["opcoes"]) != 4:
            dic["opcoes"] = "tamanho_invalido"
        else:
            if questoes["opcoes"].keys() != {"A", "B", "C", "D"}:
                dic["opcoes"] = "chave_invalida_ou_nao_encontrada"
            else:
                for chav, valor in questoes["opcoes"].items():
                    valor=valor.strip()
                    if valor== '':
                        if "opcoes" not in dic:
                            dic["opcoes"] = {}
                            dic["opcoes"][chav] = "vazia" 
                        else:
                            dic["opcoes"][chav] = "vazia"
    return dic

def valida_questao(questoes):
    chaves = ["titulo", "nivel", "opcoes", "correta"]
    dic = {}
    for chave in chaves:
        if chave not in questoes:
            dic[chave] = "nao_encontrado" 
    if "titulo" in questoes:
        questoes['titulo']=questoes['titulo'].strip()
        if questoes['titulo']=='':
            dic["titulo"] = "vazio"      
    if len(questoes.keys()) != 4:
        dic["outro"] = "numero_chaves_invalido"     
    if "nivel" in questoes.keys():
        if questoes["nivel"] not in ['facil', "medio", "dificil"]:
            dic["nivel"] = "valor_errado"            
    if "correta" in questoes.keys():
        if questoes["correta"] not in 'ABCD':
            dic["correta"] = "valor_errado"
    if "opcoes" in questoes.keys():
        if len(questoes["opcoes"]) != 4:
            dic["opcoes"] = "tamanho_invalido"
        else:
            if questoes["opcoes"].keys() != {"A", "B", "C", "D"}:
                dic["opcoes"] = "chave_invalida_ou_nao_encontrada"
            else:
                for chav, valor in questoes["opcoes"].items():
                    valor=valor.strip()
                    if valor== '':
                        if "opcoes" not in dic:
                            dic["opcoes"] = {}
                            dic["opcoes"][chav] = "vazia" 
                        else:
                            dic["opcoes"][chav] = "vazia"
    return dic


def valida_questoes(questoes):
    list = []
    for y in range(len(questoes)):
        z = valida_questao(questoes[y])
        if z == {}:
            list.append({})
        else:
            list.append(z)
    return list

import random
def sorteia_questao(questoes,nivel):
    questoes[nivel]
    return random.choice(questoes[nivel])

def sorteia_questao_inedita(entrada,nivel, qsorteadas):
    continuar=True
    while continuar:
    
        z = sorteia_questao(entrada,nivel)
        
        if z not in qsorteadas:
            
            qsorteadas.append(z)
            continuar=False

def questao_para_texto(questao,num):
    i = 0
    r = 0
    n = str(num)
    A = 0
    B = 0
    C = 0
    D = 0
    for i in questao:
        if i == "titulo":
            t = questao[i]
        if i == 'opcoes':
            r = questao[i]
    for l in r:
        if l == "A":
            A = r[l]
        elif l == "B":
            B = r[l]
        elif l == "C":
            C = r[l]
        elif l == "D":
            D = r[l]
    res = "----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}".format(n,t,A,B,C,D)
    return res

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
        return 'DICA:\nOpções certamente erradas: ' + sorteado + ' | ' + sorteado2