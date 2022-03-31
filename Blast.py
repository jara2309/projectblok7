from Bio.Blast import NCBIWWW

import BestandLezen
import OrfZoeken



class Blast:
    def blast(new_orf_list, header_list):
        """ Gebruikt NCBI qblast om een blastp uit te voeren
        op alle orfs uit de lijst en maakt gebruik van de functie
        writefile om de resultaten op te slaan
        :param new_orf_list: String list - Aa sequentie
        """
        count = 0
        for i in new_orf_list:
            seq = new_orf_list[count]
            print("Blasting sequence:\n" + i)
            result_handle = NCBIWWW.qblast("blastp", "nr", seq, word_size=3,
                                           matrix_name="BLOSUM62",
                                           alignments=10,
                                           expect=0.0001,
                                           hitlist_size=5)
            filename = header_list[count] + ".XML"
            count += 1
            Blast.writefile(result_handle, filename)
            time.sleep(6)

    def writefile(result, filename):
        """ Maakt een bestand aan en schrijft meegegeven
        data naar het bestand
        :param result: Data
        :param filename: Bestandsnaam die niuew bestand krijgt
        :return:
        """
        print("Generating file...")
        with open(filename, 'w') as file:
            file.write(result.read())
        file.close()
        result.close()


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
        testlijst = []
        for key in header:
            for i in sequentie:
                count = 0
                while count < 6:
                    count, OrfSequentie = OrfZoeken.OrfZoeken.Orfmaker\
                        (i, count)
                    count += 1
                    eiwitten = OrfZoeken.OrfZoeken.\
                        SeqConverter(OrfSequentie)

                    orflist = OrfZoeken.OrfZoeken.Genefinder\
                        (eiwitten, MinimumLength)
                    if orflist != []:
                        testlijst.append(orflist)
            orfdict.update({key: testlijst[:]})
            testlijst.clear()
        list_header  = []
        list_seq = []
        counter = 0
        for key in orfdict:
            for list in (orfdict[key]):
                for i in range(0, len(list), 3):
                    counter+=1
                    list_seq.append(list[i])
                    list_header.append("Header: " + str(key) + " ORF: " + str(counter))

        try:
            blast(list_seq, header)
            print("Runtime in minutes: ")
        except ModuleNotFoundError:
            print("Biopython module not found")
        except ValueError:
            print("File containing Nucleotides instead of aminoacids")



