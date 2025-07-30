import os
os.chdir('python\KT_two')
FILENAME = 'user_notes.txt'

# Убедимся, что файл существует
if not os.path.exists(FILENAME):
    open(FILENAME, 'w').close()

def show_file():
    print("\n📄 Текущий файл:")
    with open(FILENAME, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if not lines:
            print("Файл пуст.")
        else:
            for i, line in enumerate(lines, 1):
                print(f"{i}: {line.strip()}")
    print()

def add_line():
    text = input("Введите текст для добавления: ")
    with open(FILENAME, 'a', encoding='utf-8') as file:
        file.write(text + '\n')
    print("✅ Добавлено!\n")

def delete_line():
    show_file()
    try:
        num = int(input("Введите номер строки для удаления: "))
        with open(FILENAME, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if 1 <= num <= len(lines):
            del lines[num - 1]
            with open(FILENAME, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            print("🗑️ Строка удалена!\n")
        else:
            print("⚠️ Неверный номер строки!\n")
    except ValueError:
        print("⚠️ Введите целое число!\n")

def main():
    while True:
        print("Выберите действие:")
        print("1. Показать файл")
        print("2. Добавить строку")
        print("3. Удалить строку")
        print("4. Выйти")
        choice = input("Введите номер: ")
        if choice == '1':
            show_file()
        elif choice == '2':
            add_line()
        elif choice == '3':
            delete_line()
        elif choice == '4':
            print("👋 До свидания!")
            break
        else:
            print("⚠️ Неверный ввод. Попробуйте снова.\n")

if __name__ == "__main__":
    main()
