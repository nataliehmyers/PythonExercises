def listGiven(terms):
    if len(terms) == 1:
        return terms[0]
    return '{}, and {}'.format(', '.join(terms[:-1]), terms[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']
print(listGiven(spam))
