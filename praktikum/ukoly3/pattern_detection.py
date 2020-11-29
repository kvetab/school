import random
import numpy as np

bases = {"A": 0, "C": 1, "G": 2, "T": 3, "a": 0, "c": 1, "g": 2, "t": 3}

def find_pattern(seqs, k):
    kmers = []
    new_indices = []
    indices = []
    iteration = 0
    for seq in seqs:
        index = random.randint(0, len(seq) - k - 1)
        kmer = seq[index:index + k]
        kmers.append(kmer)
        new_indices.append(index)
    while indices != new_indices:
        iteration += 1
        pssm = create_pssm(kmers, k)
        kmers = []
        indices = new_indices
        new_indices = []
        for seq in seqs:
            index = find_best_kmer(seq, pssm, k)
            kmers.append(seq[index:index + k])
            new_indices.append(index)
        print(f"Iteration {iteration}, best k-mers: ", kmers)
    return kmers, indices, iteration


def create_pssm(kmers, k):
    # pseudocounts
    pfm = np.full((4, k), 0.1)
    for kmer in kmers:
        for i in range(k):
            base = bases[kmer[i]]
            pfm[base, i] += 1
    pssm = pfm / len(kmers)
    return pssm


def vectorize_sequence(seq):
    matrix = np.zeros((len(seq), 4))
    for i in range(len(seq)):
        base = bases[seq[i]]
        matrix[i, base] = 1
    return matrix


def find_best_kmer(seq, pssm, k):
    index = 0
    score = 0
    for i in range(len(seq) - k):
        vector = vectorize_sequence(seq[i:i+k])
        product = np.matmul(vector, pssm)
        new_score = np.prod(np.diagonal(product))
        if new_score > score:
            index = i
            score = new_score
    return index


sequences = [
    "ggggtccagctacgctatagggttaagcgcgtcgtcatgaccct",
    "gagccctctaccagctgacgagccctctgactggtcgcaggttg",
    "gatccggagcgagttactcaggcggagcagccatccataggggg",
    "tacttagtccggtggtcagcagataataatggaagaaatgacaa"
]

for i in range(20):
    kmers, indices, iters = find_pattern(sequences, 6)
    if iters > 2:
        print(indices)
        print(kmers)
