#===========================================
#============= READ DATA() =================

def read_data(filename):
    data = {}
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            data[row[0]] = row[1]
    return data


