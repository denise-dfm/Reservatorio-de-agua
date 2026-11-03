from colorama import Fore, Style, init

# Inicializa o Colorama
init()

# Lista com as mensagens de cada nível
mensagens = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Retorna a cor correspondente ao nível informado
def definir_cor(nivel):
    cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]
    return cores[nivel - 1]

while True:
    nivel = int(input("\nDigite o nível do reservatório (1 a 5) ou 0 para sair: "))

    # Encerra o programa
    if nivel == 0:
        print("Sistema encerrado.")
        break

    # Verifica se o nível é válido
    if 1 <= nivel <= 5:
        print(definir_cor(nivel) + mensagens[nivel - 1])
        print(Style.RESET_ALL)  # Restaura a cor padrão
    else:
        print("Nível inválido!")
