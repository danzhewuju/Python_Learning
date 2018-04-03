#!usr/bin/python
def unique_in_order(iterable):
    yh = []
    c = ""
    for ch in iterable:
        if ch != c:
           yh.append(ch)
        c = ch
    return yh


def duplicate_encode(word):
    word = word.lower()
    dict = {}
    for c in word:
        if c in dict.keys():
           dict[c] += 1
        else:
           dict[c] = 1
    sen = ""
    for number in word:
       if dict[number] == 1:
           sen += "("
       else:
           sen += ")"
    return sen


print(duplicate_encode("Success"))
