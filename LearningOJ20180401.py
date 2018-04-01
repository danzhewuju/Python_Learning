#!usr/bin/python
def unique_in_order(iterable):
    yh = []
    c = ""
    for ch in iterable:
        if ch != c:
           yh.append(ch)
        c = ch
    return yh


print(unique_in_order("AAABBBCCCGGTTTC"))
