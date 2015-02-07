function formValidation()  
{  
alert('dcdcdcdc')
var uname = document.registration.fname;  
var uadd = document.registration.add1;
var ucontact = document.registration.contact;  
var ucountry = document.registration.country;  
  
var uemail = document.registration.email;  
 
{  
 
if(allLetter(uname))  
{  
if(ValidateEmail(uemail))  
{  
if(ValidateEContact(ucontact))  
{  
if(countryselect(ucountry))  
{  
if(alphanumeric(uadd))  
{  
if(allnumeric(uzip))  
{    
}   
}  
}
}   
}  
}  
  
}  
return false;  
  
} 

function allLetter(uname)  
{   
var letters = /^[A-Za-z]+$/;  
if(uname.value.match(letters))  
{  
return true;  
}  
else  
{  
alert('Username must have alphabet characters only');  
uname.focus();  
return false;  
}  
}  
function alphanumeric(uadd1)  
{   
var letters = /^[0-9a-zA-Z]+$/;  
if(uadd.value.match(letters))  
{  
return true;  
}  
else  
{  
alert('User address must have alphanumeric characters only');  
uadd.focus();  
return false;  
}  
}  
function countryselect(ucountry)  
{  
if(ucountry.value == "Default")  
{  
alert('Select your country from the list');  
ucountry.focus();  
return false;  
}  
else  
{  
return true;  
}  
}  
function allnumeric(uzip)  
{   
var numbers = /^[0-9]+$/;  
if(uzip.value.match(numbers))  
{  
return true;  
}  
else  
{  
alert('ZIP code must have numeric characters only');  
uzip.focus();  
return false;  
}  
}  
function ValidateEmail(uemail)  
{  
var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;  
if(uemail.value.match(mailformat))  
{  
return true;  
}  
else  
{  
alert("You have entered an invalid email address!");  
//email.focus();  
return false;  
}  
} 
