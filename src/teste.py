import inquirer

chosenAction = inquirer.prompt([
    inquirer.List("action", message="MENU PRINCIPAL\nSelecione uma ação para ser realizada pelo robô", choices=["Home", "Ligar ferramenta", "Desligar ferramenta", "Mover", "Posição atual", "Sair da aplicação"])
])

match chosenAction:
    case "Home": home()
    case "Ligar ferramenta": ligar_ferramenta()
    case "Desligar ferramenta": desligar_ferramenta()
    case "Mover": mover(input("Digite o eixo no qual você deseja mover a ferramenta do robô: ", input("Digite o valor da distância que você deseja mover o robô: ")))
    case "Posição atual": atual()
    case "Sair da aplicação": exit()
