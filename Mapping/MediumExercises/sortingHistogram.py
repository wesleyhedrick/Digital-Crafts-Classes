# sentence = input('Give me a sentence.\n')
sentence = 'hat cat cat fat hat cat'
sentence = sentence.split(' ')

wordSummary = {}

for word in sentence:
    if str(word).lower() in wordSummary:
        wordSummary[str(word).lower()] += 1
    else:
        wordSummary[str(word).lower()] = 1

print(wordSummary)
counts = []

for word in wordSummary:
    counts.append(wordSummary[word])

counts = list(set(counts))
counts.sort(reverse = True)

print(counts)

output = []

for i in counts:
    for j in wordSummary:
        if wordSummary[j] == i:
            output.append({'word': j, 'count': i})
            print(j, i)


# print(output)
#Iterations of the Code
#1
# i = 3, j = 'hat', wordSummary['hat] = 2
# 3 = 3
#no append
#2
#i = 3, j = 'cat', wordSummary['cat'] = 3
# 3 == 3
#output.append({'word': 'cat', 'count': 3})
#output[{'word': 'cat', 'count': 3}]
#3
#i = 3, j = 'fat', wordSummary['fat'] = 1
# 3 == 1
# no append
#4
