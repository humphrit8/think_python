def middle(array):
    return array[1:-1]

def chop(array):
    del array[0]
    del array[-1]
    return None

array  = [1, 2, 3, 4, 5, 6]

print(middle(array))
print (array)

chop(array)
print (array)

a = "banana"
b = "banana"

print (a is b)

a += "b"

print (a is b)
print (a)
x = 4

#array.append([x])
#array + [x]
#array = array.append(x)
#array = array + x
print (array)