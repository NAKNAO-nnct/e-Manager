%rebase('main')
<div id="page-wrapper">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header"><i class="fa fa-users fa-fw"></i> UserList</h1>
            </div>
            <!-- /.col-lg-12 -->
        </div>
        <!-- /.row -->
        <div class="row">
            <div class="col-lg-12">
                <div class="panel panel-default">

                    <div class="panel-body">
                        <!-- Tab panes -->
                        <div class="tab-content">
                            <div class="tab-pane fade in active" id="book">
                                <table width="100%" class="table table-striped table-bordered table-hover" id="dataTables-book">
                                    <thead>
                                    <tr>
                                        <th>固有ID</th>
                                        <th>UserID</th>
                                        <th>名前</th>
                                        <th>権限</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                        %for i in range(len(data)):
                                        <tr>
                                            <td>{{data[i][0]}}</td>
                                            <td>{{data[i][1]}}</td>
                                            <td>{{data[i][2]}}</td>
                                            <td>{{data[i][4]}}</td>
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