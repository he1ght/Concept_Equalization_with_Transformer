import torch
import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('~/codes/GoogleNews-vectors-negative300.bin', binary=True)

print(model)

weights = torch.FloatTensor(model.vectors)  # formerly syn0, which is soon deprecated


def from_pretrained(embeddings, freeze=True):
    assert embeddings.dim() == 2, \
        'Embeddings parameter is expected to be 2-dimensional'
    rows, cols = embeddings.shape
    embedding = torch.nn.Embedding(num_embeddings=rows, embedding_dim=cols)
    embedding.weight = torch.nn.Parameter(embeddings)
    embedding.weight.requires_grad = not freeze
    return embedding


embedding = from_pretrained(weights)
print(embedding)
# a = model.word_vec("King")
# b = model.word_vec("de")
# c = model.word_vec("européenne")

# print(model.vocab.keys())
print(len(model.vocab.keys()))

# x = torch.Tensor([model.vocab["King"].index]).long()
# print((embedding(x) - a).sum())
# print(model.distance("Apple", "Banana"))

# model.vectors[self.vocab[word].index]


# with open('../../../../codes/glove_dir/glove.6B.300d.txt', 'r') as f:
#     a = f.readlines()
#     lines = []
#     for line in a:
#         print(line)
#         break
#     print(len(a))
