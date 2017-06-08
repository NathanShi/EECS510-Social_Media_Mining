import csv
import re

c = r'*[vaccine]*'

keywords = ['vaccine','vaccination']
tweets = []
with open('t2w1.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='"')
    for row in reader:
      if '{' in row:
        print row
        if row[15] == 'source':
          text = row[13]
        else:
          text = row[13] + row[15]
        tweets.append(text)
# print "w1"
# print tweets
vaccine_count = 0
tweets_count = 0
for tweet in tweets:
  tweets_count +=1
  if any((re.match(r'absdfkjsbv', tweet, re.IGNORECASE)) for keyword in keywords):
    vaccine_count+=1

print vaccine_count
print tweets_count

tweets = []
with open('t2w2.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='"')
    for row in reader:
      if '{' in row:
        if row[15] == 'source':
          text = row[13]
        else:
          text = row[13] + row[15]
        tweets.append(text)
# print "w2"
# print tweets
vaccine_count = 0
for tweet in tweets:
  if any(keyword in tweet.lower() for keyword in keywords):
    vaccine_count+=1

print vaccine_count