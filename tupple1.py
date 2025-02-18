l1 = [('darshit','Ashit','devang'),'ragi','aashna','darshini',('darshil',)]
bcount = 0
gcount = 0
for name in l1:
    if(isinstance(name,tuple)):
        for n in name:
            bcount +=1
    else:
        gcount +=1
print("no of boys = ",bcount)
print("no of girls = ",gcount)
