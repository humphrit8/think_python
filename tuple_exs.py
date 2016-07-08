def most_frequent(words):
    freq = dict()
    for word in words:
        word = word.strip()
        for letter in word:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
    print (freq['e'])
    ordered = []
    ordered.append((2, 3))
    print (type(ordered))
    print (ordered)
    for thingy in freq:
        #print (freq[thingy])
        ordered.append((freq[thingy], thingy))
    ordered = sorted(ordered, key= lambda letter: letter[0], reverse=True)
    return ordered




word_group = ('bum ', ' poo ', 'wee ', 'fart ', ' shit ', 'turd ', 'ankle ', ' willy', ' elbow  ')
premise = most_frequent(word_group)
print (premise)