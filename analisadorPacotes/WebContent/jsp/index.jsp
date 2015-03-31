<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta Http-Equiv="Cache-Control" Content="no-cache">
<meta Http-Equiv="Pragma" Content="no-cache">
<meta Http-Equiv="Expires" Content="0">
<title>SIOPI - Gerador de massa de testes</title>

<!-- Bootstrap -->
<link href="css/bootstrap.min.css" rel="stylesheet">
<link href="css/visual.css" rel="stylesheet">

<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
<!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->


<script type="text/javascript">
	function fileSelected() {
		var file = document.getElementById('inputFile').files[0];
		if (file) {
			var fileSize = 0;
			if (file.size > 1024 * 1024)
				fileSize = (Math.round(file.size * 100 / (1024 * 1024)) / 100)
						.toString()
						+ 'MB';
			else
				fileSize = (Math.round(file.size * 100 / 1024) / 100)
						.toString()
						+ 'KB';

			document.getElementById('info_archive').innerHTML = '<b>Detalhamento do arquivo</b><br/><br/>'
					+ '<b>Nome do arquivo:</b> '
					+ file.name
					+ '<br/>'
					+ '<b>Tamanho:</b> '
					+ fileSize
					+ '<br/>'
					+ '<b>Tipo de arquivo:</b> ' + file.type;
		}
	}

	function uploadFile() {
		var fd = new FormData();
		fd.append("inputFile", document.getElementById('inputFile').files[0]);
		var xhr = new XMLHttpRequest();
		xhr.upload.addEventListener("progress", uploadProgress, false);
		xhr.addEventListener("load", uploadComplete, false);
		xhr.addEventListener("error", uploadFailed, false);
		xhr.addEventListener("abort", uploadCanceled, false);
		xhr.open("POST", "upload", true);
		xhr.send(fd);
	}

	function uploadProgress(evt) {
		if (evt.lengthComputable) {
			var percentComplete = Math.round(evt.loaded * 100 / evt.total);
			document.getElementById('progressBar').style.width = percentComplete
					.toString()
					+ '%';
			$('#sr-only').html(percentComplete + '%');
		} else {
			document.getElementById('#sr-only').innerHTML = 'unable to compute';
		}
	}

	function uploadComplete(evt) {
		/* This event is raised when the server send back a response */
		alert(evt.target.responseText);
		//var msg=evt.target.responseText;
		//document.getElementById('corpoAviso').innerHTML = msg; 
		//$('modalAviso').on('shown.bs.modal', function (e) {

		//})
	}

	function uploadFailed(evt) {
		alert("Ocorreu um erro na tentativa de realizar upload do arquivo.");
	}

	function uploadCanceled(evt) {
		alert("O upload foi cancelado pelo usuário ou o navegador perdeu conexão com o servidor.");
	}

	function updateProgress(percentage) {
		document.getElementById('progressBar').style.width = percentage + '%';
		$('#progressText').html(percentage + '%');
	}
</script>

</head>
<body>


	<!-- Modal -->
	<div class="modal fade" id="modalAviso" tabindex="-1" role="dialog"
		aria-labelledby="myModalLabel" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">
						<span aria-hidden="true">&times;</span><span class="sr-only">Close</span>
					</button>
					<h4 class="modal-title" id="myModalLabel">Aviso</h4>
				</div>
				<div class="modal-body" id="corpoAviso"></div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" data-dismiss="modal">Fechar</button>
				</div>
			</div>
		</div>
	</div>










	<div class="bs-docs-header" id="content">
		<div class="container">
			<h1>Gerador de Massa de testes</h1>
			<h2>Operações imobiliárias</h2>
			<p>Massa de testes para reprodução de erros e falhas em produção.</p>

		</div>
	</div>


	<form role="form" enctype="multipart/form-data">
		<div id="form-group">
			<h3>Instruções:</h3>
			<p class="help-block">Informe o caminho do arquivo de origem para
				geração da massa de testes.</p>
			<p class="help-block">A massa de testes, por questões de
				segurança, são geradas no mesmo caminho C:\Desenvolvimento\, sendo
				que o nome do arquivo permanecerá o mesmo, porém, acrescentando-se o
				sufixo "MT".</p>

			<div class="panel panel-default">
				<div class="panel-body">
					<label for="inputFile">Arquivo de entrada</label> <input
						type="file" id="inputFile" name="inputFile"
						onchange="fileSelected();">

					<p class="bg-warning" id="info_archive">
					<div id="fileName"></div>
					<div id="fileSize"></div>
					<div id="fileType"></div>

					<p>
						<input type="button" class="btn btn-primary"
							onclick="uploadFile();" value="Gerar massa de testes" />
					</p>
					<div class="form-group">
						<h5>Progresso:</h5>
						<div class="progress progress-striped active"
							style="height: 30px; width: 300px;">
							<span class="sr-only"></span>
							<div id="progressBar" class="bar"
								style="height: 30px; width: 3%; background-color: green"></div>
						</div>
					</div>
				</div>
			</div>
		</div>

	</form>

	<footer class="bs-docs-footer" role="contentinfo">
		<div class="container">
			<ul class="bs-docs-footer-links muted">
				<li>Versão 3.0 - 18/11/2014</li>
			</ul>
		</div>
	</footer>

	<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
	<script
		src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	<!-- Include all compiled plugins (below), or include individual files as needed -->
	<script src="js/bootstrap.min.js"></script>
</body>
</html>