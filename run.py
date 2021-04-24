import sent_analysis
import os 
positive, negative, neutral = sent_analysis.sentiment_analysis('newtwitter.csv', 'res1')

file1 = open("data.txt","w")
for item in [positive, negative, neutral]:
    file1.write(str(item)+"\n")
file1.close() 

os.system('python ./web/Application.py')