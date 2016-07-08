import string

def readfile(filename):
    file = open(filename)
    l = file.readlines()
    l = strip_gut_header(l)
    l = strip_gut_footer(l)
    #print (l[0:5])
    spc = string.whitespace + string.punctuation
    words = []
    print (spc)
    for item in l:
        #print (type(item))
        thing = item.split(" ")
        for word in thing:
            word = word.strip(spc)
            word = word.translate(spc)
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

def strip_gut_footer(plan):
    for i in range(len(plan)-500, len(plan)):
        if plan[i][0:28] == 'End of the Project Gutenberg':
            footer = i
            break
    return plan[:footer]

def each_word_used(book):
    word_times = dict()
    for word in book:
        if word in word_times:
            word_times[word] += 1
        else:
            word_times[word] = 1
    return word_times

def twenty_most_common(word_dict):
    values = []
    for key in word_dict:
        values.append(word_dict[key])
    values.sort(reverse = True)
    print (values[0], values[10])
    for key in word_dict:
        if word_dict[key] == 1780:
            print (word_dict[key])
    for i in range(0, 30):
        for key in word_dict:
            if word_dict[key] == values[i]:
                print (values[i], key)
                #pass

def check_word_list(word_dict):
    file = open('words.txt')
    wordlist = file.readlines()
    for word in wordlist:
        word.strip()
    strangers = []
    for key in word_dict:
        if key not in wordlist:
            strangers.append(key)
    return strangers


t = each_word_used(readfile('jacobs.txt'))
print ('No. different words:', len(t))

twenty_most_common(t)
print (check_word_list(t))

