import functions
import database

def returnWord(testWord:str) -> str:

    length , words = database.show_all_words(pr= False)

    min_dist = -1
    min_word = ''

    for word in words:
        a = functions.definchetian(testWord, word[0],pr = False)
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
        return min_word
    else:
        print('no')
        return ''
    
if __name__ == '__main__': 
    print(returnWord('tech'))