%rebase('main')
<div id="page-wrapper">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">物品管理</h1>
            </div>
            <!-- /.col-lg-12 -->
        </div>
        <!-- /.row -->
        <div class="row">
            <div class="col-lg-12">
                <div class="panel panel-default">
                    <div class="panel-heading">
                        物品一覧
                    </div><!-- /.col-lg-6 -->

                    <div class="panel-body">
                        <!-- Nav tabs -->
                        <ul class="nav nav-pills">
                            <li class="active"><a href="#book" data-toggle="tab">本</a>
                            </li>
                            <li><a href="#dvd" data-toggle="tab">DVD等</a>
                            </li>
                        </ul>
                        <!-- Tab panes -->
                        <div class="tab-content">
                            <div class="tab-pane fade in active" id="book">
                                <table width="100%" class="table table-striped table-bordered table-hover" id="dataTables-book">
                                    <thead>
                                    <tr>
                                        <th>タイトル</th>
                                        <th>登録日</th>
                                        <th>配架場所</th>
                                        <th>Preview</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                        %for i in range(len(data[0])):
                                        <tr>
                                            <td>{{data[0][i][1]}}</td>
                                            <td>{{data[0][i][5]}}</td>
                                            <td>{{data[0][i][4]}}</td>
                                            <td><img class="pre_img" src="{{doc_root}}/img/{{data[0][i][2]}}" data-lity="data-lity"></td>
                                        %end
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="tab-pane fade" id="dvd">
                                <table width="100%" class="table table-striped table-bordered table-hover" id="dataTables-dvd">
                                    <thead>
                                    <!-- title, cover, addDate, jan -->
                                    <tr>
                                        <th>タイトル</th>
                                        <th>登録日</th>
                                        <th>Preview</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                        %for i in range(len(data[1])):
                                        <tr>
                                            <td>{{data[1][i][1]}}</td>
                                            <td>{{data[1][i][3]}}</td>
                                            <td><img class="pre_img" src="{{doc_root}}/img/{{data[1][i][2]}}" data-lity="data-lity"></td>
                                        %end
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>