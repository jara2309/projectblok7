def openfasta(path):
    """ Opent file, voegt headers toe aan headerarray
    en voegt sequenties toe aan sequentie array
    :param path: Bestandsnaam / bestandslocatie
    :return:seqs: Array met sequenties
            headers: Array met headers
    """
    seq = ""
    seqs = []
    headers = []
    file = open(path)
    x=0
    for line in file:
        if (">" in line): #Controleer of regel header is
            if x>0:
                seqs.append(seq) #Sequentie toevoegen aan array seqs
            headers.append(line.replace("\n", ""))  # Headers toevoegen aan array headers
            seq = "" #Sequentie leegmaken voor nieuwe seq
            x+=1
        else:
            seq += line.replace("\n", "") #Enters weghalen en Seqbuilder
    if seq != "":
        seqs.append(seq) #Voeg laatse sequentie toe
    file.close()

    return seqs, headers


if __name__ == '__main__':
    try:
        s, h = openfasta("SD.fa")
        if not s:
            print("Warning: No sequences found")
    except FileNotFoundError:
        print("File not found, check filepath")