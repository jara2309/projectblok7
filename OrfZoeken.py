# Ricardo van der Lande
import BestandLezen


class OrfZoeken:

    def Orfmaker(sequentie, count):
        """
        De ifs om de string in 6 verschillende ORFS te zetten.
        Hieronder staat bij welke count welk RF erbij hoort.
        0:normal, 1:normal zonder de 1ste, 2:normal zonder de
        1ste 2, 3:reverse, 4:reverste zonder de 1ste, 5:reverse
        zonder 1ste 2.
        :param sequentie, count:
        :return: count, Orfsequentie
        """
        if count == 0:
            OrfSequentie = sequentie
        elif count == 1:
            OrfSequentie = sequentie[1:]
        elif count == 2:
            OrfSequentie = sequentie[2:]
        elif count == 3:
            OrfSequentie = sequentie[::-1]
        elif count == 4:
            OrfSequentie = sequentie[-2::-1]
        elif count == 5:
            OrfSequentie = sequentie[-3::-1]
        return count, OrfSequentie

    def SeqConverter(OrfSequentie):
        """
        Maakt de sequentie lowercase voor het geval dat er een
        foutje met uppercase in zit.
        Maakt ook een lijst van de sequentie in parts van 3
        nucleotiden
        :param: Orfsequentie
        :return: eiwitten
        """
        AminoDict = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
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

        lijst = []
        OrfSequentie = OrfSequentie.lower()
        for i in range(0, len(OrfSequentie), 3):
            #Gooit n eruit aangezien die niet gebalst kan worden
            if "n" not in OrfSequentie[i:i+3]:
                lijst.append(OrfSequentie[i:i + 3])
            else:
                pass
        # Converteert de sequentie naar een eiwitsequentie.
        try:
            eiwitten = ""
            for i in range(len(lijst)):
                if len(lijst[i]) == 3:
                    eiwitten += AminoDict[lijst[i]]
        except KeyError:
            print(
                "There is an unidentified or incorrect nucleotide in "
                "the "
                "sequence.")
        return eiwitten

    def Genefinder(eiwitten, MinimumLength):
        """
        gaat door de eiwitten lijst heen en houdt de indexen van de
        stopcodons bij die worden dan in de orflist gezet als
        begin en eindpunt van de orf.
        :param: MinimumLength:
        :return: eiwitten, MinimumLength
        """
        orfindex1 = []
        orfindex2 = []
        orflist = []
        for i in range(len(eiwitten)):
            if eiwitten[i] == "*":
                if not orfindex1:
                    orfindex1.append(i + 1)
                else:
                    orfindex2.append(i)
                    if len(orfindex1) == 2:
                        length = orfindex1[1] - orfindex1[0]
                        if length > int(MinimumLength):
                            orflist.append(eiwitten[orfindex1[
                                                        0]:orfindex1[
                                1]])
                            orflist.append("Amino acid length:" + str(
                                length))
                            orflist.append("Nucleotide length:" + str(length
                                           * 3))
                            orfindex1.clear()
                            orfindex1 = orfindex2
                            orfindex2.clear()
                        else:
                            pass
                    else:
                        orfindex1.clear()
                        orfindex1 = orfindex2
                        orfindex2.clear()
        return orflist

    if __name__ == '__main__':
        MinimumLength = input("wat is de minimale lengte die je wil "
                              "hebben voor de Genen?")


        try:
            sequentie, header = BestandLezen.BestandLezen.openfasta(
                input("Enter filepath: "))
            if not sequentie:
                print("Warning: No sequences found")
        except FileNotFoundError:
            print("File not found, check filepath")
        orfdict = {}
        rfgenelijst = []
        for i in range(len(header)):
            count = 0
            while count < 6:
                count, OrfSequentie = Orfmaker(sequentie[i], count)
                count += 1
                eiwitten = SeqConverter(OrfSequentie)
                orflist = Genefinder(eiwitten, MinimumLength)
                if orflist != []:
                    rfgenelijst.append(orflist)
            orfdict.update({header[i]: rfgenelijst[:]})
            rfgenelijst.clear()
