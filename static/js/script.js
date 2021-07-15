function onSignIn(googleUser)
{
	var profile=googleUser.getBasicProfile();
	$(".g-sigin2").cc("display","none");
	$(".data").css("display","block");
	$("#pic").attr("scr",profile.getImageUrl());
	$("email").text(profile.getEmail());
}

