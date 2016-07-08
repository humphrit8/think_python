def is_sorted(array):
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            return False
    return True

def is_anagram(word1, word2):
    array1 = list(word1)
    array2 = list(word2)
    array1.sort()
    array2.sort()
    print (array1)
    print (array2)
    if array1 == array2:
        return True
    else:
        return False

def has_duplicates(orig_array):
    array = [] + orig_array
    array.sort()
    duplicated = []
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            duplicated.append(array[i])
        else:
            pass
    if len(duplicated) > 0:
        print (duplicated)
        return True
    else:
        return False


array = [1, 2, 3, 4, 4]
array2 = [1, 3, 2, 56, 12]
array3 = [1, 2, 3, 4, 5, 4]

print(is_sorted(array))
print (is_sorted(array2))
print (is_sorted(array3))

first = "jeremy irons"
second = "jeremy irons"
print(is_anagram(first, second))

array4 = ["a", "b", "d", "d", "e", "f", "e", "f"]
print (array4)
print(has_duplicates(array4))
print (array4)