def remove_duplicates(array):
    new_array = []
    #print (len(array))
    i = len(array)
    while i > 0:
        #print (i)
        bum = array.pop(i-1)
        if bum not in new_array:
            new_array.append(bum)
        else:
            pass
        i -= 1
    return new_array

#array1 = ["a", "b", "c", "d", "e", "f", "g", "h", "g", "g", "h", "f", "a", "b"]
#array2 = remove_duplicates(array1)
#print (array2)