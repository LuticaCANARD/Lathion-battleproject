import PDinputer as Pin
import macher as mat
import canonbat as can
import Battleshot as batt

CANA = can.canonbat(Pin.Hashmap_ID_HP_ATK,Pin.AFA,Pin.CDe)
NHash = CANA[0]
KL = CANA[1]
print("포격으로 죽은부대")
print(KL)
KLP = []
for i in range(len(KL)) :
    UR = KL[i]
    KLP.append(UR)

MTP = mat.matcher(NHash,Pin.AFA,0,0,0)
EE = len(Pin.ATKL_ID) + len(Pin.DEFL_ID)
JR = batt.battlecall(MTP,Pin.AFA,0,0,EE)
print(JR)
EB= mat.matcher(NHash,Pin.AFA,0,0,0)
if EB == "전멸" :
    print("전반전에서 전멸하여 공격측의 완승")
    EN = Pin.repun(JR+KLP) 
    print(EN)

else :
    JE = batt.battlecall(EB,Pin.AFA,1,0,EE)
    EU = Pin.repun(JE+KLP) 
    print(EU)

