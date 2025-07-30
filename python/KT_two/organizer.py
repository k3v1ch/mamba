import os

FILENAME = 'organizer.txt'

if not os.path.exists(FILENAME):
    open(FILENAME, 'w').close()

def open_file():
    print("\n Текущий файл:")
    with open(FILENAME, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if not lines:
            print("Файл пуст.")
        else:
            for i, line in enumerate(lines, 1):
                if line.strip():  # Если строка не пустая
                    print(f"{i}: {line.strip()}")
    print()

def add_line():
    text1 = input("Введите название задачи ")
    print("-----------------------------------------------------")
    text2 = input("Введите описание задачи ")
    print("-----------------------------------------------------")
    text3 = input("Введите срок выполнения задачи ")
    print("-----------------------------------------------------")
    text4 = input("Напишите что то еще, если хотите(добавьте пробел,если ничего доплнительно не хотите писать)")
    print("-----------------------------------------------------")
    with open(FILENAME, 'a', encoding='utf-8') as file:
        file.write("-----------------------------------------------------")
        file.write(text1 + '\n')
        file.write(text2 + '\n')
        file.write(text3 + '\n')
        file.write(text4 + '\n')
        file.write("-----------------------------------------------------")
        file.write('\n')
    print("Добавлено!\n")

def delete_line():
    open_file()
    try:
        num = int(input("Введите номер строки для удаления: "))
        with open(FILENAME, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if 1 <= num <= len(lines):
            del lines[num - 1]
            with open(FILENAME, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            print(" Строка удалена!\n")
        else:
            print(" Неверный номер строки!\n")
    except ValueError:
        print(" Введите целое число!\n")

def edit_line():
    open_file()
    try:
        num = int(input("Введите номер строки для редактирования: "))
        with open(FILENAME, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if 1 <= num <= len(lines):
            print(f"Текущий текст: {lines[num - 1].strip()}")
            new_text = input("Введите новый текст: ")
            lines[num - 1] = new_text + '\n'
            with open(FILENAME, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            print(" Строка отредактирована!\n")
        else:
            print(" Неверный номер строки!\n")
    except ValueError:
        print(" Введите целое число!\n")

def main():
    while True:
        print("Выберите действие:")
        print("1. Показать файл")
        print("2. Добавить задачу")
        print("3. Удалить строку")
        print("4. Отредактировать строку")
        print("5. Выйти")
        choice = input("Введите номер: ")
        if choice == '1':
            open_file()
        elif choice == '2':
            add_line()
        elif choice == '3':
            delete_line()
        elif choice == '4':
            edit_line()
        elif choice == '5':
            print("👋 До свидания!")
            break
        else:
            print("⚠️ Неверный ввод. Попробуйте снова.\n")

if __name__ == "__main__":
    main()