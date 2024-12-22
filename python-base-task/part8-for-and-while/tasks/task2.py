acocunt = 0
command = input("Введите команду: ")

while command.strip().lower() != "выйти":
    if command.strip().lower() == "пополнить счет":
        money = int(input("Сумма для пополнения: "))
        acocunt += money
        print(f'Счет пополнен на {money}. Текущий баланс: {acocunt}')

    elif command.strip().lower() == "снять деньги":
        money = int(input("Сумма для снятия: "))
        if money > acocunt:
            print(f'На вашем счету не хватает денег. Текущий баланс: {acocunt}')
        else:
            acocunt -= money
            print(f'Со счета снято {money}. Текущий баланс: {acocunt}')

    elif command.strip().lower() == "проверить баланс":
        print(f'Текущий баланс: {acocunt}')

    else:
        print("Такой команды нет. Попробуйте еще раз")

    command = input("Введите команду: ")

print("Выход из программы. Спасибо за использование нашего сервиса!")