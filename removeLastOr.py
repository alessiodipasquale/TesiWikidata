import os
directory = 'G:/subjectForAPI/' 
list = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    with open(f,'rb+') as file: #rb+
        file.seek(-2, os.SEEK_END)
        file.truncate()
       #file.seek(-1, os.SEEK_END)
       #file.truncate()