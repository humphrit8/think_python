def more_than_20(list):
    for line in list:
        word = line.strip()
        if len(word) >= 20:
            print word

def has_no_e(word):
    for char in word:
        if char == "e":
            return False
    return word

def words_witout_x(list, letter):
    counter = 0
    total = 0
    for line in list:
        total += 1.0
        word = line.strip()
        if avoids(word, letter) != False:
            print avoids(word, letter)
            counter += 1.0
    return counter/total * 100.0

def avoids(word, letter):
    for char in word:
        if char == letter:
            return False
    return word

def uses_only(list, letters):
    #print ("letters")
    for line in list:
        word = line.strip()
        check_word_letters(word, letters)

def check_word_letters(word, letters):
    for char in word:
        #print (char)
        #print (letters)
        if letters.find(char) < 0:
            return False
    print (word)
    return word

def uses_all(word, letters):
    for char in letters:
        if word.find(char) < 0:
            return False
    print word
    return word

def use_all_pass(list, letters):
    for line in list:
        word = line.strip()
        uses_all(word, letters)

def alphabet_pass(list):
    counter = 0
    for line in list:
        word = line.strip()
        if is_alphabetarian(word) != False:
            counter += 1
    return counter

def is_alphabetarian(word):
    index = 1
    while index < len(word):
        if word[index]< word[index-1]:
            return False
        index += 1
    print word
    return word

def three_doubles(word):
    index = 0
    while index < (len(word) - 6):
        if word[index] == word[index +1] and word[index+2]==word[index+3] and word[index+4]== word[index+5]:
            print word
            return word
        index += 1
    return False

def pass_to_three_doubles(list):
    for line in list:
        word = line.strip()
        if len(word) >= 6:
            three_doubles(word)


flan = open('words.txt')
#print (words_witout_e(flan))
letters = "aeiouy"
pass_to_three_doubles(flan)
