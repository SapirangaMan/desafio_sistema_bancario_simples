menu = """
    Bem vindo ao banco Sapiranga, favor selecionar a opção abaixo:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()
    if opcao == 'd':
        deposito = float(input("Favor informar valor para depósito: \n"))
        saldo += deposito
        extrato += f"\n Deposito efetuado no valor de: R${deposito}"
        
    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários")
            break
        else:
            saque = float(input("Favor informar valor de saque: \n"))
            if saque > 500:
                print("O limite para cada saque é de R$ 500,00")
                continue
            if (saldo - saque) < 0:
                print (saldo-saque)
                print("Saldo insuficiente para essa operção")
            else:
                numero_saques += 1
                saldo -= saque
                extrato += f"\n Saque efetuado no valor de: R${saque}"
        
    elif opcao == 'e':
        if extrato == "":
            print("Não foram realizadas movimentações")
        else:
            print("Extrato: \n", extrato)
            print(f"Seu saldo é de {saldo}")
    
    elif opcao == 'q':
        print("Obrigado por usar o banco Sapiranga")
        break