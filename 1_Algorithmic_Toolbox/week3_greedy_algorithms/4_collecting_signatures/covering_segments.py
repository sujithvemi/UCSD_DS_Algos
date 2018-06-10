# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    sort_seg = sorted(segments, key=lambda segment: segment.start)
    cur_point = sort_seg[0].start
    last_seg = 0
    while sort_seg:
        cur_seg = 0
        index = 0
        for seg in sort_seg:
            if cur_point >= seg.start and cur_point <= seg.end:
                index += 1
                cur_seg += 1
        if cur_seg >= last_seg:
            last_point = cur_point
            last_seg = cur_seg
            last_index = index
        else:
            points.append(int(last_point))
            last_seg = 0
            sort_seg = sort_seg[last_index:]
        cur_point += 0.5
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
