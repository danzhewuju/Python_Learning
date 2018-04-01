#!usr/bin/python


def mul(n, count):
    a = []
    sum = 1
    if n < 10:
        return count
    else:

        while n != 0:
            a.append(n % 10)
            n = int(n/10)
        for number in a:
            sum *= number
        return mul(sum, count+1)


def persistence(n):
    return mul(n, 0)


def friend(x):
    friends = []
    for name in x:
        if len(name) == 4:
            friends.append(name)
    return friends


b = ["Ryan", "Kieran", "Mark"]


def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def find_even_index(arr):
    sumnumber = sum(arr)
    suma = 0
    result = -1
    if arr.count(0) == len(arr):
        result = 0
    else:
        for index in range(len(arr)):
            if index > 0:
                suma += arr[index - 1]
                if sumnumber - suma - arr[index] == suma:
                    result = index
                    break
            else:
                if sumnumber - arr[index] == 0:
                    result = index
    return result


def tickets(people):
    people = sorted(people)
    flag = True
    suma = [0, 0, 0]
    for number in people:
        if number == 25:
            suma[0] += 1
        else:
            if number == 50:
                suma[1] += 1
                suma[0] -= 1
                if suma[0] < 0:
                    flag = False
                    break
            else:
                if suma[1] >= 1:
                    suma[2] += 1
                    suma[0] -= 1
                    suma[1] -= 1
                    if suma[0] < 0:
                        flag =False
                        break
                else:
                    suma[0] -= 3
                    suma[2] += 1
                    if suma[0] < 0:
                        flag =False
                        break
    if flag:
        return "YES"
    else:
        return "NO"


yh = [25, 100]
print(tickets(yh))













