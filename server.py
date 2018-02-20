from bottle import *
from model import *

# top
@get('/')
def top():
    return 'Hello'

# 物品管理
# SQLから引っ張ってきたデータを表示
@get('/<gid>/goods/manage')
def goodsManagement(gid):
    return gid

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
