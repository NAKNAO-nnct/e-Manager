from bottle import *
import model, config

document_root = config.document_root
cookie_key = config.COOKIE_KEY

# top
@get('/')
def top():
    return redirect('{}/login'.format(document_root))

@get('/login')
def view_login():
    return template('login', doc_root=document_root)

@post('/login')
def login():
    uid = request.forms.uid
    passwd = request.forms.password
    if model.login_process(uid, passwd):
        token = model.issueToken()
        response.set_cookie(cookie_key, token)
        response.set_cookie('uid', uid)
    else:
        redirect('{}/login'.format(document_root))
    return redirect('{}/goods/list'.format(document_root))

# ログアウト
@get('/logout')
def logout():
    response.delete_cookie(cookie_key)
    response.delete_cookie('uid')
    return redirect('{}/login'.format(document_root))

# ユーザ関連
@get('/user/config')
def user_conf():
    token = request.get_cookie(cookie_key)
    if token is not None:
        uid = request.get_cookie('uid')
        u_info = model.getUserInfo(uid)
        name = u_info[0][2]
        permit = u_info[0][4]
        print(u_info)
        return template('user', name=name, UID=uid, Permission=permit, doc_root=document_root)
    else:
        return redirect('{}/login'.format(document_root))
# User登録
@get('/user/add')
def userAdd_views():
    token = request.get_cookie(cookie_key)
    if token is not None:
        data = model.getUserList()
        return template('user_add', doc_root=document_root)
    else:
        return redirect('{}/login'.format(document_root))

# ユーザ追加
@post('/user/add')
def user_add():
    token = request.get_cookie(cookie_key)
    if token is not None:
        uname = request.forms.name
        uid = request.forms.uid
        passwd = request.forms.passwd
        if model.user_add([uid, uname, passwd, 'admin']):
            return (''' <script>
                            alert('成功');
                            window.location.href = '{}/user/config'; 
                        </script>'''.format(document_root))
        else:
            return (''' <script>
                            alert('処理に失敗しました');
                            window.location.href = '{}/user/config'; 
                        </script>'''.format(document_root))
    else:
        return redirect('{}/login'.format(document_root))

# UserList表示
@get('/user/list')
def userList():
    token = request.get_cookie(cookie_key)
    if token is not None:
        data = model.getUserList()
        return template('users_list', data=data, doc_root=document_root)
    else:
        return redirect('{}/login'.format(document_root))

# 物品管理
# 物品リストを表示
@get('/goods/list')
def viewList():
    token = request.get_cookie(cookie_key)
    if token is not None:
        data = model.shapList()
        return template('goods_list', data=data, doc_root=document_root)
    else:
        return redirect('{}/login'.format(document_root))
        
# 物品登録
@get('/register/isbn_code')
def regist_isbn_view():
    token = request.get_cookie(cookie_key)
    if token is not None:
        return template('registISBN', doc_root=document_root)
    else:
        return redirect('{}/login'.format(document_root))

@post('/register/isbn_code')
def regist_isbn():
    token = request.get_cookie(cookie_key)
    if token is not None:
        isbn = request.forms.isbn
        place = request.forms.place
        if model.addBook(isbn, place):
            redirect('{}/goods/list'.format(document_root))
        else:
            return (''' <script>
                            alert('処理に失敗しました');
                            window.location.href = '{}/goods/list'; 
                        </script>'''.format(document_root))
    else:
        return redirect('{}/login'.format(document_root))

@get('/register/jan_code')
def regist_jan_view():
    token = request.get_cookie(cookie_key)
    if token is not None:
        return template('registJAN', doc_root=document_root)
    else:
        return redirect('{}/login'.format(document_root))

@post('/register/jan_code')
def regist_jan():
    token = request.get_cookie(cookie_key)
    if token is not None:
        jan = str(request.forms.jan)
        if model.addGoods(jan):
            redirect('{}/goods/list#dvd'.format(document_root))
        else:
            return (''' <script>
                            alert('処理に失敗しました');
                            window.location.href = '{}/goods/list'; 
                        </script>'''.format(document_root))
    else:
        return redirect('{}/login'.format(document_root))

# PATH設定
@route('/css/<filename>')
def route_css(filename):
    return static_file(filename, root='views/css/', mimetype='text/css')

@route('/js/<filename>')
def route_js(filename):
    return static_file(filename, root='views/js/', mimetype='text/javascript')

@route('/fonts/<filename>')
def route_fonts(filename):
    return static_file(filename, root='views/fonts')

@route('/images/<filename>')
def route_images(filename):
    return static_file(filename, root='views/images/')

# Preview画像
@route('/img/<filepath:re:.*\.*>')
def preview_img(filepath):
    return static_file(filepath, root='contents/photo')

# Boostrap template
@route('/vendor/<filepath:re:.*\.*>')
def route_vendor(filepath):
    return static_file(filepath, root='views/v/vendor')
@route('/dist/<filepath:re:.*\.*>')
def route_dist(filepath):
    return static_file(filepath, root='views/v/dist')
@route('/data/<filepath:re:.*\.*>')
def route_data(filepath):
    return static_file(filepath, root='views/v/data')
@route('/web/<filepath:re:.*\.*>')
def route_web(filepath):
    return static_file(filepath, root='views/v/')


run(host=config.DOC_URL[0], port=config.DOC_URL[1], debug=True, reloader=True, server='waitress')

    