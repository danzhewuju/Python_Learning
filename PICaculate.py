#!/usr/bin/python
import time


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
        number = int(ra[-index]) + int(rb[-index]) + tem
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


def format_number(a):
    result = a
    if "." in result:
        index = 1
        while result[-index] == "0":
            result = result[:-index]
        if result[-1] == ".":
            result = result[:-1]
    index = 0
    while result[index] == "0":
        result = result[index+1:]
    if result[0] == ".":
        result = "0"+result
    return result


def radd(a, b):
    ra = a
    rb = b
    lena = len(a);
    lenb = len(b)
    if lena < lenb:
        for index in range(lenb - lena):
            ra = "0" + ra
    else:
        for index in range(lena - lenb):
            rb = "0" + rb
    tem = 0
    result = ""
    time = max([lenb, lena])
    i = 1
    while i <= time:
        number = int(ra[-i]) + int(rb[-i]) + tem
        tem = 0
        if number >= 10:
            number -= 10
            tem = 1
        result += str(number)
        i += 1
    result = result[::-1]
    if tem == 1:
        result = "1" + result
    return result


def aadd(a, b):
    ra = a
    rb = b
    numbera = ra.split(".");
    numberb = rb.split(".")
    result = ""
    lena = len(numbera);
    lenb = len(numberb)
    if lena == 1 and lenb == 1:
        result = radd(ra, rb)
    else:
        if lena == 2 and lenb == 2:
            resultb = ladd(numbera[1], numberb[1])
            resulta = radd(numbera[0], numberb[0])
            resultbb = resultb.split(".")
            if resultbb[0] == "1":
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
    result = format_number(result)
    return result


def division(a, b, time):
    result = ""
    ca = a
    cb = b
    count = 0
    if ca % cb == 0:
        result = str(ca / cb)
    else:
        int_count = len(str(ca // cb))
        while ca % cb != 0 and count < time:
            tem = ca // cb
            result += str(tem)
            ca = ca - cb * tem
            ca *= 10
            count += 1
        if ca % cb == 0 and ca != 0:
            result += str(ca / cb)
        result = result[:int_count] + "." + result[int_count:]
    return result


def mul(a, b):
    result = ""
    tem = 0
    if len(a) > len(b):
        ra = b[::-1]
        rb = a[::-1]
    else:
        ra = a[::-1]
        rb = b[::-1]
    count = 0
    if "." in ra:
        ra = ra[:ra.index(".")] + ra[ra.index(".") + 1:]
    if "." in rb:
        rb = rb[:rb.index(".")] + rb[rb.index(".") + 1:]
    for x in ra:
        multime = ""
        for y in rb:
            rt = (int(x) * int(y) + tem)
            tem = 0
            if rt >= 10:
                tem = rt // 10
                rt %= 10
            multime += str(rt)
        if tem != 0:
            multime += str(tem)
        multime = multime[::-1]
        if count == 0:
            result = multime
        else:
            for index in range(count):
                multime += "0"
            result = aadd(result, multime)
        count += 1
    dec = 0
    if "." in a and "." in b:
        dec = len(a) - 1 - a.index(".") + len(b) - 1 - b.index(".")
    else:
        if "." not in a and "." not in b:
            dec = 0
        else:
            if "." in a and "." not in b:
                dec = len(a) - 1 - a.index(".")
            else:
                dec = len(b) - 1 - b.index(".")
    if dec >= len(result):
        d = dec-len(result)+1
        for index in range(d):
            result = "0"+result
    if dec != 0:
        result = result[:-dec] + "." + result[-dec:]
    result = format_number(result)
    return result


def caculate_pi(time, dec):
    pi = "0"
    ra = 1
    rb = 3
    tem = "1"
    pi = aadd(pi, "1")
    for index in range(time):
        tem = mul(tem, division(ra, rb, dec))
        pi = aadd(pi, tem)
        ra += 1
        rb += 2
    pi = mul(pi, "2")
    return pi


start = time.clock()
# print(mul("1.570553001", "2"))
result = caculate_pi(50,100)
f = open("PI.txt", "w+")
print(result)
length = len(result)
count = 0; raw = 0
while count < length:
    raw = 0
    while raw < 100 and count < length:
        f.write(result[count])
        raw += 1
        count += 1
    f.write("\n")
print len(result)-1, "bit"
f.write(str(len(result)-1)+"bit")
end = time.clock()
f.write("\n"+"Running Time:" + str(end - start)+"s")
f.close()
print "Running Time:", (end - start), "s"
