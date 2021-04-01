import PDinputer as Pin
import copy


def battlecall (Blist,VFV,Mo,bon,AR):
    #Blist의 구조: [전투[미소전투[부대]]]
    ATKL=[]
    HKP=[]
    Hashmap = []
    if Mo == 0 :
        for i in range(len(Blist)):
            for v in range(len(Blist[i])):
                if Blist[i][v][0] <=VFV-1:
                    ATKL.append(Blist[i][v][2])
                    Hashmap.append(Blist[i][v])
                else:
                    HKP.append(Blist[i][v])

            for N in range(len(HKP)):
                    UHP=copy.deepcopy(HKP[N][1]-(sum(ATKL)/len(HKP)))
                    HKP[N][1]=UHP
                    Hashmap.append(HKP[N])
                    
            ATKL.clear()
            HKP.clear()

            
    else : 
        for i in range(len(Blist)):
            for v in range(len(Blist[i])):
                if Blist[i][v][0] <=(VFV-1):
                    HKP.append(Blist[i][v])
                else:
                    
                    ATKL.append(Blist[i][v][2])
                    Hashmap.append(Blist[i][v])

            for N in range(len(HKP)):
                    UHP=copy.deepcopy(HKP[N][1]-(sum(ATKL)/len(HKP)))
                    HKP[N][1]=UHP
                    Hashmap.append(HKP[N])
                    
            ATKL.clear()
            HKP.clear()
             
    return Hashmap
