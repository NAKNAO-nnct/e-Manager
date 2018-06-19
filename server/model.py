import sqlite3, json, xmltodict, re, random, uuid
import config as fs
import getBookData as gBook
import getAmazonData as aData
import bottlenose as api
from bs4 import BeautifulSoup
from datetime import *

# 日付
def getDate():
    now = datetime.now()    # 日付取得
    year = now.year     # 年
    month = now.month   # 月
    day = now.day       # 日
    result = shapingDate([year, month, day])
    return result

# 整形
def shapingDate(date):
    date_jp = '{}/{}/{}'.format(date[0], date[1], date[2])
    return date_jp


# ViewsTable用
def shapList():
    book_list = getBookList()
    goods_list = getGoodskList()
    List = [book_list, goods_list]
    return List

# User
def getUserInfo(uid):
    user_info = access('''SELECT * from Member where uid = "{}";'''.format(uid), fs.SQL)
    return user_info

# UserList
def getUserList():
    return access('''SELECT * from Member;''', fs.SQL)

# 物品一覧取得
# 本リスト
def getBookList():
    return access('''SELECT * from BOOK;''', fs.BOOK_SQL)
    
# その他リスト
def getGoodskList():
    return access('''SELECT * from AGoods;''', fs.BOOK_SQL)

# 物品登録処理
# JANコードによる登録
def addGoods(jan):
    response = aData.getItem(jan)
    if isJan(response[2]):
        access('''INSERT into AGoods(title, cover, addDate, jan) values("{}", "{}", "{}",{});'''.format(response[0], response[1], getDate(), response[2]), fs.BOOK_SQL)
        return True
    else:
        return False

# すでに登録されているか
def isJan(jan):
    if access('''SELECT * from AGoods where jan = {};'''.format(jan), fs.BOOK_SQL) == []:
        return True
    else:
        return False

# 書籍登録処理
def addBook(isbn, place):
    response = gBook.getBookData(isbn)  # ISBN, title, 著者, 配架場所, 登録日, CoverPhoto
    print(response)
    if isIsbn(response[0]):
        access('''INSERT into BOOK(isbn, title, pubdate, place, addDate, cover) values({}, "{}", "{}", "{}", "{}","{}");'''.format(response[0], response[1], response[4], place ,getDate(),response[5]), fs.BOOK_SQL)
        return True
    else:
        return False

# 本がすでに登録されているか確認
def isIsbn(isbn):
    if access('''SELECT * from BOOK where isbn = {};'''.format(isbn), fs.BOOK_SQL) == []:
        return True
    else:
        return False

# 物品削除
def removeIsbn():
    pass  
def remobeJan():
    pass

# ユーザー関連処理
# ユーザの登録
def user_add(add_data):
    if isUid(add_data[0]):
        access('''INSERT into Member(uid, uname, passwd, permission) values("{}", "{}", "{}", "{}");'''.format(add_data[0], add_data[1], add_data[2], add_data[3]), fs.SQL)
        return True
    else:
        return False

# UIDに被りがないか確認
# なければTrueを返却
def isUid(uid):
    if access('''SELECT * from Member where uid = "{}";'''.format(uid), fs.SQL) == []:
        return True
    else:
        return False

# login処理
# 認証
def login_process(uid, passwd):
    print([uid, passwd])
    if access('''SELECT id from Member where uid = "{}";'''.format(uid), fs.SQL) == []:
        return False
    else:
        _pass = access('''SELECT passwd from Member where uid = "{}";'''.format(uid), fs.SQL)
        if passwd == _pass[0][0]:
            return True
        else:
            return False

#token発行
def issueToken():
    uniqueId = uuid.uuid4()
    return str(uniqueId)

# SQLクエリ実行
def access(query, sql):
    connection = sqlite3.connect(sql)
    cursor = connection.cursor()
    try:
        result = cursor.execute(query).fetchall()
    except sqlite3.IntegrityError:
        cursor.close()
        connection.close()
        raise sqlite3.IntegrityError
    connection.commit()
    cursor.close()
    connection.close()
    return result

# 初期
# SQLテーブル作成
def data_base_initialize():
    access('''CREATE TABLE Member(
	    id	INTEGER PRIMARY KEY,
	    uid	TEXT NOT NULL,
	    uname	TEXT NOT NULL,
	    passwd	TEXT NOT NULL,
        permission  TEXT NOT NULL);''', fs.SQL)
     
    access('''CREATE TABLE BOOK (
	    id	INTEGER PRIMARY KEY,
	    title	TEXT NOT NULL,
	    cover	TEXT NOT NULL,
        pubdate	TEXT NOT NULL,
        place TEXT NOT NULL,
        addDate TEXT NOT NULL,
	    isbn	INTEGER NOT NULL);''', fs.BOOK_SQL)

    access('''CREATE TABLE AGoods (
	    id	INTEGER PRIMARY KEY,
	    title	TEXT NOT NULL,
	    cover	TEXT NOT NULL,
        addDate TEXT NOT NULL,
	    jan	INTEGER NOT NULL);''', fs.BOOK_SQL)


if __name__ == '__main__':
    # data_base_initialize()  # TABLE作成
    
    # if user_add(fs.ADMIN):   # 初期ユーザ作成
    #     print('Success')
    # else:
    #     print('失敗')
    print(addBook('9784774193977', '長男部屋'))
    # print(addGoods('4988013068711'))
    info = getUserInfo('admin')
    # print(info[0])
    print(getUserList())
    # print(getBookList())
    # print(getGoodskList())
    # print(login_process('admin', 'admin'))
    # print(shapList())
    # shapList()
    # if user_add(['trompot', '捕鯨太郎', 'password', 'admin']):
    #     print('Success')
    # else:
    #     print('Fuck you!')

