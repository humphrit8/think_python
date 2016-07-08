from random import random

def sumall(*argc):
    return sum(*argc)

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), random(), word))

    t.sort(reverse=True)

    res = []
    for length, _, word in t:
        res.append(word)
    return res

def most_frequent(word):
    for letter in word:


t = ('t',)
print (type(t))

a = 1
b = 2
c = 3


(a, b, c) = (b, c, a)

print ((a, b, c)[1])
print (a, b, c, type((a, b, c)))

p = 3, 4, 5
k = 4, 5, 6

print (type(p))

print (sumall(p))

g = dict(zip(k, p))

print (g)

d = {1:2, 3:4, 5:6, 7:8}

print (d.items())

word_group = ('bum', 'poo', 'wee', 'fart', 'shit', 'turd', 'ankle', 'willy', 'elbow')
print (sort_by_length(word_group))