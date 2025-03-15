import os
import pymysql
from urllib.request import urlopen

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    

    cmd = "update some_table set value='%s' where id='%s'" % (user_input, id)
    sql1 = """SELECT * FROM a_table WHERE value < %s"""
    sql2="insert into table values (1, 2, {0}, '', '', null)"
    cursor.execute("SELECT * FROM platforms WHERE language = '%s';" % data)
    cursor.execute(sql1 % (data,))
    cursor.execute("insert into table values (1, 2, {0}, '', '', null)".format(data))
    cursor.execute(sql2.format(data))

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
