from random import random

def quantuty(answer_quantuty, buy, item, money):
    # Функция "Наступил 1 день. Удачи! Цена ресурса 15 руб./шт."
    # "На какое количество мороженого вы закупитесь ресурсами?"
    if buy * 15 < money:
        print('У тебя недостаточно денег, будет куплено: ', money//15 ,'мороженого')
        money -= 15 * (money//15)
        item += money//15
    else:
        money -= buy * 15
        item += buy

# Здесь будет вопрос "Сколько мороженого вы готовы сегодня продать?" ПЕРЕМЕННАЯ dream

def sale(sale_answer, sale, item, dream, client, crisis, money):
    # Функция "Сегодня клиенты пришли за sale мороженого"
    if dream >= sale:
        money += sale * 25
        item -= sale
        client += random(5,10)
    else:
        client -= random(5,10)
        crisis += random(5,10)
        if crisis == 100:
            print('Ты проиграл. Увы, бизнес - это не твоё. Кризис достигнул отметки МАКСИМУМ.')