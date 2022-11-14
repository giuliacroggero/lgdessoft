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
valor_lista = [0,1000,5000,10000,30000,50000,100000,300000,500000,1000000]
v_i = 0

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
      val = 0
      questao=sorteia_questao(dicio2,nivel)
      lista_jafoi.append(questao)
      
      while continuar2:
          
        if cont_nivel == 3:
            nivel='medio'
            print('HEY! Você passou para o nível MEDIO!')
        elif cont_nivel ==6:
            nivel= 'dificil'
            print('HEY! Você passou para o nível DIFICIL!')
        
        if cont_nivel >= 0 and jafoia != 1 and val != 0:
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
            v_i = v_i+1
            print ('\33[32mVocê acertou! Seu prêmio atual é de {}'.format(valor_lista[v_i]))
            
            if valor_lista[v_i] == 1000000:
                print('Você é o novo milionário!')
                continuar2 = False
                continuar = False
                
            enter = input('\33[0mAperte ENTER para continuar')
            cont_nivel+=1
            
        if resposta in listaerradas:
            print ('\33[32mVocê errou!')
            enter = input('\33[0mAperte ENTER para continuar')
            play_again = input('Deseja jogar novamente? (s/n) ')
            
            if play_again == 's':
               v_i = 0
               continuar= True
               continuar2= True
               lista_jafoi=[]
               nivel='facil'
               cont_nivel= 0
               ajudac = 2
               pular = 3
               jafoia = 0
               listavalidos = ['ajuda', 'pula', 'parar', 'A', 'B', 'C', 'D']
               continuar2 = True
               val = 0
               questao=sorteia_questao(dicio2,nivel)
               lista_jafoi.append(questao)
            if play_again == 'n':
                print('Obrigado por jogar!')
                continuar= False
                continuar2= False
            
            
        if resposta == 'ajuda':
            val = 0
            chamaajuda = gera_ajuda(questao)
            ajudac = ajudac - 1
            
            if ajudac < 0:
                print('Você já usou todas as suas ajudas!')
                enter = input('\33[0mAperte ENTER para continuar')
            
            
            
            
            
            elif jafoia == 1:
                print('\33[35mNão deu! Você não tem mais direito a ajuda!')
                enter = input('\33[0mAperte ENTER para continuar')
                
            elif jafoia == 0:
                
                if ajudac == 0:
                    print("Você usou sua ultima ajuda")
                else:
                    print('\33[0mOk, lá vem ajuda! Você ainda tem {} ajudas!'.format(ajudac))
                enter = input('\33[0mAperte ENTER para continuar')
                print(chamaajuda)
                jafoia += 1
                enter = input('\33[0mAperte ENTER para continuar')
                

                
        if resposta not in listavalidos:
            print('\33[31mOpção inválida\n\33[36mAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
            val = 0
            resposta=input('\n\n\33[0mQual sua resposta?! ')
        else:
            val = 1
            
        if resposta == 'pula':
            if pular == 0:
                print('\33[35mNão deu! Você não tem mais direito a pular!')
                enter = input('\33[0mAperte ENTER para continuar')
                val = 0
            else:
                val = 1
                pular = pular - 1
                print('\33[0mOk, você pulou a questão! Você ainda tem {} pulos!'.format(pular))
                cont_nivel = cont_nivel + 1
            
        if resposta == 'parar':
            continuar2 = False
            continuar = False
            print('\33[0mOk, você parou o jogo! Sua premiação é {}'.format(valor_lista[v_i]))
            play_again = input('Deseja jogar novamente? (s/n) ')
            
            if play_again == 's':
               v_i = 0
               continuar= True
               continuar2= True
               lista_jafoi=[]
               nivel='facil'
               cont_nivel= 0
               ajudac = 2
               pular = 3
               jafoia = 0
               listavalidos = ['ajuda', 'pula', 'parar', 'A', 'B', 'C', 'D']
               continuar2 = True
               val = 0
               questao=sorteia_questao(dicio2,nivel)
               lista_jafoi.append(questao)
            if play_again == 'n':
                print('Obrigado por jogar!')
                continuar= False
                continuar2= False
            