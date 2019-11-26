fw = open('sample.txt','w')
fw.write('I want to make a difference in this wolrd\n')
fw.write('I need to improve my willpower\n')
fw.close()


fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()