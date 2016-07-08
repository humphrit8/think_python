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
    print ("Some strings were found and not added to the total: ", strings)
    return total

bunch_of_numbers=[3, 454, 123.5, 12, 75675, 1231, "donkeypunch",  6, [234, 3423, 66, [34, 56454, 1232, 5456], 0.000009], 324, [0, 5, 4554, 1.0005]]
test = [1, 1, 1, [1, 1, "wee", 1], "poo"]

print (nested_sum(bunch_of_numbers))

#for i in bunch_of_numbers:
    #print (type(i))