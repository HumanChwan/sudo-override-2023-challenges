from Crypto.Util.number import long_to_bytes, inverse
from gmpy2 import iroot

e = 3

n1 = 7712665439054718801677881785612553647515222289773403356728017066774875303084180996995551772705015359441910324281951003644383985696149628026781841252140219
n2 = 7516375989297551865433612573482386602082633394354015310506338394861520519532730967365482533292545503134270143440449045994659031928888283650671184290022859
n3 = 8930462496785621465846278042933252294301525791148443378963281385218198917264173611718577548562474300423868750876951938779141643294250018797251329923807921

c1 = 6237846984197584534166465480000122720912559379417334610362100408319534655429045396200288295004402354335343432655217780890501480257815604820206615772420417
c2 = 7148985146571013572546256897237051555639429949657014720398919205505637817913697262375289738332742287042492511470875406357705251569420178429804865342692995 
c3 = 1549528573180828709707776185871440958504816185479208923022709771870490036669002581231033691044256406711895189565019814115510878288318366423947827439226616

N = n1 * n2 * n3
N1 = N//n1
N2 = N//n2
N3 = N//n3

u1 = inverse(N1, n1)
u2 = inverse(N2, n2)
u3 = inverse(N3, n3)

M = (c1*u1*N1 + c2*u2*N2 + c3*u3*N3) % N

m = iroot(M, 3)[0]
print(m)
print(long_to_bytes(m))