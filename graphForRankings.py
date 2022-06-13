from turtle import color
import matplotlib.pyplot as plt
import json
import numpy as np
import os
import random
#Deprecated valuesArray.append(data['deprecated'])
#Normal                    


directory = 'G:/rankings'
count = 0
fileNameArray = []
valuesDeprecatedArray = []
valuesNormalArray = []
valuesPreferredArray = []
valuesCountArray = []

for filename in os.listdir(directory):
    #if count < 100:
     #   rand = random.randint(1,100)
      #  if rand % 2 == 0:
            f = os.path.join(directory, filename)
            if not filename.startswith('errors'):
                with open(f,'r') as file:  
                    data = json.load(file)
                    
                    entity = str(filename.replace('.json',''))
                    fileNameArray.append(entity)
                    valuesDeprecatedArray.append(data['deprecated'])
                    valuesNormalArray.append(data['normal'])
                    valuesPreferredArray.append(data['preferred'])
                    valuesCountArray.append(data['count'])

                    count+=1
#ind = np.arange(len(fileNameArray))
#plt.figure()
#plt.bar(ind, valuesDeprecatedArray, tick_label=fileNameArray, width=0.7, color='red')
#plt.xticks(fontsize=4, rotation =90)

#plt.figure()
#plt.bar(ind, valuesNormalArray, tick_label=fileNameArray, width=0.7, color='orange')
#plt.xticks(fontsize=4, rotation =90)

#plt.figure()
#plt.bar(ind, valuesPreferredArray, tick_label=fileNameArray, width=0.7, color='green')
#plt.xticks(fontsize=4, rotation =90)

#plt.figure()
#plt.bar(ind, valuesCountArray, tick_label=fileNameArray, width=0.7, color='purple')
#plt.xticks(fontsize=4, rotation =90)
#plt.show()       
    
#MEDIA    
#mediaDeprecated = np.mean(valuesDeprecatedArray)       
#mediaNormal = np.mean(valuesNormalArray)       
#mediaPreferred = np.mean(valuesPreferredArray)       
#mediaCount = np.mean(valuesCountArray)  
#print('Deprecated: '+str(mediaDeprecated))
#print('Normal: '+str(mediaNormal))     
#print('Preferred: '+str(mediaPreferred))     
#print('Count: '+str(mediaCount))     
     
#plt.figure()
#plt.xticks(fontsize=5, rotation =90)
#plt.bar([1,2,3,4],[mediaDeprecated,mediaNormal,mediaPreferred,mediaCount],tick_label=['Deprecated', 'Normal', 'Preferred', 'Count'], width=0.7, color=['red','orange','green','purple'])



#PIE CHART

sumDeprecated = np.sum(valuesDeprecatedArray)       
sumNormal = np.sum(valuesNormalArray)       
sumPreferred = np.sum(valuesPreferredArray)       
plt.pie([sumDeprecated, sumNormal, sumPreferred], labels= ['Deprecated','Normal','Preferred'], colors=['red','orange','green'],startangle=90, shadow= True, radius=1.2, autopct='%1.1f%%')
plt.legend()
    
#plt.figure()
#plt.bar(ind, getDeprecatedArray(values), tick_label ='deprecated',width= 0.7, color = 'red')

#plt.figure()
#plt.bar(ind, getNormalArray(values) ,tick_label ='normal',width= 0.7, color = 'yellow')

#plt.figure()
#plt.bar(ind, getPrefferedArray(values), tick_label ='preferred',width= 0.7, color = 'green')

  
# naming the x-axis
#plt.xlabel('Entities-Rank')
# naming the y-axis
#plt.ylabel('Values')
# plot title
#plt.title('Rankings distribution')
  
# function to show the plot
plt.show()
