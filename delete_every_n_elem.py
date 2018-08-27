def delete_elem(arr, n):
    i = 1
    for elem in arr:
        if i % n == 0:
            arr.remove(elem)
        i += 1
    return arr


def main():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 2
    print(delete_elem(arr, n))

if __name__ == '__main__':
    main()
