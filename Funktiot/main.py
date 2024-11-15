import os
import random

def main():
    os.system('cls')
    print("1. Kivi, Sakset, Paperi")

    uinput = int(input("Valitse Toiminto: "))
    if (uinput == 1):
        rock_paper_siccors()

def rock_paper_siccors():
    '''
    ## Basic Kivi Paperi Sakset Peli \n
    1. Käyttäjältä pyydetään valitsemaan joku neljästä valinnasta missä neljäs on "Lopeta" eli peli loppuu jos käyttäjä kirjoitaa sen
    2. Peli valitsee "random.choise" funktiolla listasta joko Kiven, Paperin tai Saksen
    3. Kun molemmat ovat vallineet peli vertaa valintoja "voitto_säännot" dictionaryyn jossa kerrotaan mikä voitaa minkä. Dictianaryn avulla voidaan myöskin helposti lisätä lisää valintoja
    4. Peli pitää kirjaa montako peliä on pelattu, kuinka monta kertaa peljaaja on voittanut ja kuinka monta kertaa tietokone on voittanut
    '''

    kps = ['Kivi', 'Sakset', 'Paperi']


    pscore = 0
    cscore = 0
    rplayed = 0

    


    voitto_säännöt = {
        "Kivi" : "Sakset",
        "Sakset" : "Paperi",
        "Paperi" : "Kivi"
    }

    while True:
        os.system('cls')
        
        print("Valitse Kivi, Sakset, Paperi tai Lopeta")
        uinput = input()
        choose = random.choice(kps)

        if (uinput == "Lopeta"):
            print("Pistemääräsi:", pscore)
            print("Koneen pistemäärä:", cscore)
            print("Kertoja Pelattu:", rplayed)
            print(" ")
            win_precentage = pscore / rplayed * 100
            print("Voitto prosentti: ", win_precentage, "%")

            quit()

        elif (uinput == choose):
            os.system('cls')
            print("Sinä Valitsit: ", uinput)
            print("Tietokone Valitsi: ", choose)
            print("Tasapeli!")
            rplayed += 1
            input("paina jotain jatkaaksesi")

        elif (voitto_säännöt[uinput] == choose):
            os.system('cls')
            print("Sinä Valitsit: ", uinput)
            print("Tietokone Valitsi: ", choose)
            print("Sinä voitit!")
            pscore += 1
            rplayed += 1
            input("paina jotain jatkaaksesi")

        else:
            os.system('cls')
            print("Sinä Valitsit: ", uinput)
            print("Tietokone Valitsi: ", choose)
            print("Sinä hävisit!")
            cscore += 1
            rplayed += 1
            input("paina jotain jatkaaksesi")


if __name__ == '__main__':
    main()
