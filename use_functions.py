"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""


def transaction(history_transaction, positiv_negativ_numb):
    balance = 0
    for i in range(len(history_transaction)):
        balance += history_transaction[i]
    if positiv_negativ_numb > 0:
        add_transaction = float(input('Ввведите сумму , которую вы хотите внести на ваш счёт: '))
        history_transaction.append(add_transaction)
    else:
        add_transaction = float(input('Ввведите сумму вашей покупки: '))
        if add_transaction <= balance:
            add_transaction = add_transaction * -1  # умножаем на -1 для того что бы сумма добавлялась с минусом, это покупка
            history_transaction.append(add_transaction)
        else:
            print('Сумма покупки превышает ваш баланс')
    # print(history_transaction)


def balance_func(history_transaction):
    balance = 0
    for i in range(len(history_transaction)):
        balance += history_transaction[i]
    print(f'Ваш баланс: {balance} $')
    return balance


def history_buy(history_transaction):
    buy_list=[]
    all_summ_buy = 0
    for i in range(len(history_transaction)):
        if history_transaction[i] < 0:
            buy_list.append(history_transaction[i])
            all_summ_buy += history_transaction[i]
            print(f'Покупка: {history_transaction[i]} $')

    print(f'Общая сумма покупок: {all_summ_buy * -1} $')
    return buy_list


history_transaction = []
print('Добро пожаловать в ваш электроный кошелек!')

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. запросить баланс')
    print('5. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        transaction(history_transaction, 1)
        balance_func(history_transaction)
        pass
    elif choice == '2':
        transaction(history_transaction, -1)
        balance_func(history_transaction)
        pass
    elif choice == '3':
        history_buy(history_transaction)
        pass
    elif choice == '4':
        balance_func(history_transaction)
        pass
    elif choice == '5':
        break
    else:
        print('Неверный пункт меню')
