file1 = open("C:/Users/manis/Downloads/Email1.txt","r+")
line_num=0
dat = file1.read()
split=dat.split();
#print(split);
'''
with open("C:/Users/manis/Downloads/Email2.txt") as myFile:
  for num, line in enumerate(myFile, 1):
      print(line);
'''
invoicenum=[]
count=0
skip=0
price=[]
for word in split:
    count+=1
    if ";" in word:
        invoicenum.append(word.replace(";",""));
    elif "$" in word:
        if skip==0:
            skip+=1
        else :
            skip=0
            price.append(word)
    elif "otr" in word.lower():
        invoicenum.append(word)
print(set(invoicenum))
print(price)
