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


def translate(n):
    st = ""
    if n <= 0:
        st = "00"
    else:
        if n > 255 :
            st = "ff"
        else:
            st = str(hex(n))
            st = st[2:4]
            if len(st) == 1:
                st = "0" + st
    return st


def rgb(r, g, b):
    result = translate(r)
    result += translate(g)
    result += translate(b)
    result = result.upper()
    return result


print(rgb(0, 123, 1))