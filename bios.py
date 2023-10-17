# imports
import os
import sys
import platform
import psutil

from datetime import datetime
from pynput import keyboard
from colored import fore, back, style

from advanced import get_usar_senha
from advanced import set_usar_senha

from boot import get_disp1
from boot import get_disp2
from boot import get_disp3
from boot import save_boot

# ====================================================
# variaveis globais (terão valores alterados)
# ====================================================
menu_ativo = 0
enter = None
item_tela = 0

# dispositivos de boot
disp1 = get_disp1()
disp2 = get_disp2()
disp3 = get_disp3()

# ====================================================
# constantes globais (não serão alteradas)
# ====================================================
color: str = f"{fore('black')}{back('cyan')}"
color_ativo: str = f"{fore('red')}{back('black')}"
color_inativo: str = f"{fore('light_gray')}{back('blue')}"
color_selecionado: str = f"{fore('blue')}{back('light_gray')}"
color_editavel: str = f"{fore('white')}{back('black')}"
color_movendo: str = f"{fore('blue')}{back('black')}"
color_tela: str = f"{fore('black')}{back('light_gray')}"

# ====================================================
# funcoes
# ====================================================


def limpar_tela():
    if (os.name == "posix"):
        os.system("clear")
    else:
        os.system("cls")


def end():
    print(style("reset"))


def atualizar():
    limpar_tela()
    tela()
    end()


def titulo():
    print(f"{color}{'Projeto BIOS':^80}")


def menu():
    print(f"{color_inativo}{' ':^80}")
    main_menu()
    advanced_menu()
    boot_menu()
    exit_menu()


def main_menu():
    sys.stdout.write(f'\x1b[{2};{2}H')
    if (menu_ativo == 0):
        print(f"{color_selecionado}{'Main':^12}")
    else:
        print(f"{color_inativo}{'Main':^12}")


def advanced_menu():
    sys.stdout.write(f'\x1b[{2};{14}H')
    if (menu_ativo == 1):
        print(f"{color_selecionado}{'Advanced':^12}")
    else:
        print(f"{color_inativo}{'Advanced':^12}")


def boot_menu():
    sys.stdout.write(f'\x1b[{2};{26}H')
    if (menu_ativo == 2):
        print(f"{color_selecionado}{'Boot':^12}")
    else:
        print(f"{color_inativo}{'Boot':^12}")


def exit_menu():
    sys.stdout.write(f'\x1b[{2};{38}H')
    if (menu_ativo == 3):
        print(f"{color_selecionado}{'Exit':^12}")
    else:
        print(f"{color_inativo}{'Exit':^12}")


def rodape():
    string = ' Enter: Selecionar menu   \u2191\u2193: Navegar valores   \u2190\u2192: Navegar menus'
    string2 = ' + -: Alterar valores     q: Sair'
    sys.stdout.write(f'\x1b[{22};{0}H')
    print(f"{color}{string:80}")
    sys.stdout.write(f'\x1b[{23};{0}H')
    print(f"{color}{string2:80}")


def tela():
    global menu_ativo

    titulo()
    menu()
    if (menu_ativo == 0):
        main_tela()
    elif (menu_ativo == 1):
        advanced_tela()
    elif (menu_ativo == 2):
        boot_tela()
    elif (menu_ativo == 3):
        mexit_tela()
    rodape()


def main_tela():
    for i in range(3, 23):
        sys.stdout.write(f'\x1b[{i};{0}H')
        print(f"{color_tela}{' ':80}")

    sys.stdout.write(f'\x1b[{5};{6}H')
    d = datetime.now()
    data = datetime.strftime(d, "%d/%m/%Y")
    print(f"{color_tela}Data: {data}")

    sys.stdout.write(f'\x1b[{8};{6}H')
    print(f"{color_tela}Computer network name: {platform.node()}")
    sys.stdout.write(f'\x1b[{9};{6}H')
    print(f"{color_tela}Machine type: {platform.machine()}")
    sys.stdout.write(f'\x1b[{10};{6}H')
    print(f"{color_tela}Processor type: {platform.processor()}")
    sys.stdout.write(f'\x1b[{11};{6}H')
    print(f"{color_tela}Platform type: {platform.platform()}")
    sys.stdout.write(f'\x1b[{12};{6}H')
    print(f"{color_tela}Operating system: {platform.system()}")
    sys.stdout.write(f'\x1b[{13};{6}H')
    print(f"{color_tela}Operating system release: {platform.release()}")
    sys.stdout.write(f'\x1b[{14};{6}H')
    print(f"{color_tela}Operating system version: {platform.version()}")
    sys.stdout.write(f'\x1b[{15};{6}H')
    ramTotal = psutil.virtual_memory().total / 1024 / 1024 / 1014
    print(f"{color_tela}Memória RAM instalada: {ramTotal:.1f} GB")


def advanced_tela():
    usarSenha = get_usar_senha()

    for i in range(3, 23):
        sys.stdout.write(f'\x1b[{i};{0}H')
        print(f"{color_tela}{' ':80}")

    sys.stdout.write(f'\x1b[{8};{6}H')

    if (menu_ativo != 1 or enter == None):
        if (not usarSenha):
            print(f"{color_tela}Usar senha: {color_ativo} Off ")
            sys.stdout.write(f'\x1b[{9};{6}H')
            print(f"{color_tela}Senha: {color_editavel}    ")
        else:
            print(f"{color_tela}Usar senha: {color_ativo} On ")
            sys.stdout.write(f'\x1b[{9};{6}H')
            print(f"{color_tela}Senha: {color_editavel}    ")
    else:
        if (item_tela == 0):
            if (not usarSenha):
                print(f"{color_tela}Usar senha: {color_movendo} Off ")
                sys.stdout.write(f'\x1b[{9};{6}H')
                print(f"{color_tela}Senha: {color_editavel}    ")
            else:
                print(f"{color_tela}Usar senha: {color_movendo} On ")
                sys.stdout.write(f'\x1b[{9};{6}H')
                print(f"{color_tela}Senha: {color_editavel}1234")
        elif (item_tela == 1):
            if (not usarSenha):
                print(f"{color_tela}Usar senha: {color_ativo} Off ")
                sys.stdout.write(f'\x1b[{9};{6}H')
                print(f"{color_tela}Senha: {color_movendo}    ")
            else:
                print(f"{color_tela}Usar senha: {color_ativo} On ")
                sys.stdout.write(f'\x1b[{9};{6}H')
                print(f"{color_tela}Senha: {color_movendo}1234")


def boot_tela():
    global disp1
    global disp2
    global disp3

    for i in range(3, 23):
        sys.stdout.write(f'\x1b[{i};{0}H')
        print(f"{color_tela}{' ':80}")

    sys.stdout.write(f'\x1b[{8};{6}H')

    if (menu_ativo != 2 or enter == None):
        print(f"{color_tela}1º dispositivo de boot: {color_editavel}{disp1}")
        sys.stdout.write(f'\x1b[{9};{6}H')
        print(f"{color_tela}2º dispositivo de boot: {color_editavel}{disp2}")
        sys.stdout.write(f'\x1b[{10};{6}H')
        print(f"{color_tela}3º dispositivo de boot: {color_editavel}{disp3}")
    else:
        if (item_tela == 0):
            print(f"{color_tela}1º dispositivo de boot: {color_movendo}{disp1}")
        else:
            print(f"{color_tela}1º dispositivo de boot: {color_editavel}{disp1}")

        sys.stdout.write(f'\x1b[{9};{6}H')

        if (item_tela == 1):
            print(f"{color_tela}2º dispositivo de boot: {color_movendo}{disp2}")
        else:
            print(f"{color_tela}2º dispositivo de boot: {color_editavel}{disp2}")

        sys.stdout.write(f'\x1b[{10};{6}H')

        if (item_tela == 2):
            print(f"{color_tela}3º dispositivo de boot: {color_movendo}{disp3}")
        else:
            print(f"{color_tela}3º dispositivo de boot: {color_editavel}{disp3}")


def mexit_tela():
    for i in range(3, 23):
        sys.stdout.write(f'\x1b[{i};{0}H')
        print(f"{color_tela}{' ':80}")

    sys.stdout.write(f'\x1b[{8};{6}H')
    print(f"{color_tela}Pressione ENTER para sair!")


# ====================================================
# eventos
# ====================================================
def on_press(key):
    global menu_ativo
    global enter
    global item_tela
    global disp1
    global disp2
    global disp3

    try:
        if (key.char == 'q' or key.char == 'Q'):
            exit()
        # Adicionei o caractere "=", pois em alguns teclados, a tecla do + digita = por padrão.
        elif ((key.char == '+' or key.char == "=") and enter != None):
            if (menu_ativo == 1):
                set_usar_senha("1234")
            elif (menu_ativo == 2):
                if (item_tela == 0):
                    aux = disp1
                    disp1 = disp2
                    disp2 = aux
                elif (item_tela == 1):
                    aux = disp2
                    disp2 = disp3
                    disp3 = aux
                elif (item_tela == 2):
                    aux = disp1
                    disp1 = disp3
                    disp3 = aux

                save_boot(disp1=disp1, disp2=disp2, disp3=disp3)
        elif (key.char == '-' and enter != None):
            if (menu_ativo == 1):
                set_usar_senha("")
            elif (menu_ativo == 2):
                if (item_tela == 0):
                    aux = disp1
                    disp1 = disp3
                    disp3 = aux

                elif (item_tela == 1):
                    aux = disp1
                    disp1 = disp2
                    disp2 = aux

                elif (item_tela == 2):
                    aux = disp2
                    disp2 = disp3
                    disp3 = aux

                save_boot(disp1=disp1, disp2=disp2, disp3=disp3)

    except AttributeError:
        mod = 1
        if (enter == 0):
            mod = 1
        elif (enter == 1):
            mod = 2
        elif (enter == 2):
            mod = 3

        if (key == keyboard.Key.up and enter != None):
            item_tela = ((item_tela - 1) + mod) % mod

        elif (key == keyboard.Key.down and enter != None):
            item_tela = ((item_tela + 1) + mod) % mod

        elif (key == keyboard.Key.left):
            menu_ativo = ((menu_ativo - 1) + 4) % 4
            item_tela = 0
            enter = None

        elif (key == keyboard.Key.right):
            menu_ativo = ((menu_ativo + 1) + 4) % 4
            item_tela = 0
            enter = None

        elif (menu_ativo == 3) and (key == keyboard.Key.enter):
            exit()
        elif (key == keyboard.Key.enter):
            enter = menu_ativo
            item_tela = 0

            if (menu_ativo == 2):
                save_boot(disp1, disp2, disp3)

    atualizar()


def on_release(key):
    if key == keyboard.Key.esc:
        return False


# main
try:
    atualizar()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

except:
    limpar_tela()
    print("BIOS finalizada!")
