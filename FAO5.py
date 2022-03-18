li=list(input().split())

win_set=[ 10, 11, 8, 1, 5, 20 ]
win_number=0


e=1
d={}

if(len(li)==7):
    for i in range(1,7):
        if int(li[i]) in d:
            e=0
            break
        else:
            d[int(li[i])]=1
        if(int(li[i]) in win_set):
            win_number+=100
    if e:
        if win_number!=0:
            print(li[0],"wons",win_number,"pesos!")
        else:
            print(li[0],"won nothing!")
    else:
        print("No Duplicates")
else:
    print("Should be 6 numbers")
