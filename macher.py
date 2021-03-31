import random as rd
import copy


# Mod 0 == 공격 1==수비
#TF = 경향성 사용여부
#hash = [id, 체력, 공격력]
def matcher (hashmap , AFA , trend , TF , Mod ) :
    ATKL = []
    DFEL = []
    KU = []
    if TF == 0 :
        if Mod == 0 : #ATK = 공격 DEF = 수비
            for i in range(len(hashmap)) :
                if hashmap[i][1] >= 0 :

                    if hashmap[i][0] <= int(AFA-1) :
                        ATKL.append(hashmap[i])
                    else :
                        DFEL.append(hashmap[i])
                else : pass

            if len(ATKL)!= len(DFEL) :
                if len(ATKL) > len(DFEL) :
                    NA = ATKL
                    NB = DFEL
                else : 
                    NB = ATKL
                    NA = DFEL

                for i in range(len(NB)) :
                    FGA = rd.choice(NA)
                    FGB = rd.choice(NB)
                    Rad = [[FGA] , [FGB]]
                    KU.append(Rad)
                    NA.remove(FGA)
                    NB.remove(FGB)

                for VK in range(max(len(NB),len(NA))) :
                    # 잉여부대 배당
                    PR = rd.choice(KU)
                    JV = rd.choice(NA)
                    NA.remove(JV)
                    KU.remove(PR)
                    PR.append(JV)
                    KU.append(PR)


            else : 
                NA = ATKL
                NB = DFEL
                for NJ in range(len(NB)) :
                    chedeA = rd.choice(NA)
                    chedeB = rd.choice(NB)
                    Rad = [[chedeA] , [chedeB]]
                    KU.append(Rad)
                    NA.remove(chedeA)
                    NB.remove(chedeB)

    return KU


def killere(KUL,A,B) : 
    KUc=KUL.copy() 
    for i in range(len(KUc)):
        LATK=[] 
        LDEF=[] 
        KUV=[]
        
        for j in range(len(KUc[i])): 
            Kre = KUc[i][j]
            if Kre in A:
                LATK.append(Kre) 
            elif Kre in B:
                LDEF.append(Kre) 

        KUV=[LATK,LDEF] 
        KUL.append(KUV)
        KUL.remove(KUc[i])
        
    return KUL 
         
        # 공격과 수비 list형식으로 구분
 # 입력 변수 : (공격 ID, 수비 ID ) - > 2회전시 그 역순
 # 출력 변수 : (ID전투배열)

def l_impatF (A,B,hpl) :
    # list 원본 저장(공격 ID , 수비 ID)
    Ap = A.copy()
    Bp = B.copy()

    if (len(A)!=len(B)) :
        Apx = copy.copy(A)
        Bpx = copy.copy(B)
        # 로컬 리스트 구축
        if len(A)>len(B) :
            NA = A
            NB = B
        elif (len(B)>len(A)) :
            NA = B
            NB = A

        KU = [] # 새로운 전투 배당리스트
        for NJ in range(len(NB)) :
            chedeA = rd.choice(NA)
            chedeB = rd.choice(NB)
            Rad = [chedeA , chedeB]
            KU.append(Rad)
            NA.remove(chedeA)
            NB.remove(chedeB)
        else :
            pass


        for VK in range(max(len(B),len(A))) :
            # 잉여부대 배당
            PR = rd.choice(KU)
            JV = rd.choice(NA)
            NA.remove(JV)
            KU.remove(PR)
            PR.append(JV)
            KU.append(PR)

        KJT = killere(KU,Apx,Bpx)
        return KJT

    else :         #만약 부대숫자가 동일하다면
        KU = []
        NA = A
        NB = B
        for NJ in range(len(NB)) :
            chedeA = rd.choice(NA)
            chedeB = rd.choice(NB)
            Rad = [[chedeA] , [chedeB]]
            KU.append(Rad)
            NA.remove(chedeA)
            NB.remove(chedeB)
        return KU








