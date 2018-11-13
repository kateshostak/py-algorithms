#Given a base-10 integer,n, convert it to binary (base-2).
#Then find and print the base-10 integer denoting the maximum
#number of consecutive 1's in n's binary representation.


def find_sequence_length(string, char):
    max_sequence = 0
    sequence_length = 0
    sequences = list()
    for elem in string:
        if elem == char:
            sequence_length += 1
        else:
            if sequence_length > max_sequence:
                max_sequence = sequence_length
            sequence_length = 0

    return max(max_sequence, sequence_length)

if __name__ == '__main__':
    n = int(input())
    bin_n = format(n, 'b')
    print(find_sequence_length(bin_n, '1'))
