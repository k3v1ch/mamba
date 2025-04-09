import os
os.chdir('python/КТ2 py')
FILENAME = 'organizer.txt'

if not os.path.exists(FILENAME):
    open(FILENAME, 'w').close()

def open_file():
    print("\n текущиий файл")
    with open(FILENAME, 'r', encoding='utf-8') as file:
        lines = file.readlines