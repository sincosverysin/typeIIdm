data=[]
for line in open("dm2_topo.csv").readlines():
   # print "-1"
   # print type(line.split(",")[0])
    li = []
    for number in line.split(","):
        if number.isdigit():
            li.append(int(float(number)))
        else:
            li.append(number)
    data.append(li)
print data
#def find_neighbors(id):
 #   if id in range(1,42):

