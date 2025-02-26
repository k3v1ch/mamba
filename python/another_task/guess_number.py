import random

print("Отгадай число, будет сгенирировано число от 1 - 100.")
print("У тебя 10 попыток, Удачи!")

random_number = random.randint(1,100)
attempts = 10


while attempts > 0:
    guess_number = input("Введите число (1-100): ")
    if not guess_number.isdigit():
        print("Ошибка! Введите именно число.")
        continue  # Пропускаем итерацию, если введено не число

    guess_number = int(guess_number)

    if guess_number > random_number:
        attempts -= 1
        print("----------------------")
        print(" ")
        print("Число меньше!")
        print(f"У тебя осталось: {attempts} попытки!")
        print(" ")
        print("----------------------")

    if guess_number < random_number:
        attempts -= 1
        print("----------------------")
        print(" ")
        print("Число больше!")
        print(f"У тебя осталось: {attempts} попытки!")
        print(" ")
        print("----------------------")

    if guess_number == random_number:
        print(" ")
        print("Ты победил")
        break
    
    if attempts == 0:
        print("Ты проиграл, попробуй еще раз!")
        print(f"Загадоное число было:{random_number}")