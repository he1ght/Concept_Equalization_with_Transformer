#!/usr/bin/env bash
python train.py -word_vec_size 512 -feat_merge concat -model_type text -encoder_type transformer -decoder_type transformer -layers 4 -global_attention general -self_attn_type scaled-dot -data data/europarl -save_model model/vanila_transfer -gpu_ranks 0 -world_size 1 -batch_size 64 -train_steps 77895 -valid_steps 15579 -optim adadelta -dropout 0.3 -learning_rate 1 -learning_rate_decay 1 -log_file log/test.log -tensorboard -tensorboard_log_dir log/test -heads 8 -transformer_ff 2048 -rnn_size 512
% -fix_word_vecs_enc -fix_word_vec_dec -early_stopping
% word_vec_size == rnn_size
% model_dim % heads == 0
% number of examples: 997012 , batch size: 64 -> train_steps 15579 per 1 epoch
% tensorboard --logdir D:\Research\Concept_Equalization_with_Transformer\irr_nmt\log



python train.py -word_vec_size 512 -feat_merge concat -model_type text -encoder_type transformer -decoder_type transformer -layers 4 -global_attention general -self_attn_type scaled-dot -data data/europarl -save_model model/dummy -gpu_ranks 0 -world_size 1 -batch_size 64 -train_steps 1 -valid_step 10 -optim adadelta -dropout 0.3 -learning_rate 1 -learning_rate_decay 1 -log_file log/dummy -heads 8 -transformer_ff 2048 -rnn_size 512 -concept_equalization -max_generator_batches 0



2020.01.10 Vanila Tranformer
python train.py -word_vec_size 512 -feat_merge concat -model_type text -encoder_type transformer -decoder_type transformer -layers 4 -global_attention general -self_attn_type scaled-dot -data data/europarl -save_model model/2010.01.10.vanila -gpu_ranks 0 -world_size 1 -batch_size 64 -train_steps 778950 -valid_step 15579 -optim adadelta -dropout 0.3 -learning_rate 1 -learning_rate_decay 1 -log_file log/2010.01.10.vanila.log -heads 8 -transformer_ff 2048 -rnn_size 512 -max_generator_batches 0 --tensorboard -tensorboard_log_dir log/vanila
2020.01.10 Concept Equalization Transformer
python train.py -word_vec_size 512 -feat_merge concat -model_type text -encoder_type transformer -decoder_type transformer -layers 4 -global_attention general -self_attn_type scaled-dot -data data/europarl -save_model model/2010.01.10.concept_equalization -gpu_ranks 0 -world_size 1 -batch_size 64 -train_steps 778950 -valid_step 15579 -optim adadelta -dropout 0.3 -learning_rate 1 -learning_rate_decay 1 -log_file log/2010.01.10.concept_equalization.log -heads 8 -transformer_ff 2048 -rnn_size 512 -concept_equalization -max_generator_batches 0 --tensorboard -tensorboard_log_dir log/concept_equalization