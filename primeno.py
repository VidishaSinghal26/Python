fp=open("a.txt","w")
for i in range(1,101):
    if i>1:
        for j in range(2,i):
          if i%j==0:
            break
        else:
            fp.write(str(i)+"\n")
fp.close()         
      
