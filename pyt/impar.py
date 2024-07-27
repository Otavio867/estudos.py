

def tres_impares_consecutivos(array):
    count=0
    for num in array:
        if num%2==1:
            count+=1
        else:
            count=0
        if count>2:
            return True
    return False