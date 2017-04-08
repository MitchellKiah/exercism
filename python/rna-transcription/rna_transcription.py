def to_rna(dna):
    """
    input: string, dna strand
    return: string, complement RNA strand
    """
    rna = []

    for char in dna.upper():
        if char == 'G':
            rna.append('C')
        elif char == 'C':
            rna.append('G')
        elif char == 'T':
            rna.append('A')
        elif char == 'A':
            rna.append('U')
        else:
            return ''
    return ''.join(rna)
