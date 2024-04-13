menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = False
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if(opcao == "d"):
        valor=float(input("Insira o valor do deposito: "))
        saldo = saldo + valor
        extrato = True
        print("Extrato: {:.2f}".format(saldo))
    elif(opcao == "s"):
        valor=float(input("Insira o valor do saque: "))
        insuficiente = valor > saldo
        excedido = valor > limite
        nro_saques = numero_saques >= LIMITE_SAQUES
        if insuficiente:
            print("Saldo Insuficiente para Saque")
        elif excedido:
            print("Limite de Valor de Saque Excedido")
        elif nro_saques:
            print("Limite de Saques Excedido")
        elif valor <= 0:
            print("Valor invalido")
        else:
            saldo = saldo - valor
            numero_saques = numero_saques + 1
            print("Saque Realizado!")
            print("Extrato: {:.2f}".format(saldo))
    elif(opcao == "e"):
        if(extrato):
            print("Extrato: {:.2f}".format(saldo))
        else:
            print("Ainda nao foi realizado nenhum deposito.")
    elif (opcao == "q"):
        break
    else:
        print("Opcao invalida")

        

