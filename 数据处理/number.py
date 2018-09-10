def SimpleAdding(num): 

    # code goes here
    if num == 1:
        mum = num + 1
    else:
        num = num + SimpleAdding(num-1)
    return num
    
# keep this function call here  
print SimpleAdding(raw_input())