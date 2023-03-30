from math import log10, log, exp, pow
from random import randint

# Pseudocritical Properties
def ppc_sutton(sg):
    return 756.8 - 131*sg - 3.6*(sg**2)
def tpc_sutton(sg):
    return 169.2 + 349.5*sg - 74*(sg**2)
def ppc_standing(sg):
    if sg < 0.75:
        return 667 + 15*sg - 37.5*(sg**2)
    else:
        return 706 - 51.7*sg - 11.1*(sg**2)
def tpc_standing(sg):
    if sg < 0.75:
        return 168 + 325*sg - 12.5*(sg**2)
    else:
        return 187 + 330*sg - 71.5*(sg**2)

# Impurities
def sg_corrected(sg, yn2, yco2, yh2s):
    return (sg - (yn2*28.014 + yco2*44.01 + yh2s*34.1))/(28.97*(1 - yn2 - yco2 - yh2s))
def tpc_corrected_wicherta(tpc, yco2, yh2s):
    eps = 120*(((yh2s+yco2)**0.9) - ((yh2s+yco2)**1.6)) + 15*((yh2s**0.5) - (yh2s**4))
    return tpc - eps
def ppc_corrected_wicherta(ppc, tpc, yn2, yco2, yh2s):
    eps = 120*(((yh2s+yco2)**0.9) - ((yh2s+yco2)**1.6)) + 15*((yh2s**0.5) - (yh2s**4))
    return (ppc*tpc_corrected_wicherta(tpc, yco2, yh2s))/(tpc + (eps*yh2s*(1-yh2s)))
def tpc_corrected_carrkb(tpc, yn2, yco2, yh2s):
    return tpc - 80*yco2 + 130*yh2s - 250*yn2
def ppc_corrected_carrkb(ppc, yn2, yco2, yh2s):
    return ppc + 440*yco2 + 600*yh2s - 170*yn2

def Ppr(p, ppc):
    return p/ppc
def Tpr(t, tpc):
    return t/tpc

# Compressibility Factor (z)
def z_hally(ppr, tpr):
    y = 10
    eps = 0.0000000001
    rep = 0
    trecip = 1/tpr
    x1 = -0.06125*ppr*trecip*exp(-1.2*((1-trecip)**2))
    x2 = 14.76*trecip - 9.76*(trecip**2) + 4.58*(trecip**3)
    x3 = 9.07*trecip - 242.2*(trecip**2) + 42.4*(trecip**3)
    x4 = 2.18 + 2.82*trecip
    fy = 1
    while abs(fy) > eps:
        if y < 0:
            y *= -1
        fy = x1 + ((y + (y**2) + (y**3) +(y**4))/((1-y)**3)) - x2*(y**2) + x3*(y**x4) if y != 1 else 0
        dfy = ((1 + 4*y + 4*(y**2) - 4*(y**3) + (y**4))/((1-y)**4)) - 2*x2*y + x3*x4*(y**(x4-1)) if y != 1 else 0
        y = y - (fy/dfy) if dfy else 0
        rep += 1
        if rep > 150 or y == 0:
            y = randint(1, 50)
            continue
    return (0.06125*ppr*trecip/y)*exp(-1.2*((1-trecip)**2))

def z_dak(ppr, tpr):
    y = 10
    eps = 0.0000000001
    rep = 0
    r1 = 0.3265 - 1.07/tpr - 0.5339/(tpr**3) + 0.01569/(tpr**4) - 0.05165/(tpr**5) if tpr else 0
    r2 = 0.27*ppr/tpr if tpr else 0
    r3 = 0.5475 - 0.7361/tpr + 0.1844/(tpr**2) if tpr else 0
    r4 = 0.1056*(-0.7361/tpr + 0.1844/(tpr**2)) if tpr else 0
    r5 = 0.6134/(tpr**3) if tpr else 0
    fy = 1
    while abs(fy) > eps:
        fy = r1*y - r2/y + r3*(y**2) - r4*(y**5) + r5*(1+0.721*(y**2))*(y**2)*exp(-0.721*(y**2)) - 1 if y else 0
        dfy = r1 + r2/(y**2) + 2*r3*y - 5*r4*(y**4) + 2*r5*y*exp(-0.721*(y**2))*((1+2*0.721*(y**3)) - 0.721*(y**2)*(1+0.721*(y**2))) if y else 0
        y = y - (fy/dfy) if dfy else 0
        rep += 1
        if rep > 150 or y == 0:
            y = randint(1, 50) if y else 0
            continue
    return 0.27*ppr/(y*tpr) if tpr else 0

def z_brillb(ppr, tpr):
    a = 1.39*((tpr-0.92)**0.5) - 0.36*tpr - 0.1
    e = 9*(tpr - 1)
    b = (0.62 - 0.23*tpr)*ppr + (0.066/(tpr - 0.86) - 0.037)*(ppr**2) + 0.32*(ppr**2)/(10**e)
    c = 0.132 - 0.32*log10(tpr)
    f = 0.3106 - 0.49*tpr + 0.1824*(tpr**2)
    d = 10**f
    return a + (1-a)/exp(b) + c*(ppr**d)

# Density (rho)
def densityg(sg, p, t, z):
    if t != 0:
        pass
    else:
        t += 0.00000000001
    if z != 0:
        pass
    else:
        z += 0.00000000001
    rho = p*sg*28.97/(z*10.732*t)
    return rho

# Gas Viscosity(mug)
def mug_carrkb(sg, yn2, yco2, yh2s, ppr, tpr, tres):
    tres = tres + 460
    mul_uncorrected = (1.709*0.00001 - 2.062*0.000001*sg)*tres + 8.118*0.003 - 6.15*0.003*log10(sg)
    muco2 = yco2*(9.08*0.001*log10(sg) + 6.24*0.001)
    mun2 = yn2*(8.48*0.001*log10(sg) + 9.59*0.001)
    muh2s = yh2s*(8.49*0.001*log10(sg) + 3.73*0.001)
    mul = mul_uncorrected + muco2 + mun2 + muh2s
    a0 = -2.46211820
    a8 = -0.793385648
    a1 = 2.970547414
    a9 = 1.39643306
    a2 = -0.286264054
    a10 = -0.149144925
    a3 = 0.00805420522
    a11 = 0.00441015512
    a4 = 2.80860949
    a12 = 0.0839387178
    a5 = -3.49803305
    a13 = -0.186408848
    a6 = 0.360373020
    a14 = 0.0203367881
    a7 = -0.01044324
    a15 = -0.000609579263
    k = a0 + a1*ppr + a2*(ppr**2) + a3*(ppr**3) + tpr*(a4+a5*ppr+a6*(ppr**2)+a7*(ppr**3)) + (tpr**2)*(a8+a9*ppr+a10*(ppr**2)+a11*(ppr**3)) + (tpr**3)*(a12+a13*ppr+a14*(ppr**2)+a15*(ppr**3))
    return mul*exp(k)/tpr
def mug_leege(sg, tres, rhog):
    mw = sg*28.97
    X = 3.5 + 986/tres + 0.01*mw
    Y = 2.4 - 0.2*X
    K = ((tres**1.5)*(9.4+0.02*mw))/(209 + 19*mw + tres)
    M = rhog/62.4 if rhog >= 0 else 0
    return 0.0001*K*exp(X*(pow(M,Y)))

# compressibility (cg)
def Cg(ppr, tpr, z, rhor):
    t1 = 0.31506237 - 1.0467099/tpr - 0.5783272/(tpr**3) if tpr else 0
    t2 = 0.53530771 - 0.61232032/tpr if tpr else 0
    t3 = -0.61232032*-0.10488813/tpr if tpr else 0
    t4 = 0.68157001/(tpr**3) if tpr else 0
    a8 = 0.68446549
    dz = t1 + 2*t2*rhor + 5*t3*(rhor**4) + 2*t4*rhor*(1+a8*(rhor**2)-(a8**2)*(rhor**4))*exp(-a8*(rhor**2))
    return (1/ppr) - (0.27*dz)/((z**2)*tpr*(1+rhor*dz/z)) if (tpr*z) else 0

# Gas Formation Volume Factor (Bg)
def Bg(z, t, p):
    return 0.02827*z*t/p if p else 0
