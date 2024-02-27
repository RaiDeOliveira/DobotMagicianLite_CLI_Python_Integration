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
    robot.move_to(200, 0, 0, 0)

# turns the claw on
def ligar_ferramenta():
    robot.suck(True)

# turns the claw off
def desligar_ferramenta():
    robot.suck(False)

# moves the claw by a given distance on a given axys
def mover(axys: str, distance: float):
    current_position = robot.pose()
    match axys:
        case "x":
            robot.move_to(distance, current_position[1], current_position[2], current_position[3])
        case "y":
            robot.move_to(current_position[0], distance, current_position[2], current_position[3])
        case "z":
            robot.move_to(current_position[0], current_position[1], distance, current_position[3])
        case "r":
            robot.move_to(current_position[0], current_position[1], current_position[2], distance)

# prints and returns current claw position
def atual():
    current_position = robot.pose()

    print(f"\n\nPosição atual do robô:\n X:{current_position[0]}\n Y:{current_position[1]}\n Z:{current_position[2]}\n R:{current_position[3]}\n")
    
    return [current_position[0], current_position[1], current_position[2], current_position[3]]

# loading symbol instance
loading = yaspin.yaspin(text="Em andamento...", color="yellow")



### introduction text ###
print(Back.LIGHTBLACK_EX + Fore.YELLOW + "Seja bem vindo ao Clidobot!")

print("Sua interface de linha de comando favorita para controlar o Dobot Magician Lite! :D")

print(Back.BLACK + Fore.WHITE + "\nPrimeiro, selecione a porta USB na qual o robô que você quer controlar está conectado. Se nenhuma aparecer, certifique-se de que o robô está ligado e conectado.")
#########################



# lists all of the USB ports that are currently being used to connect to other devices
connectedUsbPorts = list_ports.comports()

# allows the user to choose which one of the connected USB ports to use
chosenUsbPort = inquirer.prompt([
    inquirer.List("port", message="Selecione a porta:", choices=[port.device for port in connectedUsbPorts])
])["port"]

# Dobot Magician Lite robot instance
robot = pydobot.Dobot(port=chosenUsbPort)
robot.speed(200, 200)


loading.start()
home()
time.sleep(3)
ligar_ferramenta()
atual()
loading.stop()


loading.start()
mover("y", -200)
mover("z", 100)
time.sleep(3)
desligar_ferramenta()
atual()
loading.stop()





# Fecha a conexão com o robô
robot.close()