# Inclementar GUI
#Implementar criptografia
'''
version:Beta 0.3
Creator:Luiz Eduardo
16/03/2020
'''

import random

x = 1
print('____________________________________________')
print('SEJA BEM VINDO AO GERADOR DE SENHAS SIMPLES!')
print('____________________________________________')
print('\n')

while x == 1:


    a = False
    b = False
    c = False
    d = False
    e = False

    ef = 1
    tipo = str(input("Digite o tipo de login: \n"))
    login = str(input("Quais as informações de login?\n"))

    while True:
        quant = input("Digite o tamanho da senha: ")
        if quant.isnumeric():
            quant = int(quant)
            break
        else:
            print("Por favor utilize números inteiros ")

    while b == False:
        char = str(input("A senha terá caracteres? y/n: \n"))
        if char == 'Y' or char == 'y' or char == 'N' or char == 'n':
            b = True
        else:
            print("Por favor, utilize Y ou N: ")
            b = False

    while c == False:
        num = str(input("A senha terá números? y/n: \n"))
        if num == 'Y' or num == 'y' or num == 'N' or num == 'n':
            c = True
        else:
            print("Por favor, utilize Y ou N: ")
            c = False

    while d == False:
        sym = str(input("A senha terá simbolos especiais? y/n: \n"))
        if sym == 'Y' or sym == 'y' or sym == 'N' or sym == 'n':
            d = True
        else:
            print("Por favor, utilize Y ou N: ")
            d = False

    print('\n')
    carac = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd''E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K',
             'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
             'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

    numbers = ['1', '2', '3', '4',
               '5', '6', '7', '8', '9', '0']

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

    if ef ==1:

        print('O login foi:\n' + tipo + ':' + login)
        print('senha:', end='')
        for i in range(i, quant):
            print(password[i], end='')
        print('\n')

        i = 0
        fh = open("passwords.txt", "a")
        fh.write(tipo + ':' + login + '\n')
        fh.write('senha:')
        for i in range(i, quant):
            fh.write(password[i])
        fh.write('\n')
        fh.close()


    while e == False:
        choice = input('Você deseja criar outra senha? y/n: ')
        if choice == 'Y' or choice == 'y' or choice == 'N' or choice == 'n':
            if choice == 'N' or choice == 'n':
                print('Muito obrigado e volte sempre! :D')
                dog=input('Aperte qualquer tecla para continuar:\n')
                e = True
                x = 0
            elif choice == 'Y' or choice == 'y':
                x = 1
                e = True
        else:
            print("Por favor, utilize Y ou N: ")
            e = False
    print('\n')
