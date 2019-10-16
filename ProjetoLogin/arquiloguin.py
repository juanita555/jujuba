sair = True
podeIr = True

while sair:

    print("O que você faz no centro?")
    print("1- Coordenador; 2- Mentor; 3- Membros; 4- sair")
    perg = str(input())

    if perg == "1":
        print('Insira a senha')
        sen = input("Senha: ")
        while sen != "123":
            print("Senha digitada incorreta!!!")
            print("Por favor digite a senha correta")
            sen = input("Senha: ")

        print("Seja bem vindo Coordenador!")

    elif perg == "2":
        while podeIr:
            print("Qual é a sua area de trabalho? Nós temos as seguintes divisões")
            print("1- DEV; 2- COM; 3-DG; 4- DI; 5-AV; 6- IF; 7- ADM")
            AT = str(input())

            if AT == "1":
                senat1 = input("Senha: ")
                while senat1 != "abc":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senat1 = input("Senha: ")
                print('Bem vindo(a) mentor de DEV!!!! <3 <3')
                podeIr = False
            elif AT == "2":
                senat2 = input("Senha: ")
                while senat2 != "def":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senat2 = input('Senha: ')
                print('Seja bem vindo(a) mentor(a) de Comunicação!!!')
                podeIr = False

            elif AT == "3":
                senat3 = input('Senha: ')
                while senat3 != "hij":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senat3 = input(" Senha: ")
                print('Seja bem vindo(a) mentor(a) de Design Grafico!!!')
                podeIr = False

            elif AT == "4":
                senat4 = input('Senha: ')
                while senat4 != "klm":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senat4 = input('Senha: ')
                print('Seja bem vindo(a) mentor(a) de Design de Interface!!!')
                podeIr = False

            elif AT == "5":
                senat5 = input('Senha: ')
                while senat5 != "nop":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senat5 = input('Senha: ')
                print('Seja bem vindo(a) mentor(a) de Audio Visual!!!')
                podeIr = False

            elif AT == "6":
                senat6 = input('Senha: ')
                while senat6 != "qrs":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senat6 = input('Senha: ')
                print('Seja bem vindo(a) mentor(a) de Infraestrutura!!!')
                podeIr = False

            elif AT == "7":
                senat7 = input('Senha: ')
                while senat7 != "tuv":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senat7 = input('Senha: ')
                print('Seja bem vindo(a) mentor(a) de Adiministração!!!')
                podeIr = False

            else:
                print('Essa não é uma área do Centro, \nPor favor excolha uma das opções. \n')
                # print("Qual é a sua area de trabalho? Nós temos as seguintes divisões")
                # print("1- DEV; 2- COM; 3-DG; 4- DI; 5-AV; 6- IF; 7- ADM")
                # AT = str(input())



    elif perg == "3":
        podeIr = True
        while podeIr:
            print('Qual a sua área de trabalho? Nós possuimos as seguintes divisões; ')
            print(' 1- DEV; 2- COM; 3- DG; 4- DI; 5- AV; 6- IF; 7- ADM;')
            ATM = int(input())

            if ATM == 1:
                senmat1 = input('Senha: ')
                while senmat1 != "devaqui":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senmat1 = input(' Senha: ')
                print('Bem vindo(a) membro de DEV!!! <3 <3 <3 <3')
                podeIr = False

            elif ATM == 2:
                senmat2 = input('Senha: ')
                while senmat2 != "comaqui":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senmat2 = input(' Senha: ')
                print('Seja bem vindo(a) membro de Comunicação !!!')
                podeIr = False

            elif ATM == 3:
                senmat3 = input('Senha: ')
                while senmat3 != "dgaqui":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senmat3 = input(' Senha: ')
                print('Bem vindo(a) membro de Design Grafico !!!')
                podeIr = False

            elif ATM == 4:
                senmat4 = input('Senha: ')
                while senmat4 != "diaqui":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senmat4 = input(' Senha: ')
                print('Bem vindo(a) membro de Design de Interiores !!!')
                podeIr = False

            elif ATM == 5:
                senmat5 = input('Senha: ')
                while senmat5 != "avaqui":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senmat5 = input(' Senha: ')
                print('Bem vindo(a) membro de Audio Visual !!!')
                podeIr = False

            elif ATM == 6:
                print('Bem vindo(a) membro de DEV!!! <3 <3 <3 <3')
                senmat6 = input('Senha: ')
                while senmat6 != "ifaqui":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senmat6 = input(' Senha: ')
                print('Bem vindo(a) membro de INFRA!!!')
                podeIr = False

            elif ATM == 7:
                senmat7 = input('Senha: ')
                while senmat7 != "admaqui":
                    print('senha incorreta!!!')
                    print('por favor digite a senha certa.')
                    senmat7 = input(' Senha: ')
                print('Bem vindo(a) membro de Adiministração !!!')
                podeIr = False

            else:
                print('Essa não é uma opção!')

    elif perg == "4":
        sair = False