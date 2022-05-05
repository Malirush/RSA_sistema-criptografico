
from random import randint


tabela = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
          'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
          'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
          'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
          'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

qtdC = 2
qtdP = 2


def primo():
    procura = True
    global primos
    primos = []
    while procura:
        ePrimo = 0
        numeros = []
        number = randint(1, 100)
        for i in range(1, 100):
            if number % i == 0:
                ePrimo += 1
        if len(str(number)) < qtdC:
            continue
        if ePrimo == 2:
            primos.append(number)
        else:
            continue
        if len(primos) == qtdP:

            return defkeys(primos)


def defkeys(pri):
    Cpu = pri[0]*pri[1]  # N 391 no video
    func = (pri[0]-1)*(pri[1]-1)  # 352 no video
    testfunc = func
    b = randint(0, 100)
    save = b    # 3 no video
    while b != 0:
        resto = testfunc % b
        testfunc = b
        b = resto
        if b == 0 and testfunc > 1:
            b = randint(0, 100)
            save = b
            testfunc = func
            continue

    return lastkey(func, Cpu, save)


def lastkey(f, c, s):
    save = s
    cpu = c
    global Lkey
    Lkey = None
    for i in range(10000):
        if (i*s) % f == 1:
            Lkey = i
            break
    return encrip(save, cpu)


def encrip(s, cpu):
    codig = []
    for letra in msg:
        if letra == ' ':
            codig.append('')
            continue
        x = ((tabela[letra])**s) % cpu
        codig.append(x)
    if rspt == '1':
        return print(f'mensagem encriptada:{codig}')
    else:
        return descript(codig, cpu)


def descript(cod, cpu):
    codig = []
    frase = []
    for i in cod:
        if i == '':
            codig.append('')
            continue
        x = i**Lkey % cpu
        codig.append(x)
    for j in codig:
        if j == '':
            frase.append(' ')
        for key, values in tabela.items():
            if j == values:
                frase.append(key)
    frase = ''.join(frase)
    return print(frase)


def init():
    ini = True
    print('______RSA ENCRIP______')
    while ini:
        print('__digite sua mensagem__')
        print('__OBS:letras maiusculas__')
        global msg
        msg = input()
        print('Voce deseja encriptar?')
        global rspt
        rspt = input('digite "1" para sim "2" para nao \n')
        if rspt == '1':
            primo()
        print('para desencriptar digite "2"')
        print('para reiniciar digite 3')
        print('para sair digite outra coisa')
        rspt = input()
        if rspt == '2':
            primo()
            print('deseja mudar a frase? se sim digite "3"')
            print('se nao digite qualquer coisa')
            rspt = input()
        if rspt == '3':
            continue
        else:
            break


init()
