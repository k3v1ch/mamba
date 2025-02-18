for i in range(3):
    user_value = int(input('Введите значение числа:'))

    #PEP8 python enchancing protocol 8

    print('user_value % 2 == 0',user_value % 2 == 0)

    if user_value % 2 == 0:  #True
        print(f'Ваше число {user_value} четное')
    else: #False
        print(f'Ваше число {user_value} Нечетное')