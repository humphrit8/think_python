import string

def readfile(filename):
    file = open(filename)
    l = file.readlines()
    l = strip_gut_header(l)
    #print (l[0:5])
    spc = string.whitespace + string.punctuation
    words = []
    print (spc)
    for item in l:
        #print (type(item))
        thing = item.split(" ")
        for word in thing:
            word = word.strip(spc)
            if len(word) > 0:
                words.append(word.lower())
    print ('Total No. words in book:', len(words))
    return words

def strip_gut_header(plan):
    for i in range (0, 50):
        if plan[i][0:8] == 'Produced':
            print (i, plan[i])
            prod = i
            break
    print (prod)
    for d in range(prod, prod+10):
        if len(plan[d]) == 1:
            start_line = d + 1
    print (plan[start_line])
    return plan[start_line:]

def each_word_used(book):
    word_times = dict()
    for word in book:
        if word in word_times:
            word_times[word] += 1
        else:
            word_times[word] = 1
    return word_times


t = each_word_used(readfile('C:\\Users\\Thomas\\Documents\\python\\pg5670.txt'))
print ('No. different words:', len(t))



