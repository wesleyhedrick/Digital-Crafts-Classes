word = input('Give me a word.\n')

letterSummary = {}

for letter in word:
    if str(letter).lower() in letterSummary:
        letterSummary[str(letter).lower()] += 1
    else:
        letterSummary[str(letter).lower()] = 1

print(letterSummary)    