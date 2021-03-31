import PDinputer as Pin
import macher as mat
import canonbat as can
import Battleshot as batt

CANA = can.canonbat(Pin.Hashmap_ID_HP_ATK,Pin.AFA,Pin.CDe)
NHash = CANA[0]
KL = CANA[1]
print("포격으로 죽은부대")
print(KL)

MTP = mat.matcher(NHash,Pin.AFA,0,0,0)
print(MTP )
