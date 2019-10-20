import heapq
from tkinter import *

import nltk

from scraper import scrapePage;
import wikipedia

def summarize(text):
    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}
    for word in nltk.word_tokenize(text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)

    sentence_list = nltk.sent_tokenize(text)

    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    return summary

def sel():
    selection = str(text.get())
    try:
        complete_content = wikipedia.page(selection)
        con=complete_content.content
        h1=con.find("== Plot ==")
        h2=con.find("==", h1+10)
        plot=con[h1+10:h2]
        print(summarize(plot))


    except wikipedia.exceptions.DisambiguationError as e:
        print("Please refine your search.")



root = Tk()
var = IntVar()

Label(root, text="Enter the Title:").pack()

text = Entry(root)
text.pack()

Label(root, text="What type of media?").pack()



R1 = Radiobutton(root, text="Book", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Movie", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Game", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)


label = Label(root)
label.pack()

b1=Button(root,
          text='Quit',
          command=root.quit)
b1.pack()

root.mainloop()