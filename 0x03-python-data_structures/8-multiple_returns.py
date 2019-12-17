#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        result = None
    else:
        result = sentence[0]
    return len(sentence), result
