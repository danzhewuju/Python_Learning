#!usr/bin/python
def next_bigger(n):
    cp = n
    number = []
    while n != 0:
        number.append(n % 10)
        n /= 10
    for index in range(len(number)-1):
        if number[index] > number[index+1]:
            tem = number[index]
            number[index] = number[index+1]
            number[index+1] = tem
            break
    sum = 0
    number.reverse()
    for index in range(len(number)):
        sum += number[index]*pow(10, len(number)-index-1)
    if sum > cp:
        return sum
    else:
        return -1


print(next_bigger(1234567890))