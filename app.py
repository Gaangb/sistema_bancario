saldo = 300
escolha = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while escolha != 4:
    print('''
    --------MENU--------
        (1) Depositar
        (2) Sacar
        (3) Extrato
        (4) Finalizar
''')
    escolha = int(input())

    if escolha == 1:
        valor =  float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
        
        else:
            print("Operação falhou: O valor informado é invalido.")

    elif escolha == 2:
        value = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos")
        
        elif valor > 0:
            saldo += valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1

        else:
            print("Operação falhou! O valor informado é invalido")
    

    elif escolha == 3:
        print("\n========== EXTRATO ==========")
        print("Não foram encontradas movimentações." if not extrato else extrato)
        print(f"\nSaldo R$: {saldo:.2f}")
        print("=============================")
    
    elif escolha == 4:
        break

    else:
        print("Operação invalida! Tente novamente.")
    
