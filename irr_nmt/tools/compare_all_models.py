
import nltk
from nltk.translate.bleu_score import SmoothingFunction
import configargparse as cfargparse


def config_opts(parser):
    parser.add('-config', '--config', required=False,
               is_config_file_arg=True, help='config file path')
    parser.add('-save_config', '--save_config', required=False,
               is_write_out_config_file_arg=True,
               help='config file save path')


def compare_opts(parser):
    group = parser.add_argument_group('Opts')
    group.add('-ref', required=True,
              help="")
    group.add('-pred', required=True, default=[], nargs='*', type=str,
              help="")
    group.add('-pred_ce', required=True, default=[], nargs='*', type=str,
              help="")


def _get_parser():
    parser = cfargparse.ArgumentParser()

    config_opts(parser)
    compare_opts(parser)
    return parser


def read_list_of_words(directory, ref=False):
    list_of_words = []
    f = open(directory, "r", encoding="utf8")
    while True:
        line = f.readline()
        if not line:
            break
        words = line.split()
        if ref:
            list_of_words.append([words])
        else:
            list_of_words.append(words)
    f.close()
    return list_of_words


def measure_bleu(ref, pred):
    # chencherry = SmoothingFunction()
    bleu_score = nltk.translate.bleu_score.sentence_bleu(ref, pred)  # , smoothing_function=chencherry.method4)
    return bleu_score


if __name__ == '__main__':

    parser = _get_parser()

    opt = parser.parse_args()
    assert len(opt.pred) == len(opt.pred_ce)
    assert len(opt.pred) > 0
    list_of_references = read_list_of_words(opt.ref, ref=True)
    list_of_hypothesis = [read_list_of_words(h) for h in opt.pred]
    list_of_hypothesis_ce = [read_list_of_words(h) for h in opt.pred_ce]

    total_cnt = len(list_of_references)
    better_line_list = []
    for hypothesis, hypothesis_ce in zip(list_of_hypothesis, list_of_hypothesis_ce):
        idx = 0
        better_line = []
        for src, hyp, hyp_ce in zip(list_of_references, hypothesis, hypothesis_ce):
            bleu_score = measure_bleu(src, hyp)
            bleu_score_ce = measure_bleu(src, hyp_ce)
            round_bleu_score = round(bleu_score, 4) * 100
            round_bleu_score_ce = round(bleu_score_ce, 4) * 100
            if bleu_score_ce > bleu_score:
                better_line.append(idx)
            idx += 1
        better_line_list.append(better_line)

    intersection = None
    for better_line in better_line_list:
        if intersection is None:
            intersection = set(better_line)
        else:
            intersection = intersection.intersection(set(better_line))
    intersection = list(intersection)
    intersection.sort()
    better_cnt = len(intersection)
    for idx in intersection:
        print("No. {}".format(idx + 1))
        print("REF: {:15s}".format(" ".join(list_of_references[idx][0])))
        for i, (hypothesis, hypothesis_ce) in enumerate(zip(list_of_hypothesis, list_of_hypothesis_ce)):
            print("{:15s}: {}".format(opt.pred[i].split('/')[-1][:-4], " ".join(hypothesis[idx])))
            print("{:15s}: {}".format(opt.pred_ce[i].split('/')[-1][:-4], " ".join(hypothesis_ce[idx])))
        print()
    print(intersection)
    round_better_score = round(better_cnt/total_cnt, 4) * 100
    print("Better score: {:.2f}% ({}/{})".format(round_better_score, better_cnt, total_cnt))
