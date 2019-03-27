
function panel_signup_form(){
if ($("#login_button").is(':visible')){
$(".form").css({"padding": "10%", 
		"height": "400px",
		"animation-duration": ".5s",
		"animation-name": "anim_signup",
	});
	if (!$('#sgn').length) $('.login-form').append('<button id="sgn">Sign Up</button>' + sgn_btn);
$("#login_button").css({"display": "none"});

// BillyGLW: Move p element to an end of the .form class
$(".form").find("p").appendTo(".form").first().html("Already registred? <a style=\"cursor: pointer;\">Let's login!</a>");

$("#sgn").css({"display": "block"});

// BillyGLW: Interaction after user presses enter key.
$('#sgn').attr("type", "submit");
$('#login_button').attr("type", "button");

}else{
	$(".form").css({"padding": "10%", 
		"height": "",
		"animation-duration": ".5s",
		"animation-name": "anim_login",
	});

	
$("#login_button").css({"display": "block"});
$("#sgn").css({"display": "none"});
$(".form").find("p").appendTo(".form").first().html("Not registered? <a style=\"cursor: pointer;\">Create an account</a>");

// Interaction after user presses enter key.
$('#sgn').attr("type", "button");
$('#login_button').attr("type", "submit");
}


}
	function send_message(){
		mail_send_url = '/blog/contact/send';
		var formdata = $('#form-mailing-thread').find("select, textarea, input").serialize();
		alert(formdata);
		login = jQuery('input[name="username"]').val();
		password = jQuery('input[name="password"]').val();
	 		if (login && password){
 		}
 		else{
 			alert("Fill positions with the right data");
 			return false;
 		}
	}

	function login_handler(){
		loginurl = '/blog/login/';
		var formdata = $("#login-form").serialize();
		login = jQuery('input[name="username"]').val();
		password = jQuery('input[name="password"]').val();
	 		if (login && password){
 		}
 		else{
 			alert("Fill positions with the right data");
 			return false;
 		}
 		// Zyhu: Registration (Ajax Request)
	$.ajax({
			url: loginurl,
			type: "POST",
			data: formdata,
			success: function(data1){
					location.reload()
			}
		});
	}


	function create_user_account(){
		loginurl = 'register/';
		var formdata = $("#login-form").serialize();
		login = jQuery('input[name="username"]').val();
		password = jQuery('input[name="password"]').val();
	 		if (login && password){
 		}
 		else{
 			alert("Fill positions with the right data");
 			return false;
 		}
 		// Zyhu: Registration (Ajax Request)
	$.ajax({
			url: loginurl,
			type: "POST",
			data: formdata,
			success: function(data1){
			}
		});
	}

function user_logout(){
		var formdata = $("#login-form").serialize();
	$.ajax({
			url: '/blog/logout/',
			type: "POST",
			data: formdata,
			success: function(data){
				window.location.href = "/blog/"
			}
		});
}

function switch_to_register(){
	jQuery("#login-form").toggleClass("login-form1")
}
	
function create_account_handler(){
	alert("GOWno");
		loginurl = '/blog/account/create/';
		var formdata = $("#login-form").serialize();
		login = jQuery('input[name="username"]').val();
		password = jQuery('input[name="password"]').val();
	 		if (login && password){
 		}
 		else{
 			alert("Fill positions with the right data");
 			return false;
 		}
	$.ajax({
			url: loginurl,
			type: "POST",
			data: formdata,
			success: function(data){
				// silence is golden
			}
		});

	}

function blog_newpost(){
		var formdata = $("form").serialize();
	alert(formdata);
	$.ajax({
			url: '/blog/panel/save',
			type: "POST",
			data: formdata,
			success: function(data){
			alert(data);
			}
		});
}

// sgnup register
sgn_btn = '<script>$("#sgn").click(create_account_handler);</script>'

// events listener
$("#login_button").click(login_handler);

// signup form
$("#panel_register").click(panel_signup_form);

// signup listener (ajax request to create an account)
$("#sgn").click(create_account_handler);

// signup listener (ajax request to create an account)
$("#button_logout").click(user_logout);

// contact sendmessage
$("#button_sendmessage").click(send_message);

// save post
$("#post-new").on("click", blog_newpost);

