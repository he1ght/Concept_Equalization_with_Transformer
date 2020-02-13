""" Onmt NMT Model base class definition """
import torch
import torch.nn as nn


class NMTModel(nn.Module):
    """
    Core trainable object in OpenNMT. Implements a trainable interface
    for a simple, generic encoder + decoder model.

    Args:
      encoder (onmt.encoders.EncoderBase): an encoder object
      decoder (onmt.decoders.DecoderBase): a decoder object
    """

    def __init__(self, encoder, decoder, ce_layer=None):
        super(NMTModel, self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.ce_layer = ce_layer

    def forward(self, src, tgt, lengths, bptt=False, with_align=False):
        """Forward propagate a `src` and `tgt` pair for training.
        Possible initialized with a beginning decoder state.

        Args:
            src (Tensor): A source sequence passed to encoder.
                typically for inputs this will be a padded `LongTensor`
                of size ``(len, batch, features)``. However, may be an
                image or other generic input depending on encoder.
            tgt (LongTensor): A target sequence passed to decoder.
                Size ``(tgt_len, batch, features)``.
            lengths(LongTensor): The src lengths, pre-padding ``(batch,)``.
            bptt (Boolean): A flag indicating if truncated bptt is set.
                If reset then init_state
            with_align (Boolean): A flag indicating whether output alignment,
                Only valid for transformer decoder.

        Returns:
            (FloatTensor, dict[str, FloatTensor]):

            * decoder output ``(tgt_len, batch, hidden)``
            * dictionary attention dists of ``(tgt_len, batch, src_len)``
        """
        new_cost = None
        dec_in = tgt[:-1]  # exclude last target from inputs

        enc_state, memory_bank, lengths = self.encoder(src, lengths)

        if bptt is False:
            self.decoder.init_state(src, memory_bank, enc_state)
        dec_out, attns = self.decoder(dec_in, memory_bank,
                                      memory_lengths=lengths,
                                      with_align=with_align)
        if self.ce_layer:
            c_s = torch.sum(memory_bank, 0)
            v_s = self.ce_layer(c_s)
            v_t = torch.sum(dec_out, 0)

            # CE type 2 : hamming distance
            # new_cost = euclidean_distance(v_s, v_t)
            new_cost = hamming_distance(v_s, v_t)
        return dec_out, attns, new_cost

    def update_dropout(self, dropout):
        self.encoder.update_dropout(dropout)
        self.decoder.update_dropout(dropout)


def euclidean_distance(inputs, target):
    return torch.sqrt(torch.sum((inputs - target) ** 2))


def hamming_distance(inputs, target, eps=1e-3):
    # [n_seq x batch x emb]
    batch_size = inputs.size(1)
    # c = torch.abs(inputs - target) > eps
    c = inputs != target
    c = torch.sum(c)
    return c / batch_size
