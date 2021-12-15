import random
list1=[['keep','it','cool'],['laughter','is','best'],['build','for','scalability'],['drill','your','skills'],['live','life','daily'],
       ['love','is','everything'],['never','give','up'],['never','look','back'],['remember','to','Live'],['speak','the','truth']]
sentence=random.choice(list1)
under = ['_' * len(word) for word in sentence]
#print(sentence)
print(under)
new_word=''
score=0


def enter_letter():
    global score
    while under != sentence:
        no_letter=0
        print('YOURE SCORE IS: ', score)
        i=0
        letter = input('Enter a letter: ')
        for word_index in range(len(sentence)):
            new_word = ''
            for letter_index in range(len(sentence[word_index])):
              i=i+1
              if sentence[word_index][letter_index] == letter:
                  new_word += letter
              else:
                  new_word += under[word_index][letter_index]
                  no_letter=no_letter+1
            under[word_index] = new_word
        if no_letter >0 and  no_letter == i:
            print('BAD choice. the letter', letter,'does not exist in the sentence.')
            score=score-1
        else:
            print('Good Job!')
            score=score+1
 #           plus_score(score)
        print(under)
        #enter_letter()

def plus_score(score):
    score=score+1
    print('the score is', score)
    return score



print('')
print('****  Wellcome to "Guess the word" play :)  ****')
print('')
print('you need to guess the letters in this sentence')
print('for good guess you will get 1 point, if the letter isnt in the sentence, i will take 1 point from youre score')
print(under)
print('')
enter_letter()

print()
print('GOOD JOB, YOU DID IT!!!')
print('')
print('YOURE FINAL SCORE is', score)


