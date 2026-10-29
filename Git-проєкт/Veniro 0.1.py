Name = input("Create Name: ")
Password = input("Create Password: ")
print("VENIRKO-соцмережа!")
is_verifed = False
while True:
    dia = input("Скажіть Дію ")
    if dia == "Пітвердити акаунт":
        if is_verifed == True:
            print("Ви вже пітверджували акаунт")
            continue

        print("Пітвердіть свій логін і пароль ")
        cheak_Name = input("Скажіть Назву свого профілю ")
        cheak_Password = input("Скажіть назву свого пароля ")
        if cheak_Name == Name and cheak_Password == Password:
            is_verifed = True
            print("Ви пітвердили свій акаунт")

        else:
            print("Сталася помилка повторіть")

    if dia == "Зупинити програму":
        break

