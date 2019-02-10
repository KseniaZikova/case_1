from random import randint


def check1():
    while True:
        try:
            number = int(input('Сколько вы готовы отдать?'))
        except ValueError:
            print('Неверный ввод данных.')
            continue
        else:
            break
    return number


def main():
    d = {'client': 50, 'item': 100, 'money': 1000, 'crisis': 0, 'price': 25, 'day': 1}

    def PrintData(d):
        print('\n' * 80)
        print(
            '_____________________________________________________________________________________________________________')
        print('{} {:^15} {} {:^15} {} {:^15} {} {:^15} {} {:^15} {} {:^15} {}'.format('|', 'Customers', '|', 'Products',
                                                                                      '|', 'Cashbox', '|',
                                                                                      'Crisis level',
                                                                                      '|', 'Day', '|', 'Price', '|'))
        print(
            '_____________________________________________________________________________________________________________')
        print('{} {:^15} {} {:^15} {} {:^15} {} {:^15} {} {:^15} {} {:^15} {}'.format('|', d['client'], '|', d['item'],
                                                                                      '|', d['money'], '|', d['crisis'],
                                                                                      '|',
                                                                                      d['day'], '|', d['price'], '|'))
        print(
            '_____________________________________________________________________________________________________________')

    while True:
        PrintData(d)
        answer_donation = input('Не хотите ли пожертвовать некоторую сумму в благ.фонд?(Да/Нет)').lower()
        while True:
            if answer_donation == 'нет' or answer_donation == 'да':
                break
            else:
                answer_donation = input('Неверный ввод. Да/Нет?: ').lower()

        if answer_donation == 'да':
            help1 = check1()
            d['money'] -= help1
            PrintData(d)
            if d['money'] < 15:
                print('Ты прогорел..........')
                break

        if answer_donation == 'нет':
            d['client'] -= randint(1, 10)
            PrintData(d)
            print('Эх... Продолжим')

        answer_orphan = input('Не хотите ли порадовать бесплатным мороженым детишек из детского дома?(Да/Нет)').lower()
        while True:
            if answer_orphan == 'нет' or answer_orphan == 'да':
                break
            else:
                answer_orphan = input('Неверный ввод. Да/Нет?: ').lower()

        if answer_orphan == 'нет':
            print('Жмоотяяяра.')
            d['client'] -= randint(1, 10)
            PrintData(d)
            d['crisis'] += randint(1, 10)
            PrintData(d)
            if d['crisis'] >= 100:
                print('Ты прогорел...(')
                break

        if answer_orphan == 'да':
            help2 = check1()
            d['item'] -= help2
            PrintData(d)
            d['client'] += randint(5, 15)
            PrintData(d)
            if d['item'] < d['client']:
                print('Ты прогорел(')
                break

        d['day'] += 1
main()