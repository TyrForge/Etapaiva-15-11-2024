import os
import random

def main():
    random_num = random.randint(0,100)
    os.system("cls")
    
    while True:
        uinput = int(input("Avaa luku 0-100 väliltä: "))

        if (uinput > random_num):
            print("Numero liian suuri.")
        elif (uinput < random_num):
            print("Numero liian pieni.")
        elif (uinput == random_num):
            print("Numero oikein, Onneksi olkoon")
            input("Paina jotain jatkaaksesi")
            return
        

if __name__ == '__main__':
    main()