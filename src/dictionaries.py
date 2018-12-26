#!/usr/bin/python3

#stand lib
import sys
import json
from pathlib import Path
import random

#custom
from words import *

def japanese(word):
    """Gets the Japanese definition. Returns String."""
    if is_valid(word):
        return dict_value(word, "japanese")

def page_number(word):
    """Gets page number of word. Returns String."""
    if is_valid(word):
        return dict_value(word, "page")

def within_page_range(word, start, end):
    """Checks if a word exists within a page range. Returns Boolean."""
    if int(page_number(word))>=int(start) and \
       int(page_number(word))<=int(end):
        return True
    else: return False

def dict_value(word, value):
    """Gets word's value from dictionary. Returns String."""
    return DICT[word][value]

def grade(word):
    """Gets grade level of word. Returns String."""
    if is_valid(word):
        return dict_value(word, "grade")

def get_pos(word):
    """Gets part of speech for word. Returns String."""
    if is_valid(word):
        return dict_value(word, "part of speech")

def same_grade(grade, word):
    """Checks that a word is in grade level. Returns Boolean."""
    if int(grade) == int(DICT[word]["grade"]): return True
    else: return False

def grade_filter(grade, some_list):
    """Filters some_list based on grade level. Returns List."""
    return list(filter(lambda word: same_grade(grade, word), some_list))

def page_filter(lo, hi, some_list):
    """Filters some_list by page range. Returns List."""
    return list(filter(lambda word: within_pages(word, lo, hi), some_list))

def gt_eq_page(word, page_num):
    """Checks if word is on or after page_num. Returns Boolean."""
    return int(page_number(word)) >= int(page_num)

def lt_eq_page(word, page_num):
    """Checks if word is on or before page_num. Returns Boolean."""
    return int(page_number(word)) <= int(page_num)

#copied from words.py
def within_pages(word, lo, hi):
    """Checks if a word exists within a page range. Returns Boolean."""
    if gt_eq_page(word, lo) and lt_eq_page(word, hi): return True
    else: return False

def punct_filter(some_list):
    """Filters some_list by words that have an apostrophe. Returns List."""
    return list(filter(lambda word: "'" in word, some_list.keys()))

def same_grade(grade_level, word):
    """Checks if the word is in grade. Returns Boolean."""
    return grade_level == int(grade(word))

def within_grade_range(word, start, end):
    """Gets word list within grade range. Returns Boolean."""
    if int(grade(word))>=int(start) and int(grade(word))<=int(end):
        return True
    else: return False

def get_japanese_words():
    """Gets Japanese words. Returns List."""
    temp = []
    [temp.append(v["japanese"]) for k, v in DICT.items()]
    return temp

def get_english_words():
    """Gets English words. Returns List."""
    temp = []
    [temp.append(k) for k in DICT.keys()]
    return temp

def get_words_in_language(language):
    """Gets words of language. Returns List."""
    if language == "english": return get_english_words()
    elif language == "japanese": return get_japanese_words()
    else: return get_english_words() + get_japanese_words()
    









def save_dictionary(save_this, file_path):
    """Saves dictionary to file_path. Returns None."""
    dump_here = open(file_path, "w+")
    json.dump(save_this, dump_here)
    dump_here.close()

def edit_entry(key, entry):
    """Edits an entry in the dictionary. Returns None."""
    dictionary[key] = entry
    save_dictionary(dictionary, default_dict_path)

def get_entry(word):
    """Sets a single entry. Returns None."""
    if in_dictionary(word):
        return DICT[word]
    else:
    #replace with dictionary.get(word, "not found")?
        try:
            return dictionary[word]
        except KeyError:
            return DEFAULTENTRY
