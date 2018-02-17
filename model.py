import sqlite3
import setting as fs




# SQLクエリ実行
def access(query):
    connection = sqlite3.connect(fs.SQL)
    cursor = connection.cursor()
    result = cursor.execute(query).fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result

# SQLテーブル作成
def data_base_initialize():
    access('''CREATE TABLE task(date text NOT NULL, subject text NOT NULL, value text NOT NULL, id integer PRIMARY KEY NOT NULL, UNIQUE(date, subject, value))''')
    access('''CREATE TABLE event(date text NOT NULL, event text NOT NULL, id integer PRIMARY KEY NOT NULL, UNIQUE(date, event))''')
    access('''CREATE TABLE time_table_change(date text NOT NULL, time text NOT NULL, subject text NOT NULL, id integer PRIMARY KEY NOT NULL, UNIQUE(date, time, subject))''')

if __name__ == '__main__':
    data_base_initialize()