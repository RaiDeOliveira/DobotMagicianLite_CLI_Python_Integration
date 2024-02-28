from colorama import Fore, Back
from serial.tools import list_ports
import inquirer
import pydobot
import yaspin
import typer
import time

# line commands definitions

# move the claw back to the main position
def home():
    loading.start()
    robot.move_to(200, 0, 0, 0)
    loading.stop()
    mainMenu()

# turns the claw on
def ligar_ferramenta():
    robot.suck(True)
    mainMenu()

# turns the claw off
def desligar_ferramenta():
    robot.suck(False)
    mainMenu()

# moves the claw by a given distance on a given axys
def mover(axys: str, distance: float):
    current_position = robot.pose()
    loading.start()
    match axys:
        case "x":
            robot.move_to(distance, current_position[1], current_position[2], current_position[3])
        case "y":
            robot.move_to(current_position[0], distance, current_position[2], current_position[3])
        case "z":
            robot.move_to(current_position[0], current_position[1], distance, current_position[3])
        case "r":
            robot.move_to(current_position[0], current_position[1], current_position[2], distance)
    loading.stop()
    mainMenu()

# prints and returns current claw position
def atual():
    current_position = robot.pose()

    print(f"\n\nPosição atual do robô:\n X:{current_position[0]}\n Y:{current_position[1]}\n Z:{current_position[2]}\n R:{current_position[3]}\n")

    mainMenu()

# loading symbol instance
loading = yaspin.yaspin(text="Em andamento...", color="yellow")

# initial menu

### introduction text ###
print(Back.LIGHTBLACK_EX + Fore.YELLOW + "Seja bem vindo ao Clidobot!")

print("Sua interface de linha de comando favorita para controlar o Dobot Magician Lite! :D")

print(Back.BLACK + Fore.WHITE + "\nPrimeiro, selecione a porta USB na qual o robô que você quer controlar está conectado. Se nenhuma aparecer, certifique-se de que o robô está ligado e conectado.")
#########################

def mainMenu():
    chosenAction = inquirer.prompt([
        inquirer.List("action", message="MENU PRINCIPAL\nSelecione uma ação para ser realizada pelo robô", choices=["Home", "Ligar ferramenta", "Desligar ferramenta", "Mover", "Posição atual", "Sair da aplicação"])
    ])

    match chosenAction["action"]:
        case "Home":
            home()
        case "Ligar ferramenta":
            ligar_ferramenta()
        case "Desligar ferramenta":
            desligar_ferramenta()
        case "Mover":
            axys = input("Digite o eixo no qual você deseja mover a ferramenta do robô: ")
            distance = float(input("Digite o valor da distância que você deseja mover o robô: "))
            mover(axys, distance)
        case "Posição atual":
            atual()
        case "Sair da aplicação": 
            robot.close()
            exit()

# lists all of the USB ports that are currently being used to connect to other devices
connectedUsbPorts = list_ports.comports()

# allows the user to choose which one of the connected USB ports to use
chosenUsbPort = inquirer.prompt([
    inquirer.List("port", message="Selecione a porta:", choices=[port.device for port in connectedUsbPorts])
])["port"]

# Dobot Magician Lite robot instance
robot = pydobot.Dobot(port=chosenUsbPort)
robot.speed(200, 200)

mainMenu()