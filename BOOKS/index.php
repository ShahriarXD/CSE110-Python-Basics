<!DOCTYPE html>
<html lang="en">
  <head><meta http-equiv="Content-Type" content="text/html; charset=gb18030">
 
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>GoogleAPI</title>

    <!-- Styles -->

    <!-- Favicons -->
<link rel="shortcut icon" href="https://images.vexels.com/media/users/3/137425/isolated/preview/f2ea1ded4d037633f687ee389a571086-logotipo-de-youtube-icono-by-vexels.png" type="image/x-icon" />

	<!-- Core Funcs -->
  	<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
  	<script src="https://ssl.p.jwpcdn.com/player/v/8.6.2/jwplayer.js"></script>
	<!-- END Core Funcs -->
	<style>
		* {
		    margin: 0px;
		}
		html {
		    overflow: hidden;
		}
	</style>	    
  </head>

<body>
	<div id="encrpyt">
		
	</div>
	<!-- Core Streaming -->
	<script>
			jwplayer.key = "cLGMn8T20tGvW+0eXPhq4NNmLB57TrscPjd1IyJF84o="; 			

			var player = jwplayer('encrpyt');

			player.setup({
			  sources: [ {
					file: "https://www.googleapis.com/drive/v3/files/<?=$_GET['id']?>?alt=media&key=AIzaSyBFHimHWDyLOtcNJjA268KwRLhsBuckUxc", label: "240p",
					type: "video/mp4"
					},{
					file: "https://www.googleapis.com/drive/v3/files/<?=$_GET['id']?>?alt=media&key=AIzaSyBFHimHWDyLOtcNJjA268KwRLhsBuckUxc", label: "360p",
					type: "video/mp4"
					},{
					file: "https://www.googleapis.com/drive/v3/files/<?=$_GET['id']?>?alt=media&key=AIzaSyBFHimHWDyLOtcNJjA268KwRLhsBuckUxc", label: "720p",
					type: "video/mp4"
					},{
					file: "https://www.googleapis.com/drive/v3/files/<?=$_GET['id']?>?alt=media&key=AIzaSyBFHimHWDyLOtcNJjA268KwRLhsBuckUxc", label: "1080p",
					type: "video/mp4"
					}
			  ],
			  autostart: false,      
			  playbackRateControls: [0.25, 0.5, 0.75, 1, 1.25, 1.5, 2],   
			  abouttext: "WG Tutoriales", 
			  	 	  aboutlink: "",         
 
			  width: $(window).width(),
		      height: $(window).height()	          
			});

			$(document).ready(function() {
				$(window).resize(function(){
					jwplayer().resize($(window).width(),$(window).height())
				})
			})

	</script>
	<!-- END Core Streaming -->
</body>
</html>