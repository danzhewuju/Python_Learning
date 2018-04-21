#!/usr/bin/python
def ladd(a, b):
    result = ""
    lena = len(a)
    lenb = len(b)
    c = min([lena, lenb])
    index = 1
    tem = 0
    if c == lena:
       ra = b[:c]
       rb = a
    else:
        ra = a[:c]
        rb = b
    while index <= c:
        number = int(ra[-index])+int(rb[-index])+tem
        tem = 0
        if number > 9:
            tem = 1
            number -= 10
        result += str(number)
        index += 1
    if tem == 1:
        result += ".1"
    else:
        result += ".0"
    result = result[::-1]
    if c == lena:
        result += b[c:]
    else:
        result += a[c:]
    return result


def radd(a, b):
    ra = a; rb = b
    lena = len(a); lenb = len(b)
    if lena < lenb:
        for index in range(lenb-lena):
            ra = "0"+ra
    else:
        for index in range(lena-lenb):
            rb = "0"+rb
    tem = 0
    result = ""
    time = max([lenb, lena])
    i = 1
    while i <= time:
        number = int(ra[-i])+int(rb[-i])+tem
        tem = 0
        if number >= 10:
            number -= 10
            tem = 1
        result += str(number)
        i += 1
    result = result[::-1]
    if tem == 1:
        result = "1"+result
    return result


def aadd(a, b):
    ra = a; rb = b
    numbera = ra.split("."); numberb = rb.split(".")
    result = ""
    lena = len(numbera); lenb = len(numberb)
    if lena == 1 and lenb ==1:
        result = radd(ra, rb)
    else:
        if lena == 2 and lenb == 2:
            resultb = ladd(numbera[1], numberb[1])
            resulta = radd(numbera[0], numberb[0])
            resultbb = resultb.split(".")
            if resultbb[0] == 1:
                resulta = radd(resulta, "1")
                result = resulta + "." + resultbb[1]
            else:
                result = resulta + "." + resultbb[1]
        else:
            if lena == 2 and lenb == 1:
                tema = numbera
                temb = rb
            else:
                tema = numberb
                temb = ra
            resulta = radd(tema[0], temb)
            result = resulta + "." + tema[1]
    return result


def division(a, b, time):
    result = ""
    ca = a
    cb = b
    count = 0

    if ca % cb == 0:
        result = str(ca/cb)
    else:
        int_count = len(str(ca//cb))
        while ca % cb != 0 and count < time:
            tem = ca//cb
            result += str(tem)
            ca = ca-cb*tem
            ca *= 10
            count += 1
        if ca % cb == 0 and ca != 0:
            result += str(ca/cb)
        result = result[:int_count]+"."+result[int_count:]
    return result


print(aadd("982.18999", "108.21001"))

    








