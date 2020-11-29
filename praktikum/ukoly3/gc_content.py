from fast import FastaReader
import matplotlib.pyplot as plt
import random

reader = FastaReader("yersinia.fasta")
_, sequence = next(reader)
sequence = sequence.upper()


def gc_content(seq: str):
    count = seq.count("G") + seq.count("C")
    if len(seq) == 0:
        return 0
    gc_perc = count / len(seq) * 100
    return gc_perc


global_GC = gc_content(sequence)


def gc_content_for_runs(seq: str, length: int):
    runs = []
    gc_runs = []
    j = 0
    for i in range(length, len(seq), length):
        gc = gc_content(seq[j:i])
        assert len(seq[j:i]) == length
        gc_runs.append(gc)
        runs.append(seq[j:i])
        j = i
    return runs, gc_runs


def display_gc(gcs, colors, avg):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    for i in range(len(gcs)):
        ax.scatter(range(0, len(gcs[i])), gcs[i], color=colors[i], marker="+")
    ax.set_xlabel('run #')
    ax.set_ylabel('GC %')
    ax.set_title('GC content in the genome of Yersinia pseudotuberculosis')
    if avg:
        ax.axhline(y=avg)
    plt.show()


runs, gc_runs = gc_content_for_runs(sequence, 100000)
#display_gc([gc_runs], ["r"], 0)


randomized_seq = list(sequence).copy()
random.shuffle(randomized_seq)
randomized_seq = "".join(randomized_seq)
runs_rand, gc_rand = gc_content_for_runs(randomized_seq, 100000)


#display_gc([gc_runs, gc_rand], ["r", "g"], 0)
#display_gc([gc_runs, gc_rand], ["r", "g"], global_GC)


runs_small, gc_small = gc_content_for_runs(sequence, 50000)
runs_long, gc_long = gc_content_for_runs(sequence, 200000)
runs_offset, gc_offset = gc_content_for_runs(sequence[30000:], 100000)

fig, ax = plt.subplots(3)
fig.suptitle('GC content in the genome of Yersinia pseudotuberculosis')
ax[0].plot(range(0, len(gc_small)), gc_small, color="r")
ax[1].plot(range(0, len(gc_long)), gc_long, color="r")
ax[2].plot(range(0, len(gc_offset)), gc_offset, color="r")
ax[0].set_xlabel('run #')
ax[1].set_xlabel('run #')
ax[2].set_xlabel('run #')
ax[0].set_ylabel('GC %')
ax[1].set_ylabel('GC %')
ax[2].set_ylabel('GC %')
ax[0].set_title('step length 50 000', rotation='vertical', x=-0.1, y=0.8)
ax[1].set_title('step length 200 000', rotation='vertical', x=-0.1, y=0.8)
ax[2].set_title('offset 30 000', rotation='vertical', x=-0.1, y=0.8)
ax[0].axhline(y=global_GC)
ax[1].axhline(y=global_GC)
ax[2].axhline(y=global_GC)
plt.show()
