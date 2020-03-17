import random
x = 1

while x == 1:
    ef = 1
    quant = int(input("Digite o tamanho da senha:\n"))
    char = str(input("A senha terá caracteres? y/n:\n"))
    num = str(input("A senha terá números? y/n\n"))
    sym = str(input("A senha terá simbolos especiais? y/n\n"))

    carac = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd''E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K',
             'k','L', 'l', 'M', 'm','N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
             'V', 'v', 'W', 'w', 'X', 'x','Y', 'y', 'Z', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    espc = ['!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '-', '_', '+', '=', '"', ' ']
    password = []
    if ((char == 'N' or char == 'n') and (num == 'N' or num == 'n')and (sym == 'N' or sym == 'n')):
        print("Não é possivel criar uma senha vazia.\n")
        ef = 0
    else:
        for i in range(0, quant):
            if ((char == 'Y' or char == 'y') and (num == 'Y' or num == 'y') and (sym == 'Y' or sym == 'y')):
                password.append(random.choice(carac))
                password.append(random.choice(numbers))
                password.append(random.choice(espc))
            elif ((char == 'Y' or char == 'y') and (num == 'Y' or num == 'y') and (sym == 'N' or sym == 'n')):
                password.append(random.choice(carac))
                password.append(random.choice(number))
            elif ((char == 'Y' or char == 'y') and (num == 'N' or num == 'n') and (sym == 'N' or sym == 'n')):
                password.append(random.choice(carac))
            elif ((char == 'N' or char == 'n') and (num == 'Y' or num == 'y') and (sym == 'Y'or sym == 'y')):
                password.append(random.choice(numbers))
                password.append(random.choice(espc))
            elif ((char == 'Y' or char == 'y') and (num == 'N' or num == 'n') and (sym == 'Y' or sym == 'y')):
                password.append(random.choice(carac))
                password.append(random.choice(espc))
            elif ((char == 'N' or char == 'n') and (num == 'N' or num == 'n') and (sym == 'Y' or sym == 'y')):
                password.append(random.choice(espc))
            elif ((char == 'N' or char == 'n') and (num == 'Y' or num == 'y') and (sym == 'N' or sym == 'n')):
                password.append(random.choice(numbers))
            #elif (nyn)
    if (ef == 1):
        for i in range(0, quant):
            print(password[i], end="")
        print('\n')
