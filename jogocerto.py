import random 
from funcoes import *
from questoes import *

dicio2 = transforma_base(questoes)
                         
f = valida_questoes(dicio2['facil'])
m = valida_questoes(dicio2['medio'])
d = valida_questoes(dicio2['dificil'])

tamanhof = len(f)
tamanhom = len(m)
tamanhod = len(d)
somaf = 0
somam = 0
somad = 0

for a in f:
   if a == {}:
      somaf += 1
for a in m:
   if a == {}:
      somam += 1
for a in d:
   if a == {}:
      somad += 1
if somaf == tamanhof and somam == tamanhom and somad == tamanhod:
   continuar = True
   
   while continuar:

      menu()

      lista_jafoi=[]
      nivel='facil'
      cont_nivel= 0
      ajudac = 2
      pular = 3
      jafoia = 0
      listavalidos = ['ajuda', 'pula', 'parar', 'A', 'B', 'C', 'D']
      continuar2 = True
      
      while continuar2:
          
        if cont_nivel == 3:
            nivel='medio'
            print('HEY! Você passou para o nível MEDIO!')
        elif cont_nivel ==6:
            nivel= 'dificil'
            print('HEY! Você passou para o nível DIFICIL!')
        
        if cont_nivel == 0 and jafoia!= 1:
            questao=sorteia_questao(dicio2,nivel)
            lista_jafoi.append(questao)
        if cont_nivel > 0 and jafoia != 1:
            questao= sorteia_questao_inedita(dicio2,nivel,lista_jafoi)
            lista_jafoi.append(questao)
        
        listaopcoes = ['A', 'B', 'C', 'D']
        listaerradas = []

        pergunta = questao_para_texto(questao,cont_nivel+1)
        print(pergunta)
        
        
        resposta=input('Qual sua resposta?! ')
        respostac = questao['correta']
        
        for v in listaopcoes:
            if v != respostac:
                listaerradas.append(v)
                
        if resposta == questao['correta'] :
            jafoia = 0
            print ('\33[32mVocê acertou! Seu prêmio atual é de')
            enter = input('\33[0mAperte ENTER para continuar')
            cont_nivel+=1
            
        if resposta in listaerradas:
            print ('\33[32mVocê errou!')
            enter = input('\33[0mAperte ENTER para continuar')
            continuar= False
            continuar2=False
            
        if resposta == 'ajuda':
            ajudac = ajudac - 1
            cont_nivel = cont_nivel - 1
            chamaajuda = gera_ajuda(questao)
            
            if jafoia == 1:
                print('\33[35mNão deu! Você não tem mais direito a ajuda!')
                enter = input('\33[0mAperte ENTER para continuar')
                cont_nivel+=1
                
            if jafoia == 0:
                print('\33[0mOk, lá vem ajuda! Você ainda tem {} ajudas!'.format(ajudac))
                enter = input('\33[0mAperte ENTER para continuar')
                print(chamaajuda)
                jafoia += 1
                enter = input('\33[0mAperte ENTER para continuar')
                cont_nivel+=1
                
        if resposta not in listavalidos:
                print('\33[31mOpção inválida\n\33[36mAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
                resposta=input('\n\n\33[0mQual sua resposta?! ')
                cont_nivel  = - 2

            
        cont_nivel = cont_nivel + 1