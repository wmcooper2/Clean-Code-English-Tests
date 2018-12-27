# Total English Assistant
## Introduction

This is a GUI tool intended to be a supplement to the "Total English" book series currently (in 2018) taught in Japan's middle schools.

Official website for the books is unknown, but here is an [example from Rakuten][0].

## Description

The primary function of this tool is to make vocabulary tests.

Secondary functions include;
* looking up words in the books' indices (dictionary tab)
* inputting sentences to check that all words exist in the book (sentence tab), and

#### Installation and Running

Install with:
```
git clone https://github.com/wmcooper2/TotalEnglishAssistant.git
cd TotalEnglishAssistant/
pipenv install
```

Run from the program's root directory with:
```
./run
```


# Instructions 
#### Vocabulary Tab

The user can choose;
* a specific grade
* a page range (start -> end; includes both start and end in the search range)
* English, Japanese or both
* how many questions per test, and 
* how many tests to make (order is random by default) 

#### Sentences Tab

* input is only accepted in English (for now).
* type any sentence that you want to use in your worksheets, and it will search for each word in the books. If it is not in the books at all, then it will display "###".
* when it searches, it does not remove apostrophes and hyphens

#### Dictionary Tab

* input only accepts English (for now)
* input a word to get that word's entry in the books' indices
* if you want to edit the word's entry, then click edit and you can change the word's entry-attributes (this edits a copy of the default dictionary)
* if you accidently make unwanted changes to the default dictionary, delete "TotalEnglishAssistant/Dictionaries/totalenglish123.json" and restart the program. It will always check that a copy exists in "TotalEnglishAssistant/Dictionaries/" 

# Developer Notes

#### Changes to Directories

This tool will :
* create these directories in the programs's root directory "TotalEnglishAssistant/";
  * "Dictionaries/"
  * "VocabularyTests/"
* write files to the newly created directories.

#### TESTING

* run "./Test" from the program's root directory.

#### Known Bugs

* dictionary tab's results are not center-aligning properly 

#### Contribute

Issue Tracker: github.com/wmcooper2/TotalEnglishAssitant/issues

#### License

Licensed under the MIT license. 


[0]: https://item.rakuten.co.jp/learners/10000360/?scid=af_pc_etc&sc2id=af_113_0_10001868
