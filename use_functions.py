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


history_transaction = []

def transaction(history_transaction, positiv_negativ_numb):
    balance = 0
    for i in range(len(history_transaction)):
        balance += history_transaction[i]
    if positiv_negativ_numb > 0:
        add_transaction = float(input('Ввведите сумму , которую вы хотите внести на ваш счёт: '))
        history_transaction.append(add_transaction)
    else:
        add_transaction = float(input('Ввведите сумму вашей покупки: '))
        if add_transaction < balance:
            add_transaction*-1
            history_transaction.append(add_transaction)
        else:
            print('Сумма покупки превышает ваш баланс')
    #print(history_transaction)
def balance_func (history_transaction):
    balance=0
    for i in range(len(history_transaction)):
        balance += history_transaction[i]
    print(f'Ваш баланс: {balance} $')
    return balance



balance = 0
print(f'Добро пожаловать в ваш электроный кошелек!\n На вашем счету: {balance} $')

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

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
        pass
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')

print(history_transaction)
