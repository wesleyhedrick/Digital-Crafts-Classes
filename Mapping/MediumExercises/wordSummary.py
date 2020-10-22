sentence = input('Give me a sentence.\n')
sentence = sentence.split(' ')

wordSummary = {}

for word in sentence:
    if str(word).lower() in wordSummary:
        wordSummary[str(word).lower()] += 1
    else:
        wordSummary[str(word).lower()] = 1

print(wordSummary)    