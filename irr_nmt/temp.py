# import torch
# import gensim
#
# from onmt import inputters
# from onmt.inputters.inputter import _build_fields_vocab
#
# vocab = torch.load('data/europarl.vocab.pt')
# print(vocab)
#
# fields = inputters.get_fields(
#         # opt.data_type,
#         'text',
#         119547,
#         119547,
#
#     pad='<PAD>',
#     bos='<S>',
#     eos='<T>',
#         # with_align=opt.train_align[0] is not None,
#         # src_truncate=opt.src_seq_length_trunc,
#         # tgt_truncate=opt.tgt_seq_length_trunc)
# )
#
# fields = _build_fields_vocab(
#                 fields, counters, opt.data_type,
#                 opt.share_vocab, opt.vocab_size_multiple,
#                 opt.src_vocab_size, opt.src_words_min_frequency,
#                 opt.tgt_vocab_size, opt.tgt_words_min_frequency)
#
# print(fields)
#
# # print(vocab['indices'].use_vocab)
# # print(fields['src'][1])
# # print(fields['src'][0])