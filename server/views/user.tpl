%rebase('main')
<div id="page-wrapper">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">ユーザ設定</h1>
            </div>
            <!-- /.col-lg-12 -->
        </div>
        <!-- /.row -->
        <div class="row">
            <div class="col-lg-12">
                <div class="panel panel-default">
                    <div class="panel-heading">
                        ユーザ情報
                    </div>
                    <!-- .panel-heading -->
                    <div class="panel-body">
                        <div class="panel-group" id="accordion">
                            <div class="panel panel-default">
                                <div id="collapseOne" class="panel-collapse collapse in">
                                    <div class="container">
                                        <div class="row">
                                            <!-- <div class="col-lg-12"> -->
                                            <div class="col-lg-2">
                                                <div class="panel-body">
                                                    <h1 class="fa fa-user fw"> {{name}}</h1>
                                                </div>
                                            </div>
                                            <div class="col-lg-8">
                                                <div class="panel-body">
                                                    ID：{{UID}}<br>
                                                    Permission：{{Permission}}<br>
                                                </div>
                                            <!-- </div> -->
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- .panel-body -->
                </div>
            </div>
            <!-- /.col-lg-12 -->
        </div>
    </div>
</div>