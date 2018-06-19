% rebase('main')
<div id="page-wrapper">
    <div class="row">
        <div class="col-lg-12">
            <h1 class="page-header">ユーザ登録</h1>
        </div>
            <!-- /.col-lg-12 -->
    </div>
        <!-- /.row -->
        <div class="row">
            <div class="col-lg-12">
                <div class="panel panel-default">
                    <div class="panel-heading">
                        登録
                    </div>

                <div class="panel-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <form role="form" method="post" action="{{doc_root}}/user/add">
                                <div class="form-group">
                                    <label>名前</label>
                                    <input class="form-control" placeholder="名前" name="name" type="" autofocus required>
                                </div>
                                <div class="form-group">
                                    <label>ID</label>
                                    <input class="form-control" placeholder="ID" name="uid" type="text" value="" required>
                                </div>
                                <div class="form-group">
                                    <label>パスワード</label>
                                    <input class="form-control" placeholder="パスワード" name="passwd" type="password" value="" required>
                                </div>
                                <div class="form-group">
                                    <button href="{{doc_root}}/user/add" type="submit" class="btn btn-lg btn-success btn-block">登録</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>