import binascii


def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")

# def mod_inverse(e,phi):
#     # See: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
#     def extendedEuclideanAlgorithm(a,b):
#         if b==0:
#             return (1,0)
#         else:
#             (q,r) = (a//b,a%b)
#             (s,t) = extendedEuclideanAlgorithm(b,r)
#             return (t, s-(q*t) )
#
#     inv = extendedEuclideanAlgorithm(e,phi)[0]
#
#     if inv < 1: inv += phi #we only want positive values
#     return inv

# https://rosettacode.org/wiki/Modular_inverse#Python
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

# https://rosettacode.org/wiki/Modular_inverse#Python
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

c1 = 613757444204638278262310351562876531607487738717774407185252131147104492450160428757483976067628603514761619532764928239807564974590961450735755461481051283186240767490110455431475543041011912015289781128865893349142785039408178696523937605624371679605130950843591197358935516266254687080122972023592091964871
c2 = 22657108022478695797486965023447848250682406595690518779077232421899889165762724488153241456845951937121308084431913683848889272505486222688188138471999687468256556616878979818168438370975399291696045396880071048188564812795530986969364538462949239012254381251606438993964309325106863727351705595563360310007
c3 = 311096000497881387953904724284440481805457233048982756757007020410000443330941053703716829538086459727079448020579354693958905904778381820371160626001594619419169121166486655254993091181369105737797409452734836563374374511516011594235202125201067840325349354834604004321427713901643355933701994777952169157646

n1 = 1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627
n2 = 405864605704280029572517043538873770190562953923346989456102827133294619540434679181357855400199671537151039095796094162418263148474324455458511633891792967156338297585653540910958574924436510557629146762715107527852413979916669819333765187674010542434580990241759130158992365304284892615408513239024879592309
n3 = 1204664380009414697639782865058772653140636684336678901863196025928054706723976869222235722439176825580211657044153004521482757717615318907205106770256270292154250168657084197056536811063984234635803887040926920542363612936352393496049379544437329226857538524494283148837536712608224655107228808472106636903723

N = n1 * n2 * n3

print(N)

N1 = n2 * n3
N2 = n1 * n3
N3 = n1 * n2

d1 = modinv(N1, n1)
d2 = modinv(N2, n2)
d3 = modinv(N3, n3)

x = (c1*N1*d1) + (c2*N2*d2) + (c3*N3*d3)
answer = x % N
print(answer)

# enter answer into factordb to find the cubic root and then convert it string
finalanswer = 11301526147910562593480172641704694161465423096780624709953790635636739226559722703113272085678800268554213086475832 # factordb result
decrypted = int2string(finalanswer)

print(decrypted)