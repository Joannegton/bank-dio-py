
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Qual o valor deseja Depositar?"))
        if valor > 0:
            print(f"O valor de {valor} foi depositado com sucesso.")
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! Valor informado é inválido!.")

    elif opcao == 2:
        valor = float(input("Qual o valor deseja sacar? "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"Operação falhou! Você não tem saldo suficiente.\nSaldo restante: R${saldo}.")
        elif excedeu_limite:
            print(f"Operação falhou! Seu limite é de R${limite} por saque.")
        elif excedeu_saque:
            print("Operação falhou! Você ja realizou os 3 saques diários.")

        elif valor > 0:
            saldo -= valor
            numero_saques +=1
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao == 0:
        break

    else:
         print("Operação inválida, por favor selecione novamente a operação desejada.")

