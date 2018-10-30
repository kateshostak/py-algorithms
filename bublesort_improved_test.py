import bublesort_improved
import generate_random_arr


def test_bublesort_improved(arr):
    sorted_arr = sorted(arr)
    if bublesort_improved.bublesort(arr) == sorted_arr:
        return True


def main():
    arr = generate_random_arr.generate_arr(0, 9, 0, 100)
    passed = True
    for i in range(50):
        arr = generate_random_arr.generate_arr(0, 9, 0, 100)
        passed = passed and test_bublesort_improved(arr)

    if passed:
        print('OK')

if __name__ == '__main__':
    main()
