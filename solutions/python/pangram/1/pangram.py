def is_pangram(sentence):
    
    my_set = set(c for c in sentence.lower() if c.isalpha())
    return len(my_set)==26
