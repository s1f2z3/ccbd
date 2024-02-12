import functions
import database

length , words = database.show_all_words(pr= False)

min_dist = -1
min_word = ''

for word in words:
    a = functions.definchetian('hold', word[0],pr = False)
    if a == 0:
        min_dist = a
        min_word = word[0]
        break
    if min_dist == -1:
        min_dist = a
        min_word = word[0]
    elif min_dist > a:
        min_dist = a
        min_word = word[0]

if min_dist < 3:
    print(min_dist)
    print(min_word)
else:
    print('no')