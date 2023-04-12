"""
Montando a calculadora dnv na sequencia certa: 

-> Ja montado: 
    I -> Montado o "cabesalho" mostrando os modulos que podem ser escolhidos 
    II -> Criado o modulo 1 (soma...)
    III -> CRIAR a Potenciação
    IV -> Criado a conversão 
    V -> Porcentagem

     
"""
# Apresentação ao usuário (Modulos que pode ser escolhido)
print("Operações possiveis: \n 1 - soma, multiplicação, divisão\n 2 - Equação 2° grau \n 3 - Potenciação \n 4 - Conversão \n 5 - Porcentagem")
print("=" * 80) #usado para organizar as informações p/ usuário na saída de inf.

# 1° -> Perguntando o usuário qual o tipo de operação desejada 
moduloOperacao = int(input("Informe a operação desejada: "))

print("=" * 80) #usado para organizar as informações p/ usuário na saída de inf.

#Criando a estrutura de decisão responsavel por selecionar a opção de operação escolhida
if moduloOperacao == 1: # Caso seja escolhido o modulo 1 (soma, divisão e mult.)
        
    num1 = float(input("Informe o 1° numero: "))
    # Perguntando se o usuário quer somar, dividir ou multiplicar
    operacao = input("Qual operação deseja? (+ , - , /) :")
    operacao = operacao.upper() # Transformando a resposta em maiuscula 
    num2 = float(input("Informe o 2° numero: "))

    # Criando a estrutura de desição p/ saber se deve somar, dividir, mult. ou subtrair
    if operacao == "+": # Caso queira somar
        soma = num1 + num2
        print(f"\nA soma dos valores resulta em: {round(soma, 2)}")

    elif operacao == "*": # Caso queira multiplicar
        mult = num1 * num2
        print(f"\nA multiplicação dos valores resulta em: {round(mult, 2)}")
    
    elif operacao == "/": # Caso queira dividir
        divi = num1 / num2
        print(f"\nA divisão dos valores resulta em: {round(divi, 2)}")
    
    elif operacao == "-": # Caso queira subtrair
        subi = num1 - num2
        print(f"\nA divisão dos valores resulta em: {round(subi, 2)}")

    else:
        print("\nOperação impossivel")
##############################################################################################
# Acabou aqui a criação do "1" que é responsavel por somar, dividir, multiplicar e subtrair
##############################################################################################

# criando a parte de equação 2° grau: 
elif moduloOperacao == 2: 
    a = float(input("Informe o valor de A: "))
    b = float(input("Informe o valor de B: "))
    c = float(input("Informe o valor de C: "))

    print("=" * 80) #usado para organizar as informações p/ usuário na saída de inf.
    # formula é: aX² + bX + c 
    # formula de delta: b² + 4ac
    delta = (b**2) - (4 * (a) * (c))
    raizD = delta ** 0.5

    x1 = ((-b) + raizD) / (2*a)
    x2 = ((-b) - raizD) / (2*a)


    print(f"\nX1 = {x1:.2f}")
    print(f"X2 = {x2:.2f}")
    
##############################################################################################
# Acabou aqui a criação do "2" que é responsavel pela equação de 2° grau
##############################################################################################

# Criando a parte da potenciação 
if moduloOperacao == 3: 
    n1 = float(input("Informe 1° numero: "))
    n2 = float(input("Informe a potenciação: "))

    potenciacao = n1 ** n2
    print(f"\n{n1} elevado a {n2} resulta em {round(potenciacao, 2)}")

    
##############################################################################################
# Acabou aqui a criação do "3" que é responsavel pela regra de 3 
##############################################################################################

# criando a parte de conversão: 
elif moduloOperacao == 4: 
    # definindo qual o tipo de conversão o usuário deseja
    conversao = int(input("1 - M p/ CM  |  2 - CM p/ M | 3 - Kg p/ g  |  4 - g p/ Kg \nInforme qual o tipode conversão desejada: "))

    # Estrutura de decisão p/ fazer a conversão desejada 
    if conversao == 1: # caso seja de Metros p/ Cm
        m = float(input("Informe o valor em Metros: "))
        cm = m * 100
        print(f"\n{m} metros equivale a {round(cm, 2)} centimetros")
    
    elif conversao == 2: # caso seja Cm p/ Metros 
        cm = float(input("Informe o valor em Centimetros: "))
        m = cm / 100
        print(f"\n{cm} centimetros equivale a {round(m, 2)} metros")
    
    elif conversao == 3: # caso seja Kg p/ G
        kg = float(input("Informe o valor em KG: " ))
        g = kg * 1000
        print(f"\n{kg} Kg equivale a {round(cm, 2)} centimetros")
    
    elif conversao == 4: # caso seja de G p/ KG 
        g = float(input("Informe o valor em Gramas: "))
        kg = g / 1000
        print(f"\n{g} G equivale a {round(kg, 2)} Kg")
    else: 
        print("\nOperação imposivel")

##############################################################################################
# Acabou aqui a criação do "4" que é responsavel pela conversão  
##############################################################################################

# Criando a parte de  Porcentagem: 
elif moduloOperacao == 5: 
    num1 = float(input("Informe o valor referente a 100%: "))
    num2 = float(input("Informe a porcentagem desejada: "))
    porc = num1 * (num2 / 100)

    print(f"{num2} se refere a {round(porc, 2)}% do valor completo")
    


