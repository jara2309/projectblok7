import re


def bestandlezen(bestand):
    """ Deze functie openent een bestand en returnd de header en
        sequentie

    :param: bestand, ingevoerde bestand vanuit de bioloog
    :return: header - string - en sequentie - string -

    """
    header = []
    sequentie = []
    seq = ""

    with open(bestand) as bestand:

        for line in bestand:
            line = line.replace("\n", "")
            if ">" in line:
                header.append(line)
            elif not (re.search(r"[^ATGCN]]", line)):
                if not line == "":
                    seq += line
                    sequentie.append(seq)

        print(sequentie)




if __name__ == '__main__':
    bestand = "SD.fa"
    bestandlezen(bestand)


