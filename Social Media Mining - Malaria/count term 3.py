import csv

tweets = []
with open('t3w1.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='"')
    for row in reader:
      if '{' in row:
        if row[15] == 'source':
          text = row[13]
        else:
          text = row[13] + row[15]
        tweets.append(text)

# print tweets
vaccine_count = 0
for tweet in tweets:
  if 'outbreak' in tweet:
    vaccine_count+=1
    print tweet

print vaccine_count

tweets = []
with open('t3w2.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='"')
    for row in reader:
      if '{' in row:
        if row[15] == 'source':
          text = row[13]
        else:
          text = row[13] + row[15]
        tweets.append(text)

# print tweets
vaccine_count = 0
for tweet in tweets:
  if 'outbreak' in tweet:
    vaccine_count+=1
    print tweet

print vaccine_count