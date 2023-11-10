import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COL = 3

contador_simbolos = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

contador_valor = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

def checar_vencedor(colunas, linhas, bet, valor):
    vencedor = 0
    linhas_vencedor = []
    for linha in range(linhas):
        simbolos = set(coluna[linha] for coluna in colunas)
        if len(simbolos) == 1:  # Se houver apenas um símbolo na linha
            simbolo = simbolos.pop()
            vencedor += valor[simbolo] * bet
            linhas_vencedor.append(linha + 1)
    return vencedor, linhas_vencedor



def pegar_rodada_da_slot_machine(linhas, colunas, contador_simbolos):
    todos_os_simbolos = []
    for simbolo, contador in contador_simbolos.items():
        for _ in range(contador):
            todos_os_simbolos.append(simbolo)

    resultados_colunas = []
    for _ in range(colunas):
        coluna = []
        simbolos_atuais = todos_os_simbolos[:]
        for _ in range(linhas):
            valor = random.choice(simbolos_atuais)
            coluna.append(valor)
            simbolos_atuais.remove(valor)  # Evita que o mesmo símbolo apareça mais de uma vez na mesma coluna
        resultados_colunas.append(coluna)

    return resultados_colunas

def print_slot_machine(colunas):
    for linha in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(colunas) - 1:
                print(coluna[linha], "| ", end="")
            else:
                print(coluna[linha], end="")
        print()




def deposito():
    while True:
        amount = input("Quanto gostaria de depositar? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("A quantidade depositada precisa ser maior que zero")
        else:
            print("Por favor, digite um número")

    return amount


def numero_linhas():
    while True:
        linhas = input("Digite o número de linhas para apostar (1-" + str(MAX_LINES) + ")? ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAX_LINES:
                break
            else:
                print("Digite um número válido de linhas")
        else:
            print("Por favor, digite um número")

    return linhas


def valor_aposta():
    while True:
        amount = input("Quanto gostaria de apostar?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"A quantidade depositada precisa ser entre ${MIN_BET} - ${MAX_BET}")
        else:
            print("Por favor, digite um número")

    return amount

def rodada(amount):
    linhas = numero_linhas()
    while True:
        aposta = valor_aposta()
        total_aposta = aposta * linhas
        if total_aposta > amount:
            print(f"Você não possui saldo suficiente para essa aposta, seu saldo é de: ${amount}")
        else:
            break

    print(f"Você está apostando ${aposta} em {linhas} linhas. Sua aposta total é de : R${total_aposta}")

    slots = pegar_rodada_da_slot_machine(ROWS, COL, contador_simbolos)
    print_slot_machine(slots)
    vencedor, linhas_vencedor = checar_vencedor(slots,linhas, aposta, contador_valor)
    print(f"Você ganhou {vencedor}.")
    print(f"Você ganhou nas linhas: ", *linhas_vencedor)
    return vencedor - total_aposta


def main():
    amount = deposito()
    while True:
        print(f"Saldo atual é: {amount}")
        spin =  input("Aperte enter para iniciar (Para sair digite sair)")
        if spin == "sair":
            break
        amount += rodada(amount)

    print(f"Você saiu com {amount}")



main()
