import psycopg2
import csv

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
''')
conn.commit()

def insert_from_csv():
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("CSV данные добавлены!")

def insert_from_console():
    name = input("Имя: ")
    phone = input("Телефон: ")
    cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Пользователь добавлен!")

def update_user():
    name = input("Имя пользователя для обновления: ")
    new_phone = input("Новый телефон: ")
    cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    print("Данные обновлены!")

def search_user():
    keyword = input("Введите имя или телефон для поиска: ")
    cur.execute("SELECT * FROM PhoneBook WHERE first_name ILIKE %s OR phone ILIKE %s", (f"%{keyword}%", f"%{keyword}%"))
    results = cur.fetchall()
    for row in results:
        print(row)

def delete_user():
    target = input("Введите имя или телефон для удаления: ")
    cur.execute("DELETE FROM PhoneBook WHERE first_name = %s OR phone = %s", (target, target))
    conn.commit()
    print("Пользователь удалён!")

def main():
    while True:
        print("\nМеню:")
        print("1 - Добавить из CSV")
        print("2 - Ввести вручную")
        print("3 - Обновить данные")
        print("4 - Найти пользователя")
        print("5 - Удалить пользователя")
        print("0 - Выход")

        choice = input("Выбор: ")
        if choice == "1":
            insert_from_csv()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_user()
        elif choice == "4":
            search_user()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            break
        else:
            print("Неверный выбор!")

    cur.close()
    conn.close()

main()
