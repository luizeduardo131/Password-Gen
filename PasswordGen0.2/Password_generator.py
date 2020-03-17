'''
version:Beta 0.2
Creator:Luiz Eduardo
12/03/2020
'''

import random

x = 1
a = False
d = False
f = open("passwerds.txt", "a")
def chamachar():
    char = str(input("A senha terá caracteres? y/n:\n"))


def chamanum():
    num = str(input("A senha terá números? y/n\n"))


def chamasym():
    sym = str(input("A senha terá simbolos especiais? y/n\n"))


def chamachoice():
    choice = input('Você deseja criar outra senha? y/n\n')
print(')__________________________________________(')
print('SEJA BEM VINDO AO GERADOR DE SENHAS SIMPLES!')
print(')__________________________________________(')


while x == 1:
    a = False
    b = False
    c = False
    d = False
    ef = 1
    login = str(input("Qual o login?\n"))
    quant = int(input("Digite o tamanho da senha:\n"))  # try exception
    while a == False:
        char = str(input("A senha terá caracteres? y/n:\n"))
        if char == 'Y' or char == 'y' or char == 'N' or char == 'n':
            a = True
            break
        else:
            print("Por favor, utilize Y ou N:")
            a = False
    while b == False:
        num = str(input("A senha terá números? y/n\n"))
        if num == 'Y' or num == 'y' or num == 'N' or num == 'n':
            b = True
            break
        else:
            print("Por favor, utilize Y ou N:")
            b = False
    while c == False:
        sym = str(input("A senha terá simbolos especiais? y/n\n"))
        if sym == 'Y' or sym == 'y' or sym == 'N' or sym == 'n':
            c = True
            break
        else:
            print("Por favor, utilize Y ou N:")
            c = False

    carac = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd''E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K',
             'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
             'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    espc = ['!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '-', '_', '+', '=', '"', ' ', ',', '.', ';', ':', '/',
            '?',
            '°', '|']
    password = []
    i = 0
    if (char == 'N' or char == 'n') and (num == 'N' or num == 'n') and (sym == 'N' or sym == 'n'):
        print("Não é possivel criar uma senha vazia.\n")
        ef = 0
    else:
        for i in range(0, quant):
            if (char == 'Y' or char == 'y') and (num == 'Y' or num == 'y') and (sym == 'Y' or sym == 'y'):
                password.append(random.choice(carac))
                password.append(random.choice(numbers))
                password.append(random.choice(espc))
            elif (char == 'Y' or char == 'y') and (num == 'Y' or num == 'y') and (sym == 'N' or sym == 'n'):
                password.append(random.choice(carac))
                password.append(random.choice(number))
            elif (char == 'Y' or char == 'y') and (num == 'N' or num == 'n') and (sym == 'N' or sym == 'n'):
                password.append(random.choice(carac))
            elif (char == 'N' or char == 'n') and (num == 'Y' or num == 'y') and (sym == 'Y' or sym == 'y'):
                password.append(random.choice(numbers))
                password.append(random.choice(espc))
            elif (char == 'Y' or char == 'y') and (num == 'N' or num == 'n') and (sym == 'Y' or sym == 'y'):
                password.append(random.choice(carac))
                password.append(random.choice(espc))
            elif (char == 'N' or char == 'n') and (num == 'N' or num == 'n') and (sym == 'Y' or sym == 'y'):
                password.append(random.choice(espc))
            elif (char == 'N' or char == 'n') and (num == 'Y' or num == 'y') and (sym == 'N' or sym == 'n'):
                password.append(random.choice(numbers))
    i = 0
    if ef == 1:
        print('O login foi:\n' + login)
        print('senha:', end='')
        for i in range(i, quant):
            print(password[i], end='')
    print('\n')
    '''
    f = open("passwerds.txt", "a")
    f.write(password)
    print(f.read())
    f.close()
    '''
    while d == False:
        choice = input('Você deseja criar outra senha? y/n:\n')
        if choice == 'Y' or choice == 'y' or choice == 'N' or choice == 'n':
            if choice == 'N' or choice == 'n':
                print('Muito obrigado e volte sempre! :D')
                d = True
                x = 0
            elif choice == 'Y' or choice == 'y':
                x = 1
                d = True
        else:
            print("Por favor, utilize Y ou N:")
            d = False
f.close()