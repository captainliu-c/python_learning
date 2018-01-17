#print("begin")
L = [[1]]
org = [1]
i = 1
while i < 3:
    j = 1
    print("L:",L,"ORG",org,"i&j",i,j)
    while j < i:
        org[j] = L[i-1][j-1]+L[i-1][j]
        print("in L:",L)
        j = j+1
    org.append(1)
    print("L:",L,"ORG",org,"i&j",i,j)
    i = i+1
    print("L:",L,"ORG",org,"i&j",i,j)
    L.append(org)
    print("L:",L,"ORG",org,"i&j",i,j)
print("first loop done")
for i in L:
    print(i)
