#For given n segments find the minimal set of dots
#such that every dot lies at least in one of the segments.
from operator import itemgetter

def find_min_set(segments):
    segments.sort(key=itemgetter(1))
    min_set = list()
    dot = segments[0][1]
    min_set.append(dot)
    for segment in segments[1:]:
        if dot < segment[0]:
            dot = segment[1]
            min_set.append(dot)
    return min_set

def main():
    segments = list()
    n = int(input())
    for i in range(n):
        segment = list(map(int, input().split(' ')))
        segments.append(segment)
    print(find_min_set(segments))

if __name__ == '__main__':
    main()
