#выполнил Коротаев Алексей ИЭ-71, 28.01.26
#проект "PLAY_AVTO", про покупку транспорта
kr = True#переменная овтечающая за основной цикл игры
ot = 0#переменная для хранения выбора пользователя
avto_garage_v = {}#словарь для хранения данных о транспорте
avto_money = [#список хранящий значения цен на транспорт, но сначала идет выбор региона по номеру (подробнее в блоке {elif ot == "2"})
    [8000000, 40000000, 12000000, 1600000, 9000000],#авто из Новосибирска
    [ 900000, 40000000, 10000000, 800000, 75000],#авто из Кемерово
    [ 3000000,  400000, 12000000, 12000000, 120000],#авто из Красноярска
    [ 400000, 12000000, 1000000, 9800000, 350000],#авто из Иркутска
    [ 60000000, 46000000, 210000, 5000000, 15000000]#авто из Норильска
]
money_avto = [#список хранящий значения транспорта, но сначала идет выбор региона по номеру (подробнее в блоке {elif ot == "2"})
    ["КАМАЗ-5320", "Т-72", "КрАЗ-255", "УАЗ-3303", "УРАЛ-4320"],#авто из Новосибирска
    ["УАЗ-469", "ЗИЛ-131", "УРАЛ-4420", "ГАЗ-66", "ВАЗ-2107"],#авто из Кемерово
    ["LADA - VESTA - CROSS", "УАЗ-452", "КрАЗ-255", "ВАЗ-2105", "ГАЗ-21-М"],#авто из Красноярска
    ["ЗАЗ-968", "БелАЗ-7522", "БелАЗ-7522", "ГАЗ-21", "УРАЛ-4420", '"Черная Волга"'],#авто из Иркутска
    ["БелАЗ-75710", "МИ-24","мотоцикл","электромобиль(электро-ЗАЗ)","ИС-3"]#авто из Норильска
]
l = 0#переменная которая хранит кол-во транспорта в гараже, создаем её и другие до цикла что бы не возникало ошибок в программе
h = 0#
k = 0#
j = 0#
aw = 0#
hg = 0#
qh = 0#
hf = 0#
while kr:#основной цикл игра
    l = len(avto_garage_v)
    print("что вы хотите сделать?\n"
          "1.карьера\n"
          "2.покупка\n"
          "3.гараж\n"
          "4.состояние\n"
          "5.закончить карьеру")
    ot = input("ваши действия?")
    if ot == "1":
        print(":)")
    elif ot == "2":
        print("откуда берем машину?\n"
              "1.Новосибирск\n"
              "2.Кемерово\n"
              "3.Красноярск\n"
              "4.Иркутск\n"
              "5.Норильск")
        ot = input("регион:")
        if ot == "1":
            qh = 0
            for qf in range(5):
                hg = qf + 1
                print(f"{hg}. {money_avto[qh][qf]} за {avto_money[qh][qf]} рублей")
            ot = input("покупаем?")
            if ot == "1":
                hf = 0
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "2":
                hf = 1
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "3":
                hf = 2
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "4":
                hf = 3
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "5":
                hf = 4
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            else:
                print("*нервно*:Ну... Ладно...")
        elif ot == "2":
            qh = 1
            for qf in range(5):
                hg = qf + 1
                print(f"{hg}. {money_avto[qh][qf]} за {avto_money[qh][qf]} рублей")
            ot = input("покупаем?")
            if ot == "1":
                hf = 0
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "2":
                hf = 1
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "3":
                hf = 2
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "4":
                hf = 3
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "5":
                hf = 4
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            else:
                print("*нервно*:Ну... Ладно...")
        elif ot == "3":
            qh = 2
            for qf in range(5):
                hg = qf + 1
                print(f"{hg}. {money_avto[qh][qf]} за {avto_money[qh][qf]} рублей")
            ot = input("покупаем?")
            if ot == "1":
                hf = 0
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "2":
                hf = 1
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "3":
                hf = 2
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "4":
                hf = 3
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "5":
                hf = 4
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            else:
                print("*нервно*:Ну... Ладно...")
        elif ot == "4":
            qh = 3
            for qf in range(5):
                hg = qf + 1
                print(f"{hg}. {money_avto[qh][qf]} за {avto_money[qh][qf]} рублей")
            ot = input("покупаем?")
            if ot == "1":
                hf = 0
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "2":
                hf = 1
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "3":
                hf = 2
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "4":
                hf = 3
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "5":
                hf = 4
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            else:
                print("*нервно*:Ну... Ладно...")
        elif ot == "5":
            qh = 4
            for qf in range(5):
                hg = qf + 1
                print(f"{hg}. {money_avto[qh][qf]} за {avto_money[qh][qf]} рублей")
            ot = input("покупаем?")
            if ot == "1":
                hf = 0
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "2":
                hf = 1
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "3":
                hf = 2
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "4":
                hf = 3
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            elif ot == "5":
                hf = 4
                if money_avto[qh][hf] != "продано":
                    print("ПРОДАНО!")
                    avto_garage_v[l] = money_avto[qh][hf]
                    money_avto[qh][hf] = "продано"
                else:
                    print("вы уже купили это авто...")
            else:
                print("*нервно*:Ну... Ладно...")
        else:
            print("да вам не машину, а образование себе купить... Хотя диплом у вас уже есть, хоть и из метро...")
    elif ot == "3":
        for s in range(l):
            aw = s + 1
            print(f"{aw}. {avto_garage_v.get(j)}")
            j = j + 1
    elif ot == "4":
        print(f"авто в гараже: {l}\n")
    elif ot == "5":
        print("смерть: Пора уходить...\n"
              "я: Подожди... Я был хорощшим человеком?\n"
              "смерть: Нет... Ты был лучшим...\n"
              "смерть: Встретимся в раю...\n")
        kr = False
    else:
        kr = False
        print("скорая нужна?\n"
              "1.Да\n"
              "2.Нет")
        ot = input("нужна?")
        if ot == "1":
            print("1 стадия - принятие")
        else:
            print("...")
        print("насколько все плохо?\n"
              "1.плохо\n"
              "2.все плохо\n"
              "3.очень плохо\n"
              "4.СКОРУЮ МНЕ")
        ot = input("как дела?")
        if ot == "1":
            print("...ну... удачи могу пожелать ток...")
        elif ot == "2":
            print("хотя бы честно...")
        elif ot == "3":
            print("верю... но поедешь сам, и за свои деньги!!!")
        else:
            print(":)/#|///?/0)/(-0-)")
