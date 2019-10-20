import heapq
import os
from tkinter import *

import nltk

import sys
sys.path.append("pytorch-transformers")
import wikipedia

f = open("story.txt", "w")
f.write("")
f.close()

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
        sum=str(summarize(plot))
        f = open("story.txt", "a")
        f.write(sum)
        f.close()
        sum = sum.replace('"', " ")
        sentence_list = nltk.sent_tokenize(sum)

        print(sum)  # steps is max number of training steps
        output=None
        for i in range(len(sentence_list)):
            inputed='python pytorch-transformers/examples/run_generation.py --model_type=gpt2 --length=50 --model_name_or_path=gpt2 --prompt="'+sentence_list[i]+'"'
            print(inputed)
            output=os.system(inputed)

    except wikipedia.exceptions.DisambiguationError as e:
        print("Please refine your search.")



root = Tk()
var = IntVar()

Label(root, text="Enter the Title:").pack()

text = Entry(root)
text.pack()

b1=Button(root,
          text='Write!',
          command=sel)
b1.pack()

label = Label(root)
label.pack()

b2=Button(root,
          text='Quit',
          command=root.quit)
b2.pack()

root.mainloop()