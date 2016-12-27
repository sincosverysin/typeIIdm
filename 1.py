for line in open("dm2_topo.csv").readlines():
   # print "-1"
   # print type(line.split(",")[0])
    if type(line.split(",")[0])==str:  
        if line.split(",")[1]=="na":
           print(line.split(",")[0])

