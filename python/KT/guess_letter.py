print("Добро Пожаловать! ")
print("Вы должны отгадать слово, отгадывая по одной букве. Если вы угадаете букву, то она появится, если нет — останется *")
print("У вас есть 10 попыток, Удачи!")

secret_word = "жопа"
attempts = 10
displayed_word = ['*'] * len(secret_word)

print(" ".join(displayed_word))  #начальное состояние слова

while attempts > 0:
    guess_letter = input("Введите букву: ").lower()

    # Проверка, что введена буква, а не цифра
    if not guess_letter.isalpha() or len(guess_letter) != 1:
        print("Введите одну букву!")
        continue

    if guess_letter in secret_word:
        print("Вы угадали букву!")

        # Открываем буквы в слове
        for i in range(len(secret_word)):
            if secret_word[i] == guess_letter:
                displayed_word[i] = guess_letter
    else:
        attempts -= 1
        print("Такой буквы нет!")
        print(f"У вас осталось {attempts} попыток.")

    print(" ".join(displayed_word))  # Выводим текущее состояние слова

    # Проверяем, угадано ли всё слово
    if '*' not in displayed_word:
        print("Поздравляем! Вы угадали слово!")
        break

if attempts == 0:
    print("Вы проиграли. Попробуйте еще раз!")
