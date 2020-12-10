import json
import math
import sys


p = 5
opts = [[1, 2, 3, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 4, 5, 6, 7], [1, 2, 3, 4, 4, 4, 5, 6, 7]]


class HmmModel:
    def __init__(self, filename):
        """
        Load model from json representation. Model is (transitions, emissions, pi), where pi = initial distribution.
        :param filaname: Name of the model used to find file to load from
        """
        self.model = json.loads(open(filename).read())["hmm"]
        self.emissions = self.model["emissions"]
        self.states = self.emissions.keys()  # get the list of states
        self.N = len(self.states)  # number of states of the model
        self.symbols = next(iter(self.emissions.values())).keys()
        #self.symbols = self.emissions[self.emissions.keys()[0]].values()  # get the list of symbols, assume that all symbols are listed in the emission matrix
        self.M = len(self.symbols)  # number of states of the model

        # use log versions of probabilities
        self.log_transitions = {}
        self.log_emissions = {}
        self.log_pi = {}
        self.set_log_model()

    def set_log_model(self):
        for state in self.states:
            self.log_emissions[state] = {}
            for symbol in self.emissions[state].keys():
                self.emissions[state][symbol] += 1/p
                self.log_emissions[state][symbol] = math.log(self.emissions[state][symbol])

    def score_background(self, seq):
        return math.log(0.25) * 7.5
        # sequences are 6 to 9 long -> 7.5 is average

    def score_motif(self, seq):
        max_score = -1000
        for opt in opts:
            score = 0
            for i, sym in enumerate(opt):
                score += self.log_emissions['model' + str(sym)][seq[i]]
            if score > max_score:
                max_score = score
        return max_score

    def find_motif(self, seq):
        results = []
        for pos in range(len(seq) - 9):
            bckgrnd = self.score_background(seq[pos:pos+9])
            motif = self.score_motif(seq[pos:pos+9])
            res = "b" if bckgrnd > motif else "m"
            results.append(res)
        return "".join(results)


model = HmmModel("model.json")
res = model.find_motif("AGATCCATTGACCGTTACACATCAGATTGATAGATTGATTTTGATCGACAAAGTG")
print(res)
