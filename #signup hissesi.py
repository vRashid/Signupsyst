#signup hissesi
while True:
    mail=input("Mailinizi daxil edin :")
    if "@" in mail and "." in mail:
        break
    else:
        print("duzgun mail girin")
while True:
    sifre=input("Sifrenizi daxil edin :")
    if len(sifre)>=6:
        break
    else:
        print("sifre en az 6 simvol olmalidir.")
with open("users.txt", "a") as file:
    file.write(f"{mail} {sifre}\n")
    