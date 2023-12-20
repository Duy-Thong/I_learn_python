t = int(input())
lengths = []
list=[]
cnt7=0
for _ in range(t):
    s = input().strip()
    s1 = s.split()
    lengths.append(len(s1))
for i in range(len(lengths)-1):
    if lengths[i]==8 and lengths[i+1]==7:
        list.append(1)
    if lengths[i]==7 and lengths[i+1]==7:
        if cnt7==4:
            list.append(2)
            cnt7=0
        else: 
            cnt7+=1
    if lengths[i]==7 and lengths[i+1]==6:
        cnt7=0
        list.append(2)
if lengths[len(lengths)-1]==8:
    list.append(1)
else:
    list.append(2)
print(len(list))
for i in list:
    print(i)
