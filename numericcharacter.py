a=raw_input()
n=len(a)
count=0
for i in range(0,n):
 if(a[i]>='1' and a[i]<='9'):
  count+=1
print(count)  
