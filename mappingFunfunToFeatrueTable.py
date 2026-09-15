import os, sys

featureTable = sys.argv[1]
funfunOut = sys.argv[2]
outFile = sys.argv[3]

##############################################################
##Counting ASV
##############################################################
##Loading sample
b = open(featureTable,'r').readlines()
samples = b[1].replace("\n","").split("\t")
del samples[0]
del b[0:2]##delete header

counting = {}
for i in b:
    iList = i.replace("\n","").split("\t")
    for index in range(1,len(iList)):
        key = iList[0]+"#"+samples[index-1]
        value = float(iList[index])
        counting[key] = value

##############################################################
##Counting function
##############################################################
b = open(funfunOut,'r').readlines()
asvs = b[0].replace("\n","").split("\t")
del asvs[0]
del b[0]##delete header

function = {}
pathways = []
for i in b:
    iList = i.replace("\n","").split("\t")
    pathways.append(iList[0])
    for index in range(1,len(iList)):
        key = iList[0]+"#"+asvs[index-1]
        if iList[index] == "":
            value = 0
        else:
            value = float(iList[index])
        function[key] = value

##############################################################
##creating feature table
##############################################################
saveFile = open(outFile,"w")
header = "pathway\t" + "\t".join(samples) + "\n"
saveFile.write(header)

for pathway in pathways:
    dataRecord = []
    dataRecord.append(pathway)
    for sample in samples:
        num = 0.0
        for asv in asvs:
            n1 = pathway+"#"+asv
            n2 = asv+"#"+sample
            frequency = function[n1]*counting[n2]
            num = num + frequency
        dataRecord.append(str(num))
    saveFile.write("\t".join(dataRecord))
    saveFile.write("\n")
saveFile.close()  
