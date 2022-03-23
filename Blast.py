from Bio.Blast import NCBIWWW
import time


def blast(new_orf_list):
    """ Gebruikt NCBI qblast om een blastp uit te voeren
    op alle orfs uit de lijst en maakt gebruik van de functie
    writefile om de resultaten op te slaan
    :param new_orf_list: String list - Aa sequentie
    """
    count = 0
    for i in new_orf_list:
        seq = new_orf_list[count]
        print("Blasting sequence: " + i)
        result_handle = NCBIWWW.qblast("blastp", "nr", seq, word_size=3,
                                       matrix_name="BLOSUM62",
                                       alignments=10,
                                       expect=0.0001,
                                       hitlist_size=5)
        filename = i[:10] + ".XML"
        writefile(result_handle, filename)
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
    duration_start = time.time()
    testorf = ["MSFWPFSNTFNNNSQLQKFLDSIQDFSNVTVDDLLGDLDLLQELLSELHNIKGNYNNLTSFQFLQQP"
           "QQHESASNNQNADLASLASSNNENNNNYGKDTHGAKLLELLLQPHILNGFLDYIVNSVDFFHDLSIKEHNDLERLVQSEEI"
           "PEPQIEGNDEVEIEEAEELSQDNKNKDSEEETNEDKLRRCIQASSDVLSIDLWVILNRIIETPIVMSKLWLILSLP"
           "NLQESSPSVSYLVHILDQLMDTNSIELLNFIRRQKNLVDTFLNKIEIPMLMDFFLRVIQTDKADSPTGILETLSLQQLISKL"
           "IDILKPEPSQFKMNISNIPNHELFFKQTAATDFIKALVTISSNTALAVVLETNRELVSPRIIYTMINDIILYKVPMPDSNEVQTNK"
           "HGINNCVGIIIEVIRKNNSDYDLNCGTYSSMLQNGENGTGEINSYVMFQWLKDFEQNPPGTRDPIYLGDMLAIFSEHLDQFAELMDVQSIPPMNIDSEILGFTKFKMSELIAELLHCSNMILLNSKKIRKIIHIRDYVRLQQSKRLRKALD", "MLGNHRLTLYLSKEYRDKHWYAHKQIVYQFYRNRLQFHQESIKHYIYYIVHELPLKIEDDTSSCHQHLEVLALKLLLQ"]
    blast(testorf)
    print(time.time()-duration_start)



