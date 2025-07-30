import sqlite3
import csv

def create_database():
    """Создание базы данных со схемой из todo_schema.sql"""
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    
    # Создание таблиц
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project (
        name        text primary key,
        description text,
        deadline    date
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS task (
        id           integer primary key autoincrement not null,
        priority     integer default 1,
        details      text,
        status       text,
        deadline     date,
        completed_on date,
        project      text not null references project(name)
    )
    """)
    
    conn.commit()
    return conn

def insert_sample_data(conn):
    """Добавление тестовых данных в обе таблицы"""
    cursor = conn.cursor()
    
    # Добавление проектов
    projects = [
        ('Редизайн сайта', 'Полный редизайн корпоративного сайта', '2023-12-31'),
        ('Запуск продукта', 'Запуск новой линейки продуктов', '2023-11-15'),
        ('Маркетинговая кампания', 'Подготовка маркетинговой кампании на 4 квартал', '2023-10-01')
    ]
    
    cursor.executemany("INSERT INTO project VALUES (?, ?, ?)", projects)
    
    # Добавление задач
    tasks = [
        (1, 'Создать wireframes', 'в ожидании', '2023-09-15', None, 'Редизайн сайта'),
        (2, 'Дизайн главной страницы', 'в работе', '2023-09-30', None, 'Редизайн сайта'),
        (1, 'Утвердить спецификации продукта', 'завершено', '2023-08-31', '2023-08-30', 'Запуск продукта'),
        (3, 'Заказать упаковочные материалы', 'в ожидании', '2023-10-01', None, 'Запуск продукта'),
        (2, 'Создать контент для соцсетей', 'в работе', '2023-09-20', None, 'Маркетинговая кампания'),
        (1, 'Определить целевую аудиторию', 'завершено', '2023-08-15', '2023-08-10', 'Маркетинговая кампания')
    ]
    
    cursor.executemany("""
    INSERT INTO task (priority, details, status, deadline, completed_on, project) 
    VALUES (?, ?, ?, ?, ?, ?)
    """, tasks)
    
    conn.commit()

def export_tasks_to_csv(conn, filename='tasks_export.csv'):
    """Экспорт задач в CSV файл"""
    cursor = conn.cursor()
    
    # Получение данных задач
    cursor.execute("""
    SELECT id, priority, details, status, deadline, completed_on, project 
    FROM task
    """)
    
    tasks = cursor.fetchall()
    
    # Заголовки столбцов на русском
    headers = [
        'ID', 'Приоритет', 'Описание', 'Статус', 
        'Срок выполнения', 'Дата завершения', 'Проект'
    ]
    
    # Запись в CSV файл
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(tasks)
    
    print(f"Данные успешно экспортированы в файл {filename}")

def main():
    # Создание и наполнение базы данных
    conn = create_database()
    insert_sample_data(conn)
    
    # Экспорт задач в CSV
    export_tasks_to_csv(conn)
    
    # Закрытие соединения
    conn.close()

if __name__ == '__main__':
    main()