import heapsort
import generate_random_arr

def test_heapsort(test_arr):
    sorted_arr = sorted(test_arr)
    my_arr = heapsort.heapsort(test_arr)
    if my_arr == sorted_arr:
        return True

def main():
    test_arr = generate_random_arr.generate_arr(1,50, 0, 100)
    if test_heapsort(test_arr):
        print('OK')

if __name__ == '__main__':
    main()