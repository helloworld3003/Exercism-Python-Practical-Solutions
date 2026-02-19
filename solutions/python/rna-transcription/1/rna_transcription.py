def to_rna(dna_strand):
    defination=[['G','C'],['C','G'],['T','A'],['A','U']]
    rna=""
    for letters in dna_strand:
        for d in defination:
            if letters==d[0]:
                rna=rna+d[1]
    return rna
