def get_disp1():
    with open("boot.txt", "r") as file:
        linha = file.readline()
        disp1 = linha.replace("\n", "")

    return disp1


def get_disp2():
    with open("boot.txt", "r") as file:
        _ = file.readline()
        linha = file.readline()
        disp2 = linha.replace("\n", "")

    return disp2


def get_disp3():
    with open("boot.txt", "r") as file:
        _ = file.readline()
        _ = file.readline()
        linha = file.readline()
        disp3 = linha.replace("\n", "")

    return disp3


def save_boot(disp1, disp2, disp3):
    with open("boot.txt", "w") as file:
        file.writelines([
            (disp1 + "\n"),
            (disp2 + "\n"),
            (disp3 + "\n"),
        ])
