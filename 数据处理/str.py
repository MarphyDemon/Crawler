def FirstReverse(str): 
    
    # code goes here 
    aaa = []
    for i in str:
        aaa.append(i)
    aaa.reverse()
    str = ''.join(aaa)
    return str

print(FirstReverse("str ddd"))