occ = 0

ln = int(input())

opt = {'ln': ln, 's':0, 'c':0, 'u': 0, 'o': 0}


with open("tweets2.txt", "r") as file:
    op = file.readlines()
    ret = op[ln - 1].split()
    for lttr in range(len(ret)):
        ret[lttr] = ret[lttr].strip("\"',.!?")
    for wp in ret:
        if len(wp) <= 3:
            opt['s']+=1
        else:
            opt['c']+=1
        
        if ret.count(wp) > 1:
            occur += 1


opt['o'] =len(ret)
opt['u'] = opt['o'] - occur
print(opt)