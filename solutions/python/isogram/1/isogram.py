from collections import Counter
def is_isogram(phrase):
    phrase_ = phrase.lower()
    count = Counter(phrase_)
    res = [c for c in phrase_ if count[c]==1 and c.isalpha()]
    count_ = 0
    for c in phrase_:
        if c.isalpha():
            count_ += 1
    return len(res) == count_
        
    