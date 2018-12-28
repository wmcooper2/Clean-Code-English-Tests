"""GUI Sentences Tab."""
#stand lib
import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import Menu

#custom
from sentutil import *

class SentenceTab():
    """Creates the 'Sentence' tab in the GUI, returns None."""
    original_sent   = []
    no_punct_sent   = []
    result_labels   = []
    results_rows    = []
    results_dict    = {}

    def __init__(self, tab_control):
        """Draws the widgets in the 'Sentences' tab. Returns None."""
        self.sentence_tab = ttk.Frame(tab_control)
        tab_control.add(self.sentence_tab, text = "Sentences")
        tab_control.grid()
        
        self.from_page = tk.IntVar()
        self.until_page = tk.IntVar()
        self.student_grade_level = tk.IntVar()

        input_frame = ttk.LabelFrame(self.sentence_tab, 
            text="Enter any sentence")
        input_frame.grid(column=0, row=1, padx=6, pady=6)		
        self.sentence_input = ttk.Entry(input_frame, 
            width=SENTWIDGETLEN)
        self.sentence_input.grid(column=0, row=0, columnspan=2, 
            padx=6, pady=6)
        
        check_sentence_button = ttk.Button(input_frame, text="Check", 
            command=self.results)
        check_sentence_button.grid(column=0, row=1, padx=6, pady=6)

        reset_button = ttk.Button(input_frame, text="Reset", 
            command=self.reset_choices)
        reset_button.grid(column=1, row=1, padx=6, pady=6)

        self.draw_results_frame()

    def quit_(self):
        """Quits the program. Returns None."""
        win.quit()
        win.destroy()

    def results(self):
        """Shows results of the input sentence in the GUI. Returns None."""
        self.reset_results_frame()
        self.draw_results_frame()
        self.break_up_original_sent()
        self.break_up_no_punct_sent()
        self.get_results() 
        self.draw_results_labels()
        self.draw_results_rows()

    def make_label(self, word, func=None):
        """Assembles a ttk Label widget. Returns ttk Label Widget."""
        if func != None:
            return ttk.Label(self.results_frame, text=func(word))
        else: return ttk.Label(self.results_frame, text=word)

    def get_results(self):
        """Creates a dictionary of the result labels. Returns None."""
        self.results_rows = []    #reset the results rows
        counter = 0
        #save original user-submitted word for the header, 
            #then remove the punctuation for the results widget search
        for word in self.no_punct_sent:
            temp = {}
            temp["word"] = word
            if is_valid(word): 
                temp["result"] = self.make_label(word)
                temp["grade"] = self.make_label(word, func=grade)
                temp["page"] = self.make_label(word, func=page_number)
                temp["verb"] = self.make_label(word, func=base_verb)
                temp["noun"] = self.make_label(word, func=base_noun)
                #add pos for each word
            else:
                temp["result"] = self.make_label(word)
                temp["grade"] = ttk.Label(self.results_frame, text="###")
                temp["page"] = ttk.Label(self.results_frame, text="###")
                temp["verb"] = ttk.Label(self.results_frame, text="###")
                temp["noun"] = ttk.Label(self.results_frame, text="###")
            self.results_rows.append(temp)
            counter = counter + 1

    def draw_results_rows(self):
        """Draws the result/button groups to the GUI. Returns None."""
        counter = 1
        for group in self.results_rows:
            group["result"].grid(column=counter, row=0, padx=6, pady=6)
            group["grade"].grid(column=counter, row=1, padx=6, pady=6)
            group["page"].grid(column=counter, row=2, padx=6, pady=6)
            group["verb"].grid(column=counter, row=3, padx=6, pady=6)
            group["noun"].grid(column=counter, row=4, padx=6, pady=6)
            counter = counter + 1

    def draw_results_labels(self):
        """Draws the row labels for the results widget. Returns None."""
        ttk.Label(self.results_frame, text="given word:").grid(column=0, 
            row=0, padx=6, pady=6, sticky=tk.E)
        ttk.Label(self.results_frame, text="grade:").grid(column=0, 
            row=1, padx=6, pady=6, sticky=tk.E)
        ttk.Label(self.results_frame, text="page:").grid(column=0, row=2, 
            padx=6, pady=6, sticky=tk.E)
        ttk.Label(self.results_frame, text="base verb:").grid(column=0, 
            row=3, padx=6, pady=6, sticky=tk.E)
        ttk.Label(self.results_frame, text="singular noun:").grid(column=0, 
            row=4, padx=6, pady=6, sticky=tk.E)

    def reset_results_frame(self):
        """Removes the results frame from the GUI. Returns None."""
        self.results_frame.grid_forget()

    def draw_results_frame(self):
        """Draws the results frame to the GUI. Returns None."""
        self.results_frame = ttk.LabelFrame(self.sentence_tab, 
            text="Results" )
        self.results_frame.grid(column=0, row=2, padx=6, pady=6)        

    def break_up_no_punct_sent(self):
        """Adds words without punctuation to self.user_sentence. Returns None."""
        self.no_punct_sent = []  #clear the stored values
        for word in self.sentence_input.get().split(" "):
            self.no_punct_sent.append(remove_punctuation(word))
    
    def break_up_original_sent(self):
        """Breaks up user's sentence by spaces. Returns None."""
        self.original_sent = []
        for word in self.sentence_input.get().split(" "):
            self.original_sent.append(word)
        
    def reset_choices(self):
        """Clears user's input/results from widgets. Returns None."""
        self.sentence_input.delete(0, "end")
        self.reset_results_frame()

class Sentence():
    def __init__(self, sentence):
        self.sentence = sentence
        self.words = []
        self.set_words()

    def __str__(self):
        return "A Sentence Object: {}.".format(self.sentence)

    def set_words (self):
        """Sets up the word list from the sentence. Returns None."""
        for element in self.sentence.split():
            self.words.append(element)
    
    def change_word(self, word):
        pass

    def change_all_words(self):
        """Changes words randomly. Returns None."""
        for element in self.words:
            word_index = self.words.index(element)
            word = Word(element)
            word.change_word()
            self.words[word_index] = word.english

if __name__ == '__main__':
    win             = tk.Tk()
    win.title("Test of Sentence Tab only")
    tab_control     = ttk.Notebook(win)
    menu_bar        = Menu(win)
    win.config(menu=menu_bar)
    sentence_tab    = SentenceTab(tab_control)
    file_menu       = Menu(menu_bar, tearoff = 0)
    file_menu.add_command(label="Exit", command=sentence_tab.quit_)
    menu_bar.add_cascade(label="File", menu=file_menu)
    win.mainloop()
