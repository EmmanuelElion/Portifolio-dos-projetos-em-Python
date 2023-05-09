""" 
I - O programa deverá pedir o valor da banca inicial 
II - devera calcular apenas 5% do valor da banca p/ apostar 
III - o programa deverá perguntar quanto o usuário apostou, se teve green ou red, no caso de green deve perguntar quanto % teve ( Ex: 1.5 ...)
IV - assim que o usuário tiver 4 red seguidos o programa deverá sugerir com que o usuário pare de apostar por pelo menos 1h 

Ao final de cada "turno" de apostas o programa deverá apresentar um balanço da quantidade de greens, reds, qual o lucro ou prejuizo, quanto que foi investido ao todo 
e qanto que retornou ao todo 
alem da porcentagem de lucro e de sua porcentagem de rendimento no jogo 

"""
# Criando listas para assim poder gravar os valores das apostas e etc... 
green = [] # lista para gravar as odds de green 
lucro = [] # lista para gravar os lucros obtidos 
red = [] # lista para gravar os red 
banca = [] # lista para fazer o controle da banca 

jogadas = 1 # variavel criada para saber quantas jogadas teve (pode servir como controle de laço de repetição)


# Resolvendo o I item: 
bancaInicial = float(input("Banca inicial = R$ "))
banca.append(bancaInicial) 

print("=" * 80)

# Resolvendo o II item: 
apostar = bancaInicial * 0.05
print(f"Você deve apostar apenas 5% da banca, sendo assim R$ {apostar}")
print("=" * 80)


# é preciso adicionar o começo do loop AQUI!!! 
while jogadas > 0: 
      
    # Resolvendo o III item: 
    vlrApostado = float(input("Qual o valor apostado? R$ ")) # reconhecendo o valor apostado 

    # perguntando ao usuário se foi green ou red 
    resultado = int(input("A aposta doi Green ou red? (1-Green | 2-Red) "))

    if resultado == 1: # se o resultado for green...
        # vendo qual foi a odd 
        oddGreen = float(input("Qual foi a odd ganha? "))
        ganho = (vlrApostado * oddGreen) + vlrApostado
        lucroJogada = ganho - vlrApostado # lucro que teve na operação 
        
        # add as informações na lista 
        lucro.append(lucroJogada) # add o lucro na lista 
        green.append(oddGreen) # add a odd de green 
        
        # fazendo o calculo da banca final 
        bancaFinal = (sum(banca) + sum(lucro)) - sum(red)

        print("=" * 80)
        print(f"Você apostou {vlrApostado} e ganhou uma odd de {oddGreen} % assim tendo um ganho de R${ganho} e um lucro de R${lucro}")
        print(f"Sua banca está com o saldo de R${bancaFinal}")
        print("=" * 80)

        # vendo se o usuário quer continuar apostando 
        continuar = int(input("Deseja continuar apostando? (1- Sim | 2- Não) "))
        
        if continuar == 1: 
            jogadas += 1 
        
        elif continuar == 2: 
            break             

    elif resultado == 2: 
        # vendo quanto o usuário perdeu 
        vlrPerdido = vlrApostado

        #add as informações a lista 
        red.append(vlrPerdido)


        # fazendo o calculo da banca final 
        bancaFinal = (sum(banca) + sum(lucro)) - sum(red)

        print("=" * 80)
        print(f"Você acabou tendo um Red. Teve um prejuizo de R${vlrPerdido}")
        print(f"Sua banca está com o saldo de R${bancaFinal}")
        print("=" * 80)

        # vendo se o usuário quer continuar apostando 
        continuar = int(input("Deseja continuar apostando? (1- Sim | 2- Não) "))
            
        if continuar == 1: 
            jogadas += 1 
            
        elif continuar == 2: 
            break     

bancaFinalTotal = (sum(banca) + sum(lucro)) - sum(red)

print("=" * 100)
print(f"Area para o balanço final \n Você realizou {jogadas} jogadas")
print(f"Sua banca final é R$ {bancaFinalTotal}")


