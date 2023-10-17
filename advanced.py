def get_usar_senha():
    with open("advanced.txt", "r") as file:
        line = file.readline()

        if (line == "False\n"):
            return False
        elif (line == "True\n"):
            return True


def set_usar_senha(senha=""):
    with open("advanced.txt", "w") as file:
        if (len(senha) == 0):
            file.write("False\n")
        else:
            file.writelines([
                "True\n",
                (senha + "\n")
            ])
