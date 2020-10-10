# Iterator functions for reading in FASTA and FASTQ files

def FastaReader(filename):
    source = open(filename, 'r')
    header = ""
    while not header:
        line = source.readline()
        if line[0] == ">":
            header = line
    seq = []
    for line in source:
        if line[0] == ">":
            yield header, "".join(seq)
            header = line
            seq = []
        else:
            seq.append(line.strip())

    yield header, "".join(seq)
    source.close()


def FastqReader(filename):
    source = open(filename, 'r')
    line = source.readline()
    while len(line):
        header = line
        seq = next(source)
        comment = next(source)
        qual = next(source)
        yield header, seq, comment, qual
        line = next(source)

