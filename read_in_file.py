from time import time
from remove_duplicates import remove_duplicates

def file_to_array2(file1):
    flan = open(file1)
    array = []
    for word in flan:
        #print (word)
        word = word.strip()
        array.append(word)
    print (len(array))
    return array

def bisect(array, word):
    half = int(len(array)/2+0.5)
    #print (half)
    if (word > array[half]):
        if word in array[half:-1]:
            return True
        else:
            return False
    else:
        if word in array[0:half]:
            return True
        else:
            return False

def reverse_pair(array):
    half = int(len(array)/2 + 0.5)
    pairs = []
    for word in array[0:half]:
        splitted = list(word)
        splitted.reverse()
        reversed = ''.join(splitted)
        if bisect(array, reversed) == True:
            pairs.append(word)
            pairs.append(reversed)
            #print ("pairs = ", pairs)
        else:
            pass
    final_pairs = remove_duplicates(pairs)
    return final_pairs



array74 = file_to_array2('words.txt')
pairs = reverse_pair(array74)
for i in range(0, len(pairs), 2):
    print (pairs[i+1], pairs[i])

#array1 = file_to_array2('words.txt')
#start_time2 = time()
#print (bisect(array1, "zooef"))
#end_time2 = time()
#runtime2 = end_time2 - start_time2
#print ("Runtime in: ", runtime2)