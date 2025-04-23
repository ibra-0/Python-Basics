import psycopg2
import json
import csv

conn = psycopg2.connect(
    dbname="phonebook_db", 
    user="postgres", 
    password="postgres", 
    host="localhost", 
    port="5432"
)
cur = conn.cursor()

def upload_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  
        users = []
        for row in reader:
            users.append({"username": row[0], "phone": row[1]})
        cur.execute("CALL insert_many_users(%s)", (json.dumps(users),))
    conn.commit()
    print("Data uploaded from CSV.")

def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone number: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (username, phone))
    conn.commit()
    print("Data inserted from console.")

def update_user():
    username = input("Enter existing username: ")
    new_phone = input("Enter new phone number: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (username, new_phone))
    conn.commit()
    print("User phone updated.")

def search_users():
    pattern = input("Enter search pattern: ")
    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def insert_multiple_users_from_console():
    users_input = input("Enter users (name,phone) separated by comma, e.g. 'John,1234567890,Alice,9876543210': ")
    users_list = users_input.split(',')
    
    users_array = [f"{users_list[i]},{users_list[i+1]}" for i in range(0, len(users_list), 2)]
    
    cur.execute("CALL insert_multiple_users(%s)", (users_array,))
    conn.commit()
    print("Users inserted or updated.")


def get_users_page():
    limit_val = int(input("Enter limit: "))
    offset_val = int(input("Enter offset: "))
    cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit_val, offset_val))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_user():
    value = input("Enter username or phone to delete: ")
    cur.execute("CALL delete_user(%s)", (value,))
    conn.commit()
    print("User deleted.")

def main():
    while True:
        print("\n1. Upload from CSV")
        print("2. Insert from console")
        print("3. Update user phone")
        print("4. Search users")
        print("5. Get users page")
        print("6. Delete user")
        print("7. Insert multiple users")
        print("8. Exit")
        choice = input("Choose an action: ")

        if choice == '1':
            upload_from_csv('phonebook.csv')
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_user()
        elif choice == '4':
            search_users()
        elif choice == '5':
            get_users_page()
        elif choice == '6':
            delete_user()
        elif choice == '8':
            break
        elif choice == '7':
            insert_multiple_users_from_console()  
        else:
            print("Invalid choice. Please select again.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
