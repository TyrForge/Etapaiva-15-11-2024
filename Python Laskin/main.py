import os
import math

'''Basic Laskin Pythonilla.
Esimerkki:
-Käyttäjä valitsee esimerkiksi toiminnon 1 eli yhteenlaskun
-Käyttäjä sen jälkeen laittaa kaksi numeroa ja ohjelma laskee sen
'''


def choise():
    '''
    Käyttäjä valitsee mikä toiminnon he haluavat tehdä
    '''

    while True:
        os.system("cls")
        print("1. Yhteenlasku")
        print("2. Vähennyslasku")
        print("3. Kertolasku")
        print("4. Jakolasku")
        print("5. Potenssilasku")
        print("6. Neliöjuuri")
        print("7. Lopeta")

        uinput = int(input("Valitse Toiminto: "))

        if (uinput == 1):
            os.system("cls")
            num1 = int(input("Ensimmäinen Numero: "))
            num2 = int(input("Toinen Numero: "))
            yht = yhteenlasku(num1, num2)
            print(yht)
            input("paina nappia jatkaaksesi")

        elif (uinput == 2):
            os.system("cls")
            num1 = int(input("Ensimmäinen Numero: "))
            num2 = int(input("Toinen Numero: "))
            vah = vahennuslasku(num1, num2)
            print(vah)
            input("paina nappia jatkaaksesi")

        elif(uinput==3):
            os.system("cls")
            num1 = int(input("Ensimmäinen Numero: "))
            num2 = int(input("Toinen Numero: "))
            krt = kertolasku(num1, num2)
            print(krt)
            input("paina nappia jatkaaksesi")

        elif(uinput==4):
            os.system("cls")
            num1 = int(input("Ensimmäinen Numero: "))
            num2 = int(input("Toinen Numero: "))
            jak = jakolasku(num1, num2)
            print(jak)
            input("paina nappia jatkaaksesi")

        elif(uinput==5):
            os.system("cls")
            num1 = int(input("Ensimmäinen Numero: "))
            num2 = int(input("Toinen Numero: "))
            pot = potenssilasku(num1, num2)
            print(pot)
            input("paina nappia jatkaaksesi")

        elif(uinput==6):
            os.system("cls")
            num1 = int(input("Ensimmäinen Numero: "))
            sqrt = neliojuuri(num1)
            print(sqrt)
            input("paina nappia jatkaaksesi")

        elif(uinput==7):
            os.system("cls")
            quit()

def yhteenlasku(number1, number2):
    '''
     ===Yhteenlasku=== \n
     Example:
        >>> yhteenlasku(1, 2)
        3
    '''
    yhteen = number1 + number2

    return yhteen

def vahennuslasku(number1, number2):
    '''
     ===vahennuslasku=== \n
     Example:
        >>> vahennuslasku(1, 2)
        -1
    '''
    miinus = number1 - number2
    return miinus


def kertolasku(number1, number2):
    '''
     ===kertolasku=== \n
     Example:
        >>> kertolasku(2, 2)
        4
    '''
    kerto = number1 * number2
    return kerto


def jakolasku(number1, number2):
    '''
     ===jakolasku=== \n
     Example:
        >>> jakolasku(2, 2)
        1
    '''
    jako = number1 / number2
    return jako


def potenssilasku(number1, number2):
    '''
     ===potenssilasku=== \n
     Example:
        >>> potenssilasku(3, 2)
        9
    '''
    potenssi = pow(number1, number2)
    return potenssi


def neliojuuri(number1):
    '''
     ===neliojuuri=== \n
     Example:
        >>> neliojuuri(4)
        2
    '''
    sqrt = math.sqrt(number1) 
    return sqrt




if __name__ == '__main__':
        choise()
        