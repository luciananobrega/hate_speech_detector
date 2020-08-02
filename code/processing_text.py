from spellchecker import SpellChecker
spell = SpellChecker(language='pt') # spell checker in portuguese

# get stopwords
import nltk
import re #regex
import string

punct = string.punctuation.replace('#','').replace('@','') # remove '#' and '@' to get hashtags and mentions
stopwords = nltk.corpus.stopwords.words('portuguese') # get stop words in portuguese
laughs = "k{2,}|a*ha+h[ha]*|e*he+h[he]*|s*rs+r[rs]*" # get regex for laughs

# get file with bad words list
# Ranzi, C. (2017) “lista-palavroes-bloqueio.txt”.
#Disponível em: https://pt.scribd.com/document/345921799/lista-palavroes-bloqueio-txt.
f = open("C:\\Users\\Acer\\Documents\\Studies\\Ciência de Dados e Big Data\\13. TCC\\hate_speech_detector\\data\\lista-palavroes-bloqueio.txt", "r")
list_bad_words = f.readlines()
list_bad_words = [x.strip() for x in list_bad_words]
f.close()


def is_unknown(word):
    return spell.unknown([word]) != set()

def count_misspell(text):
    count = 0
    for word in text:
        if '#' not in word or '@' not in word or word != 'rt':
            if is_unknown(word):
                count += 1
    return count

def correct_misspell(text):
    new_text = []
    for word in text:
        if '#' not in word or '@' not in word or word != 'rt' or is_unknown(word):
            correct = spell.correction(word)
            new_text.append(correct)
    return new_text

def count_laughs(text):
    all_laughs = re.findall(laughs, text)
    all_laughs = ''.join(all_laughs)
    return len(all_laughs)

def count_bad_words(text):
    bad = []
    text = text.split(' ')
    for bad_word in list_bad_words:
        try:
            x = [re.findall('^' + bad_word.lower(), word) for word in text]
            x = [y for y in x if y != []]
            if x != []:
                bad.append(x[0][0])
        except:
            pass
    if bad != []:
        bad = set(bad) # get the unique values
    return len(bad)

def lower(text):
    return text.lower()

def remove_punctuation(text):
    new_text = []
    for char in text:
        if char in punct:
            new_text.append(' ')
        else:
            new_text.append(char)
    return ''.join(new_text)

def remove_laughs(text):
    return re.sub(laughs, '', text)

def bag_of_words(text):
    text = text.split(' ')
    text = list(filter(lambda x: x != '', text)) # remove any empty element
    return text

def remove_links(text):
    separated_text = text.split(' ')
    for word in separated_text:
        if 'http' in word or '.com' in word:
            separated_text.remove(word)
    new_text = ' '.join(separated_text)
    if new_text == '':
        return text
    else:
        return new_text

def remove_duplicated_letters(text):
    text = text.split(' ')
    new_text = []
    for word in text:
        if is_unknown(word) and word != '':
            new_word = [word[0]] # start new word with 1st letter
            for i, letter in enumerate(word[1:]):
                if letter != word[i]:
                    new_word.append(letter)
            new_word = ''.join(new_word)
        else:
            new_word = word
        new_text.append(new_word)
    text = ' '.join(new_text)
    return text
                
def remove_stopwords(text):
    text = text.split(' ')
    text_without_stopwords = [word for word in text if word not in stopwords] # remove stopwords
    # some elements of the dataset were only stopwords (eg: "quando foi isso")
    # if it's the case, we won't remove stopwords
    if text_without_stopwords != []:
        text = text_without_stopwords
    return ' '.join(text)

def stemming(text):
    stemmer = nltk.stem.RSLPStemmer() #need to download rslp
    text = stemmer.stem(text)
    return text

def process_text1(text):
    """
    Basic text processing: lower, remove links, punctuations and duplicated letters.
    """
    text = lower(text)
    text = remove_links(text)
    text = remove_punctuation(text)
    text = remove_duplicated_letters(text)

def process_text2(text):
    #print('original2: ' + text)
    text = remove_laughs(text)
    #print('remove_laughs: ' + text)
    # remove stopwords and links
    text = remove_stopwords(text)
    #print('remove_stopwords: ' + text)
    #stemming (get words variations)
    text = stemming(text)
    #print('stemming: ' + text)
    # separate into words
    text = bag_of_words(text)
    #print('bag_of_words: ' + text)
    return text

