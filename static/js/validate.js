var inputName=	$('#inputName') ;
var inputEmail=	$('#inputEmail') ;
var inputZip=	$('#inputZip') ;
var inputAdd1=	$('#inputAdd1') ;
var inputAdd2=	$('#inputAdd2') ;
var inputNumber =$('#inputNumber')
	  
  function checkFormName() { 
  	var name = inputName.val();
	  	if(name.length > 20) {
	  	  
	  	 
	  	 $('#fnameerror').text('Error: Length is greater then 20!');
	  	 return ; 
	  	} 
	  	re = /^[A-Za-z]+$/;
	  	 if(!re.test(name)) { 
	  	 	
	  	 	$('#fnameerror').text('Error: Username must contain only letters, numbers and underscores!');
	  	 	
	  	 	 return ; 
	  	 	} else {
	  	 		
	  	 		return true;
	  	 	} 
	}

function checkFormEmail() { 
  	var name = inputEmail.val();
  	re = /^[A-Za-z]+$/;  
   if(!re.test(name))  
{  
return true;  
}  
else  
{  
$('#emailerror').text('Error: Please Enter Valid Email Address!');
//name.focus();  
return false;  
}  

}

function checkFormZip() { 
  	var name = inputEmail.val();
  	re = /^[A-Za-z]+$/;  
   if(!re.test(name))  
{  
return true;  
}  
else  
{  
$('#ziperror').text('Error: Please Enter Pincode!');
//name.focus();  
return false;  
}  

}	

function checkFormAddress1() { 
  	var name = inputAdd1.val();
	  	if(name.length == 0) {
	  	  $('#zipeerror').text('Error: Please Enter YOur Adress');
	  	 
	  	 return ; 
	  	} 
	  	re = /^\w+$/;
	  	 if(!re.test(name)) { 


	  	 	
	  	 	$('#add2eerror').text('Error: Enter Vaild Address').css('background-color', 'red');
	  	 	
	  	 	 return ; 
	  	 	} else {
	  	 		
	  	 		return true;
	  	 	} 
	}	


	function checkFormAddress2() { 
  	var name = inputAdd2.val();
	  	
	  	re = /^\w+$/;
	  	 if(!re.test(name)) {
	  	  
	  	 	$('#add2error').text('Error: Enter Valid Address');
	  	 	
	  	 	 return ; 
	  	 	} else {
	  	 		
	  	 		return true;
	  	 	} 
	}

function phonenumber()  
{  var name = inputNumber.val();
  re = /^\+?([0-9]{2})\)?[-. ]?([0-9]{4})[-. ]?([0-9]{4})$/;  
  if(re.test(name))  
        {  
      return true;  
        }  
      else  
        {  
        $('#numbererror').text('Error: Use  This Format:+91-100000000');  
        return false;  
        }  
}  







$(document).on("click","#fromdate", function (e) {

var today = new Date().toISOString().split('T')[0];
(this).setAttribute('min',today)

//document.getElementsByName("somedate")[0].setAttribute('min', today);
});
	



	inputName.blur(checkFormName);
	inputEmail.blur(checkFormEmail);
	inputZip.blur(checkFormZip);
	inputAdd1.blur(checkFormAddress2);
	inputAdd2.blur(checkFormAddress2);
	inputNumber.blur(phonenumber);