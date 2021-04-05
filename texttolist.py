import pandas as pd

def TXK (text) :
    il =[]
    for i in range(len(text)) :
        if text[i] == "[" :
            u = 0
            PA = []
            NM = []
            HP =[]
            NP= []
        elif text[i] == "/" :
            u += 1
        elif text[i] == "]" :
            NMt = ''.join(NM)
            NPt = ''.join(NP)
            HPt =int( ''.join(HP))
            PA = [NMt,NPt,HPt]
            il.append(PA)
        else : 
            if u == 0 :
                NM.append(text[i])
            elif u == 1 :
                NP.append(text[i])
            elif u == 2 :
                HP.append(text[i])


    return il

#이름 , 병종, 체력
infe = "[ 양반 / 양민 / 500 ] [ 수군 / 천민 / 500 ] [ 마모루 / 마릿츠3324 / 300 ]"
print(TXK (infe))

CP = input("텍스트 = :")
C = TXK (CP) 
PDA = pd.DataFrame(C,columns = ["이름","병종","체력"])
print(PDA)
PDA.to_excel('TESD.xlsx', sheet_name= 'ppap')




