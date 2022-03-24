#Ricardo van der Lande


sequentie = \
    "tcgattcctgggaccggcaattaatttttttaattgccttgtattcaatagaaccgttcacaaataaacacatttccactattatgatgtcagtgaaagtgaatcttctatagcattaagctatcaatgtagaatagttgtatattgtatcctagttcttaatgttgacgatcccaccgatttttcacaagataaaacagggtcgtgtaccattctcaagaatgtaatgttcatcaaactttagagctacgatatattttattatgttagttgaatcataaagaatcacagtaattcaattataggtaatttaagttaattggttatgactgttgaatatgtaagtataaataatgagtt"


code = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
        'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
        'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
        'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
        'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
        'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
        'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
        'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
        'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
        'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
        'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
        'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
        'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
        'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
        'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
        'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
       }
"""
aa3 = {"Ala": ["GCU", "GCC", "GCA", "GCG"],
       "Arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
       "Asn": ["AAU", "AAC"],
       "Asp": ["GAU", "GAC"],
       "Cys": ["UGU", "UGC"],
       "Gln": ["CAA", "CAG"],
       "Glu": ["GAA", "GAG"],
       "Gly": ["GGU", "GGC", "GGA", "GGG"],
       "His": ["CAU", "CAC"],
       "Ile": ["AUU", "AUC", "AUA"],
       "Leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
       "Lys": ["AAA", "AAG"],
       "Met": ["AUG"],
       "Phe": ["UUU", "UUC"],
       "Pro": ["CCU", "CCC", "CCA", "CCG"],
       "Ser": ["UCU", "UCC", "UCA", "UCG", "AGU","AGC"],
       "Thr": ["ACU", "ACC", "ACA", "ACG"],
       "Trp": ["UGG"],
       "Tyr": ["UAU", "UAC"],
       "Val": ["GUU", "GUC", "GUA", "GUG"],
       "Start": ["AUG", "CUG", "UUG", "GUG", "AUU"],
       "Stop" : ["UAG", "UGA", "UAA"]
      }
"""
count = 0
while count < 6:
    try:
        # De ifs om de string in 6 verschillende ORFS te zetten.
        # Hieronder staat bij welke count welk RF erbij hoort.
        # 0:normal, 1:normal zonder de 1ste, 2:normal zonder de 1ste 2,
        # 3:reverse, 4:reverste zonder de 1ste, 5:reverse zonder 1ste 2.
        if count == 0:
            orfsequentie = sequentie
        elif count == 1:
            orfsequentie = sequentie[1:]
        elif count == 2:
            orfsequentie = sequentie[2:]
        elif count == 3:
            orfsequentie = sequentie[::-1]
        elif count == 4:
            orfsequentie = sequentie[-2::-1]
        elif count == 5:
            orfsequentie = sequentie[-3::-1]
        count += 1

        # Maakt de sequentie lowercase voor het geval dat er een
        # foutje met uppercase in zit.
        lijst = []
        orfsequentie = orfsequentie.lower()
        for i in range(0, len(orfsequentie), 3):
            lijst.append(orfsequentie[i:i+3])

        # Converteert de sequentie naar een eiwitsequentie.
        eiwitten = ""
        for i in range(len(lijst)):
            if len(lijst[i]) == 3:
                eiwitten += code[lijst[i]]

        # gaat door de eiwitten lijst heen en houdt de indexen van de
        # stopcodons bij die worden dan in de orflist gezet als
        # begin en eindpunt van de orf.
        orfindex1 = []
        orfindex2 = []
        orfdict = {}
        minimum_length = 70
        for i in range(len(eiwitten)):
            if eiwitten[i] == "*":
                if not orfindex1:
                    orfindex1.append(i)
                else:
                    orfindex2.append(i)
                    length = orfindex2[0] - orfindex1[0]
                    if length > minimum_length:
                        orfdict[eiwitten[orfindex1[0]:orfindex2[0]]] =\
                            "AAlength", length, "NTlength", length * 3
                        orfindex1.clear()
                        orfindex1 = orfindex2
                        orfindex2.clear()
                    else:
                        orfindex2.clear()
        print(orfdict)
    except KeyError:
        print("There is an unidentified or incorrect nucleotide in the "
              "sequence.")
