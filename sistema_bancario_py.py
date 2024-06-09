import sys

#input para selecionar o tipo de conta
conta = int(input("[1] Normal [2] Universitária \ninforme o tipo da conta: "))
#validando o tipo de conta
if conta == 1:
    conta_normal = True
    conta_universitaria = False
elif conta == 2:
    conta_universitaria = True
    conta_normal = False
else:
    sys.exit("Opção inválida")
#input pede para o usuario informar o valor do saque
saque = float(input("informe o valor do saque: "))
saldo = 2000
cheque_especial = 450
#Verifica as condições de saque para c/c normal
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente!")
#Verifica as condições de saque para c/c universitaria
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente!")
