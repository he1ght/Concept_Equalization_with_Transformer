import math
import sys
import numpy as np
from itertools import count

def txt2dict(directory):
    f = open(directory, "r", encoding="utf8")
    vecs = {}
    while True:
        line = f.readline()
        if not line:
            break
        line = line.split()
        word = line.pop(0)
        vec = [float(v) for v in line]
        vecs[word] = vec
    f.close()
    return vecs

def get_stat(vecs):
    all_vec = []
    all_vec_length = []
    for word, vec in vecs.items():
        all_vec += vec
        vec_length = np.sqrt(np.sum([e ** 2 for e in vec]))
        all_vec_length.append(vec_length)

    min_elm = min(all_vec)
    max_elm = max(all_vec)
    mean_elm = np.mean(all_vec)
    std_elm = np.std(all_vec)

    min_length = min(all_vec_length)
    max_length = max(all_vec_length)
    mean_length = np.mean(all_vec_length)
    std_length = np.std(all_vec_length)

    stats = {'min_element': min_elm, 'max_element': max_elm, 'mean_element': mean_elm, 'std_element': std_elm,
             'min_length': min_length, 'max_length': max_length, 'mean_length': mean_length, 'std_length': std_length}
    return stats


if __name__ == '__main__':
    vectors = txt2dict(sys.argv[1])
    # print(vectors)
    stats = get_stat(vectors)
    print(stats)