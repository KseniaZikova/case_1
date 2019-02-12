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


def check2():
    while True:
        try:
            number = int(input("На какое количество мороженого вы закупитесь ресурсами?"))
        except ValueError:
            print('Неверный ввод данных.')
            continue
        else:
            break
    return number


def check3():
    while True:
        try:
            number = int(input("Отлично! Сколько мороженого вы готовы продать?"))
        except ValueError:
            print('Неверный ввод данных.')
            continue
        else:
            break
    return number


def main():
    d = {'client': 50, 'item': 100, 'money': 1000, 'crisis': 0, 'price': 25, 'day': 0}

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
        d['day'] += 1
        PrintData(d)

        print('Наступил', d['day'], 'день. Удачи! Цена ресурса 15 руб./шт.')
        buy = check2()
        if buy * 15 > d['money']:
            print('У тебя недостаточно денег, будет куплено: ', d['money'] // 15, 'мороженого')
            d['money'] -= 15 * (d['money'] // 15)
            PrintData(d)
            d['item'] += d['money'] // 15
            PrintData(d)
        else:
            d['money'] -= buy * 15
            PrintData(d)
            d['item'] += buy
            PrintData(d)

        dream = check3()

        sale = randint(1, 100)
        print('Сегодня клиенты пришли за', sale, 'мороженого.')
        u = input('Чувствуешь себя успешным? ')
        print('неважно. хаха')

        if dream >= sale:
            d['money'] += sale * 25
            PrintData(d)
            d['item'] -= sale
            PrintData(d)
            d['client'] += randint(5, 10)
            PrintData(d)

        else:
            d['client'] -= randint(5, 10)
            PrintData(d)
            d['crisis'] += randint(5, 10)
            PrintData(d)
            if d['crisis'] == 100:
                print('Ты проиграл. Увы, бизнес - это не твоё. Кризис достигнул отметки МАКСИМУМ.')
                break

        answer_donation = input('неважно. хаха! \n Не хотите ли пожертвовать некоторую сумму в благ.фонд?(Да/Нет)').lower()
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
        elif answer_donation == 'нет':
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
            PrintData(d)
            print('Жмоотяяяра.')
            d['client'] -= randint(1, 10)
            d['crisis'] += randint(1, 10)
            if d['crisis'] >= 100:
                print('Ты прогорел...(')
                break
            a = input('Ты еще готов посражаться? ')
            if a.lower() == 'да':
                continue
            else:
                break
        elif answer_orphan == 'да':
            help2 = check1()
            d['item'] -= help2
            d['client'] += randint(5, 15)
            PrintData(d)
            if d['item'] < d['client']:
                print('Ты прогорел(')
                break

main()