import random as rd
import copy


#[i,BTLH[i],BTLA[i]]
def canonbat (hashmap,AFA,aritforce) :
    NAFAL = []
    for u in range(len(hashmap)) :
        if hashmap[u][0] >= AFA+1 :
            NAFAL.append(hashmap[u])
    for i in range(AFA) :
        if aritforce[hashmap[i][0]] >= 1 :
            PK = rd.choice(NAFAL)
            NWH = [PK[0],PK[1] - aritforce[hashmap[i][0]],PK[2]]
            hashmap[PK[0]] = NWH

        else :
            0
    Chashmap =copy.deepcopy(hashmap)
    KL = []
    for j in range(len(hashmap)) :
        if hashmap[j][1] <= 0 :
            KL.append(hashmap[j])
            Chashmap.remove(hashmap[j])
    return [Chashmap,KL]
