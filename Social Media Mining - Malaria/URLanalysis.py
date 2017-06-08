
# coding: utf-8

# In[1]:

import re
from urlparse import urlparse


# In[2]:

results = []
with open('C:\Users\Michael Neuman\Desktop\csv_week1\combined.txt') as inputfile:
    count = 0
    for line in inputfile:
        if (count % 3 == 0):
            results.append(line.strip('text:'))
        count = count + 1;

results
# In[3]:

urls = []


# In[4]:

for line in results:
    if ('http' in line):
        urls.append(line)


# In[5]:

urls


# In[6]:

specific_urls = []


# In[7]:

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1


# In[8]:

for line in urls:
    url_string = ""
    index_start = find_str(line,'http')
    cur_index = index_start
    cur_char = line[index_start]
    while(cur_char != '"'):
        if(cur_char == ' '):
            break
        if (cur_char != "\\"):
            url_string = url_string + cur_char
        cur_index = cur_index + 1
        cur_char = line[cur_index]
    specific_urls.append(url_string)


# In[9]:

specific_urls


# In[10]:

from collections import defaultdict


# In[11]:

freqs = defaultdict(int)


# In[12]:

for line in specific_urls:
    freqs[line] += 1


# In[13]:

freqs


# In[14]:

import operator


# In[15]:

sorted_freqs = sorted(freqs.items(),key=operator.itemgetter(1))


# In[16]:

sorted_freqs


# In[17]:

print(len(urls))


# In[18]:

print(len(results))


# In[19]:

retweets = []


# In[20]:

for line in results:
    if ('RT' in line):
        retweets.append(line)


# In[21]:

retweets


# In[22]:

print(len(retweets))


# In[23]:

sorted_freqs.reverse()


# In[24]:

sorted_freqs


# In[25]:

len(sorted_freqs)

