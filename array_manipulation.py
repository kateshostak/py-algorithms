def arrayManipulation(n, queries):
    arr = [0]*n
    for line in queries:
        a, b, k = line[0], line[1], line[2]
        for i, elem in enumerate(arr[a:b+1]):
            arr[i+a] += k
        print(arr)
    return max(arr)

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)
