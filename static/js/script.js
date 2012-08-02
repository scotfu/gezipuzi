/* Author: 


*/
	$(window).scroll(function(){
		if($(document).scrollTop() >= 100){
			$("#scrollTop").fadeIn();
		}else{
			$("#scrollTop").fadeOut();
		}
	})
	$("#scrollTop").click(function(){
		$("#scrollTop").hide();
		$('html,body').animate({scrollTop: '0px'}, 300);
		return false;			
	})		
	$("#scrollTop").hover(
		function(){
			$(".level-2").animate({opacity: '1.0'},100);
		},
		function(){
			$(".level-2").animate({opacity: '0.0'},100);
		}
	)























