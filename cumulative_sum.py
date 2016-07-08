def cumulative_sum(numbers):
    cumulate = []
    #print ("length: ",len(numbers))
    for i in range(len(numbers)):
        #print (i)
        #print (numbers[0:i])
        cumulate.append(nested_sum(numbers[0:i+1]))
    return cumulate

def nested_sum(stuff):
    total = 0
    strings = ""
    for item in stuff:
        if type(item) == float or type(item) == int:
            total += item
        elif type(item) == list:
            total += nested_sum(item)
        elif type(item) == str:
            strings += item
            strings += " "
        else:
            print (type(item))
    if len(strings)>0:
        print ("Some strings were found and not added to the total: ", strings)
    return total

test = [1, 1, 1, 1, 1, 1]
#print(len(test))
bunch_of_numbers = [3, 54, 6745345, 34.45, 2342, [2342, 564542132]]
print(cumulative_sum(test))
print (cumulative_sum(bunch_of_numbers))