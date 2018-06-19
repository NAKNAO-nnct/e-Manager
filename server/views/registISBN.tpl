%rebase('main')
    <div id="page-wrapper">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">登録</h1>
            </div>
            <!-- /.col-lg-12 -->
        </div>
        <!-- /.row -->
        <div class="row">
            <div class="col-lg-12">
                <div class="panel panel-default">
                    <div class="panel-heading">
                        書籍登録
                    </div>
                    <div class="panel-body">
                        <div class="row">
                            <div class="col-lg-6">
                                <form role="form" method="post" action="{{doc_root}}/register/isbn_code">
                                    <div class="form-group">
                                        <label>ISBNコード</label>
                                        <input class="form-control" placeholder="ISBN" name="isbn" type="" autofocus required>
                                    </div>
                                    <div class="form-group">
                                        <label>配架場所</label>
                                        <input class="form-control" placeholder="配架場所" name="place" type="text" value="" required>
                                    </div>
                                    <div class="form-group">
                                        <button href="{{doc_root}}/register/isbn_code" class="btn btn-lg btn-success btn-block">登録</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
