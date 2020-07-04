import googletrans
dictionaryList1=googletrans.LANGUAGES 			#It will give o/p in key and value pair
#print(dictionaryList1)  
dictionaryList2={}
count=0
for item in dictionaryList1.items():
	dictionaryList2[item[1]]=item[0]
	if(item[0]=='en'):
		print(count)
	count+=1				#To swap the key and value pair
print(dictionaryList2)

