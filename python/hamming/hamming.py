def distance(dna1, dna2):
    """
    Calculates the Hamming difference between two DNA strands of equal length.
    input: string, first dna strand
    input: string, second dna strand
    return: int, Hamming distance
    """
    if len(dna1) != len(dna2):
        raise ValueError('DNA Strands must be of equal length.')
    dna1Cap = dna1.upper()
    dna2Cap = dna2.upper()
    hamDist = 0
    for index in range(len(dna1)):
        if dna1Cap[index] != dna2Cap[index]:
            hamDist += 1
    return hamDist
