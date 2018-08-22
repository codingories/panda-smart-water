$(document).ready(function(){
        $(".btn1").click(function(){
            $(this).addClass("active_write").siblings().removeClass("active_write");
            return false;
        });
	});
    // $(function(){
     //    $("#pk_section2 ul li div span").click(function(){
     //        $(this).addClass("active").siblings().removeClass("active");
     //    });
	// });
// });