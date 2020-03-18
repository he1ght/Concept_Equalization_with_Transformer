python preprocess.py -save_data data/europarl -train_src data/train.fr -train_tgt data/train.en -valid_src data/test.fr -valid_tgt data/test.en

python preprocess.py -save_data data/bert_emb -train_src data/train.fr -train_tgt data/train.en -valid_src data/test.fr -valid_tgt data/test.en -src_vocab data/bert.vocab.txt -tgt_vocab data/bert.vocab.txt -src_vocab_size 119547 -tgt_vocab_size 119547