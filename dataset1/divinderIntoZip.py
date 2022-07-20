import os
import zipfile

dir_path = "G:\DATASETCOMPLETO"

zipCounter = 8
numberOfFiles =len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])
print("numberOfFiles: "+str(numberOfFiles))
forEachZip = numberOfFiles / zipCounter;
print("forEachZip: "+str(forEachZip))

i = 0
fileCounter = 0
zf = zipfile.ZipFile("G:\Dataset1ZIPPED\script\script%s.zip" % fileCounter, "w")
for dirname, subdirs, files in os.walk(dir_path):
    zf.write(dirname)
    for filename in files:
        #print(filename)
        zf.write(os.path.join(dirname, filename))
        i+=1
    if (i>forEachZip):
        print("New file: "+str(fileCounter))
        i = 0;
        fileCounter += 1
        zf.close()
        zf = zipfile.ZipFile("G:\Dataset1ZIPPED\script\script%s.zip" % fileCounter, "w")
zf.close()