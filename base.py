from random import randint
import ru_local


def check1():
    while True:
        try:
            number = int(input(ru_local.ONEQV))
        except ValueError:
            print(ru_local.ERROR)
            continue
        else:
            break
    return number


def check2():
    while True:
        try:
            number = int(input(ru_local.TWOQV))
        except ValueError:
            print(ru_local.ERROR)
            continue
        else:
            break
    return number


def check3():
    while True:
        try:
            number = int(input(ru_local.THREEQV))
        except ValueError:
            print(ru_local.ERROR)
            continue
        else:
            break
    return number


def main():
    d = {'client': 50, 'item': 100, 'money': 1000, 'crisis': 0, 'price': 25, 'day': 0}

    def PrintData(d):
        
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

        print(ru_local.NOW, d['day'], ru_local.ONE)
        buy = check2()
        if buy * 15 > d['money']:
            print(ru_local.NOMONEY, d['money'] // 15, ru_local.ACE)
            d['money'] -= 15 * (d['money'] // 15)
            d['item'] += d['money']//15
            PrintData(d)
        else:
            d['money'] -= buy * 15
            d['item'] += buy
            PrintData(d)

        dream = check3()

        sale = randint(1, 100)
        print(ru_local.TODAYCLIENT, sale, ru_local.ACE)

        if dream >= sale:
            d['money'] += sale * 25
            d['item'] -= sale
            d['client'] += randint(5, 10)
            PrintData(d)

        else:
            d['client'] -= randint(5, 10)
            d['crisis'] += randint(5, 10)
            PrintData(d)
            if d['crisis'] == 100:
                print(ru_local.TWO)
                break
        
        u = input(ru_local.GOOD)
        print(ru_local.LOL)

        answer_donation = input(ru_local.FOREQV).lower()
        while True:
            if answer_donation == ru_local.NO or answer_donation == ru_local.YES:
                break
            else:
                answer_donation = input(ru_local.ERRORONE).lower()

        if answer_donation == ru_local.YES:
            help1 = check1()
            d['money'] -= help1
            PrintData(d)
            if d['money'] < 15:
                print(ru_local.TREE)
                break
        elif answer_donation == ru_local.NO:
            d['client'] -= randint(1, 10)
            d['crisis'] += randint(10, 40)
            PrintData(d)
            print(ru_local.FORE)

        prise = int(input(ru_local.SURPRISE))
        if prise == 1:
            lose = randint(1, d['item'] + 1)
            print(ru_local.HAHAONE, lose, ru_local.ITEM)
            d['item'] -= lose
            PrintData(d)
            if d['item'] > d['client']:
                d['crisis'] += 10
                d['client'] -= randint(5, 10)
                if d['item'] <= 0:
                    print(ru_local.ENDONE)

                elif d['crisis'] == 100:
                    print(ru_local.ENDTWO)

                elif d['item'] < d['client']:
                    print(ru_local.ENDTHREE)
        else:
            luck = randint(500, 5000)
            print(ru_local.HAHATWO, luck, ru_local.MONEY)
            d['money'] += luck
            d['crisis'] -= 10
            PrintData(d)


        answer_orphan = input(ru_local.FIVEQV).lower()
        while True:
            if answer_orphan == ru_local.NO or answer_orphan == ru_local.YES:
                break
            else:
                answer_orphan = input(ru_local.ERRORONE).lower()
        if answer_orphan == ru_local.NO:
            PrintData(d)
            print(ru_local.LOX)
            d['client'] -= randint(1, 10)
            d['crisis'] += randint(1, 10)
            if d['crisis'] >= 100:
                print(ru_local.TREE)
                break
            a = input(ru_local.WONT)
            if a.lower() == ru_local.YES:
                continue
            else:
                break
        elif answer_orphan == ru_local.YES:
            help2 = check1()
            d['item'] -= help2
            d['client'] += randint(5, 15)
            PrintData(d)
            if d['item'] < d['client']:
                print(ru_local.TREE)
                break
        s = int(input(ru_local.SURPRISETWO))
        if s == 1:
            tax = randint(20, 30)
            print(ru_local.HAHATHREE,tax, ru_local.MONEY)
            d['money'] -= tax
            d['crisis'] += randint(10, 20)
            PrintData(d)
            if d['money'] <= 0:
                print(ru_local.ENDFORE)
            elif d['crisis'] >= 100:
                print(ru_local.ENDFIVE)
        else:
            print(ru_local.HAHAFORE)
            d['client'] += randint(5, 15)
            d['money'] += randint(10, 20)
            d['crisis'] -= randint(10, 15)
            PrintData(d)

main()
