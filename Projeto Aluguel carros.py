# Criando as lisas necessárias para guardar as informações: 
#Parte referente ao cadástro de veículos
classe = []
modelo = []
marca  = []
placa  = []
cor    = []
tipo   = []
combustivel = []
vlrDiaria   = []
observacao  = []

# Parte referente ao cadástro de clientes 
nomes   = []
cpf     = []
tipoCnh = []
numCNH  = []
valiCNH = []
ende    = []
tel     = []
atvProf = []


# precis adicionar um loop de repetição ao cadastrar o carro p/ depois que cadastrar o programa perguntar o que fazer dnv

tipoServico = int(input("1- Cadastrar carros | 2- Cadastrar clientes \n3- aluguel automoveis | 4- Devolução automoveis \nR: "))
print("=" * 80)

# Caso deseje cadastrar um carro 
if tipoServico == 1:
       
    # começando com o cadastro de carros 
    senhaAdm = 1234

   
    controleCadastroCarro = 1
    while controleCadastroCarro > 0: 

         
         # 1.1: 
        senha = int(input("Informe a sua senha: "))
        # validando a senha 
        if senha == senhaAdm: 
            # se a senha estiver certa...   
            # abrindo cadastro para os veículos 
            classeVeiculo = int(input("Qual a classe do veículo? \n1- simples | 2- mediano | 3- luxuosos | 4- onibus e caminhões\nR: "))
            print("=" * 80)
            modeloVei = input("Informe qual o modelo do automovel: ")
            print("=" * 80)
            marcaVei = input("Qual a marca do veículo: ")
            print("=" * 80)
            placaVei = input("Insira a placa do automovel: ")
            print("=" * 80)
            corVei  = input("Insira a cor do automovel: ")
            print("=" * 80)
            tipoVei = int(input("1- SUV ----- 2- Ret    ----- 3- Caminhonete \n4- Van ----- 5- Onibus ----- 6- Caminhão \nR: "))
            print("=" * 80)
            combustivelVei = int(input("1- alcool \n2- gasolina \n3- hibrido \n4- eletrico \nR: "))
            print("=" * 80)
            vlrDiariaVei = float(input("Diária aluguel R$ "))
            print("=" * 80)
            observacaoVei = input("Observações: ")
            print("=" * 80)


            # Adicionando as informações nas listas necessárias 
            classe.append(classeVeiculo)
            modelo.append(modeloVei.upper())
            marca.append(marcaVei.upper())
            placa.append(placaVei.upper())
            cor.append(corVei.upper())
            tipo.append(tipoVei)
            combustivel.append(combustivelVei)
            vlrDiaria.append(vlrDiariaVei)
            observacao.append(observacaoVei.upper())

            print(f"O veiculo {modelo[-1]} foi gravado com sucesso!!")

            continuarCadastroC = int(input("Deseja continuar cadastrando novos carros? (1- Sim | 2- Não) "))

            if continuarCadastroC == 1: 
                controleCadastroCarro += 1 
            else:
                print("Programa encerrado")
                controleCadastroCarro = 0 

        
        # depois observar o loop de erro de senha novamente!!!! 
        else:
            print("Senha incorreta!")
            erroSenha = 0      
                
            # O loop de errar a senha n está funcionando.... 
            if erroSenha < 5: 
                print("Tente a senha novamente")
                controleCadastroCarro += 1
                erroSenha += 1 
            else: 
                print(f"Você ja tentou entrar {erroSenha} vezes sem Sucesso \nPrograma encerrado")
                controleCadastroCarro = 0
                break



# caso deseje cadastrar um cliente novo...     
elif tipoServico == 2: 

    nomeCli = input("Informe o nome: ")
    cpfCli = int(input("Informe seu cpf: "))
    tipoCNHcli = input("Qual o tipo da sua CNH: ")
    numCNHcli = int(input("Informe o numero da sua CNH: "))
    valiCNHcli = input("Informe a validade da sua CNH: ")
    endereco = input("Informe seu endereço: ")
    telefoneCli = int(input("Informe seu telefone: "))
    atividadeCli = input("Informe sua profissão: ")


    # Adicionando as informações necessárias 
    nomes.append(nomeCli.upper())
    cpf.append(cpfCli)
    tipoCnh.append(tipoCNHcli.upper())
    numCNH.append(numCNHcli)
    valiCNH.append(valiCNHcli)
    ende.append(endereco.upper())
    tel.append(telefoneCli)
    atvProf.append(atividadeCli.upper())

    print(f"O cliente {nomes[-1]} foi gravado com sucesso!")


     
