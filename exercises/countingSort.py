def countingSort(input: list) -> list:
    length = len(input)
    k = max(input)
    output = [0] * length
    count = [0] * (k + 1)
    # print(output)
    # print(count)
    # for i in range(0, length):
    #     count[input[i]] += 1
    for num in input:
        count[num] += 1
    for i in range(1, k + 1):
        count[i] += count[i - 1]
    # for i in range(length-1,-1,-1):
    #     output[count[input[i]]-1] = input[i]
    #     count[input[i]] -= 1
    for num in reversed(input):
        output[count[num] - 1] = num
        count[num] -= 1
    return output


input = [2, 5, 3, 0, 2, 3, 0, 3]
result = countingSort(input)
print(result)
