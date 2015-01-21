from random import randint, choice as rand_choice
import re

def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                lambda mo: mo.group(0)[0].upper() +
                            mo.group(0)[1:].lower(), s)

my_file = open('amazing_stories.txt')
word_array = []
markov_dict = {}
for line in my_file:
    line = re.sub('--', ' ', line)
    words = line.split()
    for i in range(len(words)):
        words[i] = words[i].strip('[]\'\"_*')
        if len(words[i]) > 0:
            word_array.append(words[i])


for i in range(len(word_array)-2):
    markov_dict.setdefault((word_array[i], word_array[i+1]), []).append(word_array[i+2])


quote = []

list_of_starting_words = filter(lambda x: (x[0][0] is "O") , markov_dict.items())
key = rand_choice(list_of_starting_words)[0]
# index = randint(0, len(markov_dict))
# key = markov_dict.keys()[index]
quote.append(key[0])
quote.append(key[1])


while len(quote) < 4 or (quote[-1][-1] != '.' and quote[-1][-1] != '!' and quote[-1][-1] != '?'):
# for i in range(10):
    # print quote 
    key = (quote[-2], quote[-1])
    if markov_dict.get(key):
        words = markov_dict[key]
        word = words[randint(0, len(words)-1)]
        quote.append(word)
    else:
        quote.append('...')


quote[0] = titlecase(quote[0])
for i in range(1,len(quote)):
    if quote[i-1][-1] in ['.', '!', '?', ':'] or quote[i] in ['i', 'i\'ve' 'i\'m', 'i\'d', 'dr.'] :
        quote[i] = titlecase(quote[i])
print ' '.join(quote)


