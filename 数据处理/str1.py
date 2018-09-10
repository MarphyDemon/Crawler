def LetterChanges(str): 

    # code goes here 
    newstr = []
    for i in str:
        a = ord(i)
        if (a>=65 and a<=90) or (a>=97 and a<= 122):
            b = chr(a+1)
            if b=='a' or b =='o' or b == 'e' or b== 'i' or b=='u':
                b =b.upper()
            else:
                b =b
        else:
            b = i
        newstr.append(b)
    c = "".join(newstr)
    return c
    
# keep this function call here  
print(LetterChanges('beautiful^'))
