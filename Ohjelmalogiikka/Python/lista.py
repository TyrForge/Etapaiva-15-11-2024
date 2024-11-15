lista = ['tietokone', 'näyttö', 'hiiri', 'näppäimistö', 'prosessori', 'näytönohjain', 'muisti', 'ssd', 'kiintolevy', 'usb']


print(lista)
uinput = input("Laita sana: ")
uinput = uinput.lower()

if uinput in lista:
    index = lista.index(uinput)
    print("Sana", uinput, "listassa kohdassa", index)

else:
    print("Sana", uinput, "ei ole listassa")


