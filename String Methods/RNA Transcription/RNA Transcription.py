def to_rna(dna_strand):
    mydict = {71: 67, 67: 71, 84: 65, 65: 85}
    return dna_strand.translate(mydict)