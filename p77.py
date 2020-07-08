def cal_pack(sal,ta,da):
    pack=(sal+ta+da)*12
    return pack

l1=["name1","name2","name3","name4","name5"]
l2=[]

#........calling cal_pack Function.......
e1=cal_pack(100,00,0)
e2=cal_pack(200,200,50)
e3=cal_pack(300,400,50)
e4=cal_pack(400,200,50)
e5=cal_pack(500,300,50)

#.......addng in list2........
l2.append(e1)
l2.append(e2)
l2.append(e3)
l2.append(e4)
l2.append(e5)

print(l2)

#..............max and Min................
mxp=max(l2)
minp=min(l2)
            #print(mxp)
            #print(minp)

#........index of max and min......................
mxpi=l2.index(mxp)
            #print(mxpi)
minpi=l2.index(minp)
            #print(minpi)

#....Show max and Mix pakage with employ name......
print(l1[mxpi],"has Max Pack: ",mxp)
print(l1[minpi],"has Min Pack: ",minp)




