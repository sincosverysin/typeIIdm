from collections import OrderedDict
d=OrderedDict() #d[source]=[targets]

lines=open('id_target_source.csv').readlines()
for line in lines[42:-1]:
    id,target,source=line.strip().split(',')
#   print(id,target,source)
    if source not in d:d[source]=[target]
    else:d[source].append(target)

path=[]
def forward(source):
    if source in d:
        path.append(source)
        for target in d[source]:
            forward(target)

forward('1')

path=[] #path[i]=[1,2,3,4,9,8,11,13,15]
for source,targets in d.items():
#   print(source,targets)
    path.append(target)
    

def all_paths():
    return [1,2,3,4,5,6,7]

