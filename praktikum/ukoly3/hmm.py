import json
import math


p = 5
opts = [[1, 2, 3, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 4, 5, 6, 7], [1, 2, 3, 4, 4, 4, 5, 6, 7]]


def get_length_ungapped(sequence):
    return sum(1 for pos in sequence if pos != "-")


def log_odds(sequence, probability):
    length = get_length_ungapped(sequence)
    bckgrnd = 0.25**length
    score = math.log(probability / bckgrnd)
    return score


class HmmModel:
    def __init__(self, filename):
        """
        Load model from json representation.
        """
        model = json.load(open(filename))["hmm"]
        self.emissions = model["emissions"]
        self.transitions = model["transitions"]

    def score_sequence(self, sequence):
        sequence = sequence.strip()
        option = opts[get_length_ungapped(sequence) - 6]
        emission_probs = 1
        transition_probs = 1
        for i, state in enumerate(option):
            if sequence[i] != "-":
                emission_probs *= self.emissions["model" + str(state)][sequence[i]]
            if i > 0:
                transition_probs *= self.transitions["model" + str(last_state)]["model" + str(state)]
            last_state = state
        return emission_probs * transition_probs


def score_alignment_sequences():
    # Task no. 1
    # (Matrix already contains pseudocounts)
    model = HmmModel("model.json")
    with open("alignment.txt", "r") as f:
        alignment = f.readlines()
    for seq in alignment:
        prob = model.score_sequence(seq)
        logodds = log_odds(seq, prob)
        print(f"Sequence: {seq.strip()}; score: {logodds}")


def search_sequence(sequence, model):
    # Task no. 2
    probs = {}
    pos_probs = {}
    for opt in opts:
        window = len(opt)
        probs[window] = []
        for pos in range(len(sequence) - window + 1):
            subseq = sequence[pos:pos + window]
            score = model.score_sequence(subseq)
            probs[window].append(score)
            pos_probs[pos] = pos_probs.get(pos, []) + [(window, score)]

    maxprob = 0
    maxpos = -1
    for pos, probs in pos_probs.items():
        probs.sort(key=lambda x: x[1], reverse=True)
        if pos_probs[pos][0][1] > maxprob:
            maxpos = pos
            maxprob = pos_probs[pos][0][1]
    window = pos_probs[maxpos][0][0]
    result_string = "b" * maxpos + "m" * window + "b" * (len(sequence) - maxpos - window)
    return result_string


sequence = "AGATCCATTGACCGTTACACATCAGATTGATAGATTGATTTTGATCGACAAAGTG"

score_alignment_sequences()
print()

model = HmmModel("model.json")
print(sequence)
res_string = search_sequence(sequence, model)
print(res_string)
