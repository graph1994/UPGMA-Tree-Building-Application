import re

class taxa:
    def __init__(self, id, data,size,distance):
         self.id = id
         self.data = data
         self.size = size
         self.distance = distance

#Set up the new data structure 
def form_taxas(species):
    taxas = {}
    ids = 1
    for item in species:
        x = taxa(ids,item,1,0)
        taxas[x.id] = x
        ids = ids + 1
    return taxas
def find_min(dic, array):
    lowest = None
    iMin = 0
    jMin = 0
    for i in dic:
        for j in dic:
            if j>i:
                tmp = array[j -1 ][i -1]
                
                if not lowest:
                    lowest = tmp
                    
                if tmp <= lowest:
                    iMin = i
                    jMin = j
                    lowest = tmp
    return (iMin, jMin, lowest)



def combine(dic_taxas,matrix):
    while len(dic_taxas) != 1:
        i,j,dij = find_min(dic_taxas,matrix)
        icluster = dic_taxas[i]
        jcluster = dic_taxas[j]
        
        u = taxa(max(dic_taxas) +1, (icluster,jcluster),(icluster.size + jcluster.size),(dij))
        del dic_taxas[i]
        del dic_taxas[j]
        matrix.append([])
        for l in range(0, u.id -1):
            matrix[u.id-1].append(0)
        for l in dic_taxas:
            dil = matrix[max(i, l) -1][min(i, l) -1]
            djl = matrix[max(j, l) -1][min(j, l) -1]
            dul = (dil * icluster.size + djl * jcluster.size) / float (icluster.size + jcluster.size)
            matrix[u.id -1][l-1] = dul
        dic_taxas[u.id] = u
           
    return dic_taxas


def taxaPrint(tax, distance):
    if tax.size > 1:
        print("(", end = "")
        taxaPrint(tax.data[0], tax.distance)
        print ("," ,end = ""),
        taxaPrint(tax.data[1], tax.distance)
        print ("," + str(tax.distance) ,end = ")")
    else :
        
        print ("%s" % (tax.data), end = "")
        

species = []
mdata = []
file = input("File name:")
with open(file) as f:
    for line in f:
        if '>' in line:
            species.append(line[2:].strip())  
        else:
            mdata = mdata + line.split(" ")
              
for m in range(0,len(mdata)):
    if mdata[m] == "":
        del mdata[m]
    else:
        mdata[m]= float(mdata[m].replace("\n",""))
    
matrix = [[0 for x in range(len(species))] for x in range(len(species))]
count = 0
for x in range(1,len(species)):
    for y in range(0,x):
        matrix[x][y] = mdata[count]
        count+= 1
            

    #matrix = [ [ 0, 0, 0, 0, 0, 0, 0 ],[ 19, 0, 0, 0, 0, 0, 0 ],[ 27, 31, 0., 0., 0., 0, 0 ],[ 8, 18, 26, 0., 0, 0, 0 ],[ 33, 36, 41, 31, 0, 0, 0 ],[18, 1, 32, 17, 35, 0, 0 ],[13, 13, 29, 14, 28, 12, 0 ]]
dic_taxas = form_taxas(species)

test = combine(dic_taxas,matrix)

for u in test:
    taxas = test[u]
taxaPrint(taxas,taxas.distance)





