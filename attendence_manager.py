records = [
    ("Aman", "2025-01-01", "P"),
    ("Aman", "2025-01-02", "A"),
    ("Aman", "2025-01-03", "P"),
    ("Neha", "2025-01-01", "P"),
    ("Neha", "2025-01-02", "P"),
    ("Ravi", "2025-01-01", "A"),
    ("Ravi", "2025-01-02", "A"),
    ("Ravi", "2025-01-03", "P")
]
d={}#dict of names,total no of days and no of present days.
for i in records:
    name=i[0]
    day=i[2]
    if name  not in d:
        d[name]=[0,0]
    d[name][0]+=1

    if day=="P":
        d[name][1]+=1
#creating a list of names with percentage
l=[]
for i in d:
    a=(d[i][1]/d[i][0])*100
    b=round(a,2)
    l.append((i,b))
#sorting the list on the bases of percentage
l.sort(key=lambda x:x[1],reverse=True)
print("attendence record")
for i in l:
    if i[1]< 75:
        print(i[0],":",i[1],"<-- below 75%")
    else:
        print(i[0],":",i[1])
