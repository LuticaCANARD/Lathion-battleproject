import pandas as pd
import numpy as np

AFAi = input("공격부대수 : ")

AFA = int(AFAi)
FuAFA = AFA-1

Battlelistdf = pd.read_excel ("testr1.xlsx")

armyID = Battlelistdf.shape[0]
al = [ i for i in range(armyID) ]


#print(np.array(Battlelistdf['부대체력'].tolist()))
#print(np.array(Battlelistdf['부대전투력'].tolist()))<

ATKL_ID = [ i for i in range (AFA)]
DEFL_ID = [x for x in [i for i in range(Battlelistdf.shape[0])] if x not in ATKL_ID]
BTLA = np.array(Battlelistdf['부대전투력'].tolist())
BTLH = np.array(Battlelistdf['부대체력'].tolist())
CDe = np.array(Battlelistdf['포격'].tolist())

Hashmap_ID_HP_ATK = []

for i in range(Battlelistdf.shape[0]) :
    KN = [i,BTLH[i],BTLA[i]]
    Hashmap_ID_HP_ATK.append(KN)
print(Hashmap_ID_HP_ATK)


def toex(otp) :
    #otp= [[,],[,]]
    for i in range (len(otp)) :
        Battlelistdf.iloc[otp[i][0],2] = otp[i][1]
    
    Battlelistdf.iloc[:,3] -= 1
    Battlelistdf.to_excel('output.xlsx')
    return Battlelistdf


print(Battlelistdf)