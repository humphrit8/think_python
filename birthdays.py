from random import randint

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
        #print (duplicated)
        return True
    else:
        return False

def random_birthday():
    month = randint(1, 12)
    #print (month)
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    if month in thirty_one:
        day = randint(1, 31)
    elif month == 2:
        day = randint(1, 29)
    else:
        day = randint(1, 30)
    date = str(month)+"-"+str(day)
    return date


def generate_some_birthdays(n):
    array  = []
    for i in range(n):
        birthday = random_birthday()
        array.append(birthday)
    #print (array)
    return array

total = 0
iterations = 3000
for i in range(iterations):
    birthdays = generate_some_birthdays(23)
    if has_duplicates(birthdays) == True:
        total += 1
    else:
        pass

print ("total = ", total)
print ("percentage = ", total/iterations*100)

#print (birthdays)
#print (len(birthdays))
