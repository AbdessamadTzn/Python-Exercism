def to_rna(dna_strand):
    table = str.maketrans(
        "GCTA",
        "CGAU"
    )
    result = dna_strand.translate(table)
    return result
