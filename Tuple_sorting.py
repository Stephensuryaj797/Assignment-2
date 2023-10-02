My_tup=[]
n=int(input("Enter the number of tuples in the list: "))
for i in range(n):
    V=input("Enter tuple Ex: 2,3 (comma-separated values): ")
    M=V.split(',')
    tup=[]
    for s in M:
        tup.append(int(s))
    My_tup.append(tuple(tup))
if len(My_tup)==0:
    print('Please enter a list of tuple ')
print("Before Sorting",My_tup)
for i in range(len(My_tup)):
    for j in range(i+1,len(My_tup)):
        if My_tup[i][-1]>My_tup[j][-1]:
            My_tup[i],My_tup[j]=My_tup[j],My_tup[i]
print("After Sorting",My_tup)
