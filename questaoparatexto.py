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