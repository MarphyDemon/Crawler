
export function GetCookie(name) {  
    var cookie = document.cookie;
    var cookieArr = cookie.split('; ');
    for(var i=0;i<cookieArr.length;i++){
        if(cookieArr[i].indexOf(name)!=-1){
            var result = cookieArr[i].split('=');
            return result[i]
        }
    }  
} 
