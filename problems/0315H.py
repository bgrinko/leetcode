def brut(freq):
    result = [0] * freq.__len__()
    for i in range(freq.__len__()):
        for j in range(i + 1, freq.__len__()):
            if freq[i] > freq[j]:
                result[i] += 1
    return result


def find(tree, el):
    low = 0
    high = tree.__len__() - 1

    while low <= high:
        mid = low + (high - low) // 2
        if tree[mid] == el:
            for j in range(mid, -1, -1):
                if tree[j] != el:
                    tree = tree[:j + 1] + [el] + tree[j + 1:]
                    return tree, j
        elif tree[mid] < el < tree[mid + 1]:
            tree = tree[:mid + 1] + [el] + tree[mid + 1:]
            return tree, mid
        elif tree[mid] < el:
            low = mid + 1
        else:
            high = mid - 1


def main():
    freq = [i for i in range(-100000, 100000)]

    # for i in range(1000):
    #     freq.append(random.randint(1, 10000))
    #
    # print(freq)

    # freq = [3, 5, 1, 6, 3, 2, 0, 5, 14, 2]
    # r1 = brut(freq)
    # print(r1)

    freq.reverse()
    tree = [-10000000, 10000000]
    n = freq.__len__()

    result = []
    for i in range(n):
        tree, k = find(tree, freq[i])
        result.append(k)
    result.reverse()
    # print(result)
    # print(r1 == result)


main()
