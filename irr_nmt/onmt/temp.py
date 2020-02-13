import torch
def euclidean_distance(inputs, target):
    return torch.sqrt(torch.sum((inputs - target) ** 2))


def hamming_distance(inputs, target, norm=True):
    # [n_seq x batch x v_dim]
    v_dim = inputs.size(-1)

    ret = torch.abs(inputs - target)
    ret = torch.sum(ret, dim=-1)
    if norm:
        ret = ret / v_dim
    ret = torch.mean(ret)
    return ret

a = torch.rand((2,3,4))
b = torch.rand((2,3,4))

# print(a)
# print(b)

# d1 = euclidean_distance(a, b)
d2 = hamming_distance(a, b)
# print(d1)
print(d2)