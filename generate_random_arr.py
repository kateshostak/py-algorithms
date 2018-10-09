import random

def generate_arr(len_min, len_max, int_min, int_max ):
    arr = list()
    arr_length = random.randint(len_min, len_max)
    for i in range(arr_length):
        arr.append(random.randint(int_min, int_max))

    return arr
