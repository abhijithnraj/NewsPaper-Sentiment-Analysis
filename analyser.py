#!/usr/bin/python3

import codecs
fn=codecs.open("negative-words.txt", "r",encoding='utf-8', errors='ignore')
n=fn.read()
n=n.split("\n")
fp=codecs.open("positive-words.txt", "r",encoding='utf-8', errors='ignore')
p=fp.read()
p=p.split("\n")

import os
os.system("wget http://indianexpress.com/latest-news")
f=open("latest-news")
text=f.read()
os.remove("latest-news")


title=[]
def cal_sentiment(words_title,words_desc,i):
    positive=0
    negative=0

    for j in words_title.split()+words_desc.split():
        if j in p:
            #print(i)
            positive+=1
        if j in n:
            #print(i)
            negative+=1
    
    if positive>negative:
        #words_title=words_title+"\n"
        fpositive.write(title_header[i])
        #fpositive.write(words_title)
        #print(words_title+"\nis Positive"+"\n"+str(positive)+"\n"+str(negative))
    elif negative > positive:
         #print(words_title+"\nis Negative"+"\n"+str(negative)+"\n"+str(positive))
        #words_title=words_title+"\n"
        #fnegative.write(words_title)
        fnegative.write(title_header[i])
    else :
        #print(words_title+"\n"+"NEUTRAL\n\n")
        #words_title=words_title+"\n"
        #fneutral.write(words_title)
        fneutral.write(title_header[i])

def get_value(list_values,delimitter1,delimitter2):
    return_list=[]
    for i in range(len(list_values)):
    #t[t.find("/india/")+len("/india/"):t.find('/">')]
        t=list_values[i].replace('&nbsp;',' ').replace('&#8217;',' ').lower()
        return_list.append(t[t.find(delimitter1)+len(delimitter1):t.find(delimitter2)])
    return return_list



txt=text.split("\n")
title_header=[]
desc_html=[]
for i in range(len(txt)):
    if '<div class="title"' in txt[i]:
        title_header.append(txt[i])
        desc_html.append(txt[i+1])

title=[]
title=get_value(title_header,'/">','</a>')
desc=[]
desc=get_value(desc_html,'<p>','</p>')

fnegative=open("negative-news.txt","w")
fpositive=open("positive-news.txt","w")
fneutral=open("neutral-news.txt","w")


for i in range(len(title)):
    cal_sentiment(title[i],desc[i],i)

fnegative.close()
fpositive.close()
fneutral.close()    

