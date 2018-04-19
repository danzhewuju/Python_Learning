#!usr/bin/python
def solution(string, markers):
    string += "\n"
    result = string
    first = -1
    end = -1
    index = 0
    length = len(string)
    while index < length:
        if result[index] in markers:
            first = index
            result = result[:index-1]+result[index:]
            length -= 1
            first -= 1
            index -= 1
        if first != -1 and result[index] == "\n":
            end = index
            tem = result
            result = tem[:first]+tem[end:]
            length -= end - first
            index -= (end - first)
            first = -1
        index += 1
    result = result[:len(result)-1]
    return result


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["!", "#"]))





