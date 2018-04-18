
export function GetCookie(name) {  
    var arg = name + "=";  
    var alen = arg.length;  
    var clen = document.cookie.length;  
    var i = 0;  
    while (i < clen) {  
        var j = i + alen;  
        if (document.cookie.substring(i, j) == arg)
            var endstr = document.cookie.indexOf(";", j);  
            if (endstr == -1) endstr = document.cookie.length;  
                return unescape(document.cookie.substring(j, endstr));
        i = document.cookie.indexOf(" ", i) + 1;  
        if (i == 0) break;  
    }  
    return null;  
} 
