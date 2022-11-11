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