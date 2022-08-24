# Functions



from random import randint as r
from random import shuffle

def shuffle_symbols(string):
    string_list = split(string)
    shuffle(string_list)
    string = ''.join(string_list)
    return string

def select_symbols(string, n=1):
    result = ''
    if string != '':
        for i in range(n):
            index = r(0, len(string) - 1)
            result += string[index]
    return result


def select_require(*args):
    result = ''.join(e for e in args)
    return result


def divide_word(word, divide_symbol=' '):
    result = ''
    for e in word:
        result += e + divide_symbol
    return result


def change_symbol(word, s1, s2):
    result = ''
    for symbol in word:
        if symbol == s1:
            result += s2
        else:
            result += symbol
    return result


def selection_letters(word, argument='normal'):
    result = ''
    if argument == 'normal':
        result = word
    elif argument == 'great_letters':
        for e in word:
            if e.isupper():
                result += e
    elif argument == 'small_letters':
        for e in word:
            if e.islower():
                result += e
    return result


def only_type_symbols(word, argument='normal'):
    result=''
    if argument == 'normal':
        result=word
    elif argument == 'letters':
        for e in word:
            if e.isalpha():
                result += e
    elif argument == 'numbers':
        for e in word:
            if e.isdigit():
                result += e
    elif argument == 'other':
        for e in word:
            if not e.isdigit() and not e.isalpha():
                result += e
    return result


def split(word):
    result = []
    for e in word:
        result += e
    return result




def do_nothing():
    pass
