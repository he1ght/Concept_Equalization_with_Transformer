# import torch
# def euclidean_distance(inputs, target):
#     return torch.sqrt(torch.sum((inputs - target) ** 2))
#
# def hamming_distance(inputs, target, eps=1e-3):
#     # from scipy.spatial import distance
#     # distance.hamming(inputs, target)
#     # from scipy.spatial.distance import cdist
#     # return cdist(inputs, target, 'hamming')
#     c = torch.abs(inputs-target) > eps
#     c = torch.sum(c)
#     return c
#
# a = torch.rand((2,3,4))
# b = torch.rand((2,3,4))
# d1 = euclidean_distance(a, b)
# d2 = hamming_distance(a, b)
# print(d1)
# print(d2)