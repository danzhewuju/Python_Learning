#!usr/bin/python
def next_bigger(n):
    cp = n
    number = []
    while n != 0:
        number.append(n % 10)
        n /= 10
    p = 0
    for index in range(len(number)-1):
        if number[index] > number[index+1]:
            p = index + 1
            break
    back = number[0:p+1]
    tem = max(back)
    for x in back:
        if x > number[p] and x < tem:
            tem = x
    back[back.index(tem)] = number[p]
    number[p] = tem
    back.remove(back[p])
    p -= 1
    back.sort()
    back.reverse()
    for index in range(len(back)):
        number[index] = back[index]
    sum = 0
    number.reverse()
    for index in range(len(number)):
        sum += number[index]*pow(10, len(number)-index-1)
    if sum > cp:
        return sum
    else:
        return -1


print(next_bigger(143))