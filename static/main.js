function validate(element){
	var fail = validateemail(element.email.value);
	fail += validateusername(element.username.value);
	fail += validatepassword(element.password.value);
	fail += validatefirstname(element.firstname.value);
	fail += validatelastname(element.lastname.value);
    fail += validatephoneno(element.phoneno.value);
    fail += validateregno(element.regno.value);
    fail += validatesex(element.sex.value);
    fail += validateimage(element.image.value);
	if (fail==""){
		alert("enter the missing input");
	} 
	else {alert(fail);}
}




function validatefirstname(field){
	if (field==""){ alert ("firstname missing");}
	return ""
}

function validateusername(field){
	if (field=="") { alert ("username missing");}
	return ""
}

function validatepassword(field){
	if (field==""){ alert("password misssing");}
	else if (field < 6){alert("password > 6");}
	return ""
	
}

function validatesex(field){
	if (field==""){alert("sex missing.");}
	return ""
	}

function validatelastname(field){
	if (field=="") {alert("lastname missing.");}
	return ""
}


function validateemail(field){
	if (field== "") {alert("email missing.");}
	else if (!((field.indexOf(".")>0) && (field.indexOf("@")>0))){
	alert("invalid mail address");}
	return ""
}

function validatephoneno(field){
	if (field==""){ alert("phoneno missing.");}
	else if (NaN(field)){alert("numbers only.");}
	else if (field < 11){alert("invalid no");}
	return ""
}

function validateregno(field){
	if (field==""){ alert("regno missing.");}
	else if (NaN(field)){alert("numbers only.");}
	return ""
}

function validateimage(field){
	if (field==""){ alert("image missing.");}
	return ""
}



