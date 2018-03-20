<!DOCTYPE html>
<html lang="en">
<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>e-Manager</title>

    <!-- Bootstrap Core CSS -->
    <link href="{{doc_root}}/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- MetisMenu CSS -->
    <link href="{{doc_root}}/vendor/metisMenu/metisMenu.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="{{doc_root}}/dist/css/sb-admin-2.css" rel="stylesheet">

    <!-- Morris Charts CSS -->
    <link href="{{doc_root}}/vendor/morrisjs/morris.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="{{doc_root}}/vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">

    <!-- DataTables CSS -->
    <link href="{{doc_root}}/vendor/datatables-plugins/dataTables.bootstrap.css" rel="stylesheet">

    <!-- DataTables Responsive CSS -->
	<link href="{{doc_root}}/vendor/datatables-responsive/dataTables.responsive.css" rel="stylesheet">

    <!-- CustomCSSv2 -->
    <link href="{{doc_root}}/css/style.css" rel="stylesheet">

    <!-- Litt.js -->
    <link href="{{doc_root}}/dist/lity.css" rel="stylesheet">
    <script src="{{doc_root}}/vendor/jquery.js"></script>
    <script src="{{doc_root}}/dist/lity.js"></script>


    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>

    <div id="wrapper">

        <!-- Navigation -->
        <nav class="navbar navbar-default navbar-static-top" role="navigation" style="margin-bottom: 0">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="">e-Manager</a>
            </div>
            
            <!-- /.navbar-top-links -->

            <div class="navbar-default sidebar" role="navigation">
                <div class="sidebar-nav navbar-collapse">
                    <ul class="nav" id="side-menu">
                        <li>
                            <a href="{{doc_root}}/user"><i class="fa fa-user fa-fw"></i> Dashboard<span class="fa arrow"></span></a>
                            <ul class="nav nav-second-level">
                                <li>
                                    <a href="{{doc_root}}/user/config">User</a>
                                </li>
                                <li>
                                    <a href="{{doc_root}}/user/list">List</a>
                                </li>
                                <li>
                                    <a href="{{doc_root}}/user/add">User登録</a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <a href="{{doc_root}}/manager/"><i class="fa fa-table fa-fw"></i> 物品管理<span class="fa arrow"></span></a>
                            <ul class="nav nav-second-level">
                                <li>
                                    <a href="{{doc_root}}/goods/list">一覧 </a>
                                </li>
                                <li>
                                    <a href="{{doc_root}}/register/">登録 <span class="fa arrow"></span></a>
                                    <ul class="nav nav-third-level">
                                        <li>
                                            <a href="{{doc_root}}/register/isbn_code">ISBNコード</a>
										</li>
										<li>
                                            <a href="{{doc_root}}/register/jan_code">JANコード</a>
										</li>
                                    </ul>
                                    <!-- /.nav-third-level -->
                                </li>
                            </ul>
                        </li>
                        
                        <li>
                            <li>
                                <a href="{{doc_root}}/logout"><i class="fa fa-sign-out fa-fw"></i>Logout</a>
                            </li>
                            <!-- /.nav-second-level -->
                        </li>
                    </ul>
                </div>
                <!-- /.sidebar-collapse -->
            </div>
            <!-- /.navbar-static-side -->
		</nav>
		{{!base}}

    <!-- jQuery -->
    <script src="{{doc_root}}/vendor/jquery/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="{{doc_root}}/vendor/bootstrap/js/bootstrap.min.js"></script>

    <!-- Metis Menu Plugin JavaScript -->
    <script src="{{doc_root}}/vendor/metisMenu/metisMenu.min.js"></script>

    <!-- Morris Charts JavaScript -->
    <script src="{{doc_root}}/vendor/raphael/raphael.min.js"></script>
    <script src="{{doc_root}}/vendor/morrisjs/morris.min.js"></script>
    <script src="{{doc_root}}/data/morris-data.js"></script>

    <!-- Custom Theme JavaScript -->
    <script src="{{doc_root}}/dist/js/sb-admin-2.js"></script>

    <!-- DataTables JavaScript -->
    <script src="{{doc_root}}/vendor/datatables/js/jquery.dataTables.min.js"></script>
    <script src="{{doc_root}}/vendor/datatables-plugins/dataTables.bootstrap.min.js"></script>
	<script src="{{doc_root}}/vendor/datatables-responsive/dataTables.responsive.js"></script>
	
	<!-- Table -->
    <script>
        $(document).ready(function() {
            $('#dataTables-book').DataTable({
                responsive: true
            });
        });
    </script>
    <script>
        $(document).ready(function() {
            $('#dataTables-dvd').DataTable({
                responsive: true
            });
        });
    </script>

</body>

</html>
