def main():
    uinput = int(input("Kirjoita kokonaisluku: "))
    luku = 0

    while True:
        if (uinput > luku):
            print(uinput, "on enemmän kuin", luku)
            main()
        elif (uinput < luku):
            print(uinput, "on vähemmän kuin", luku)
            main()
        elif (uinput == luku):
            print(uinput, "on yhtä paljon kuin", luku)
            main()
    


if __name__ == "__main__":
    main()