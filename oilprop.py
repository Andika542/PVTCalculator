from math import pow, exp, log10, log

#Gas Solubility

def Rs_Standing(Sgg, P, T, api):
    x = (0.0125*api)-(0.00091*(T-460))
    x1 = pow(10, x)
    x2 = ((P/18.2)+1.4)*x1
    x3 = pow(x2, 1.2048) if x2 >= 0 else 0
    Rs = Sgg*x3/1000
    return(Rs)

def Rs_VasquezBeggs(Sgg, P, api, T, Tsep, Psep):
    Sggs = Sgg*(1+(5.912*0.00001*api*(Tsep-460)*(log10(Psep/114.7))))
    if api <= 30:
       x = 25.7240*(api/T)
       x1 = exp(x)
       x2 = pow(P, 1.0937) if P >= 0 else 0
       Rs = 0.0362*Sggs*x2*x1
    elif api > 30:
       x = 23.931*(api/T)
       x1 = exp(x)
       x2 = pow(P, 1.1870) if P >= 0 else 0
       Rs = 0.0178*Sggs*x2*x1/1000
    return(Rs)

def Rs_Glaso(api, T, P, Sgg): #Masih Dalam Development
    x1 = (14.1811 - (3.3093*(log10(P))))
    x2 = pow(x1, 0.5)
    x = 2.8869- x2
    Pb = pow(10, x)
    y1 = pow(api, 0.989)
    y2 = pow((T-460), 0.172) 
    y3 = (y1/y2)*Pb
    y4 = pow(y3, 1.2255)
    Rs = Sgg*y4/1000
    return(Rs)

def Rs_Marhoun(Sgg, Sgo, T, P):
    x1 = pow(Sgg, 1.877840)
    x2 = pow(Sgo, -3.1437)
    x3 = pow(T, -1.32657)
    x4 = 185.843208*x1*x2*x3*P
    Rs1 = pow(x4, 1.398441)
    Rs = Rs1/1000
    return(Rs)

def Rs_PetroskyFarshad(P, Sgo, api, T):
    x = 7.916*0.0001*(pow(api, 1.541))-(4.561*0.00001*(pow((T-460), 1.3911)))
    x1 = pow(Sgo, 0.8439)
    x2 = pow(10, x)
    x3 = ((P/112.27)+12.34)*x1*x2
    Rs1 = pow(x3, 1.73184)
    Rs = Rs1/1000
    return(Rs)

#Bubble Point Pressure

def Pb_Standing(Rs, Sgg, T, api):
    a = (0.00091*(T-460)) - (0.0125*api)
    x1 = Rs/Sgg if Sgg else 0
    x2 = pow(x1, 0.83)
    x3 = pow(10, a)
    Pb = 18.2*((x2*x3)-1.4)
    return(Pb)

def Pb_VasquezBeggs(Rs, Sgg, api, Tsep, Psep, T):
    Sggs = Sgg*(1+(5.912*0.00001*api*(Tsep-460)*(log10(Psep/114.7))))
    if api <= 30:
       a = -11.172*api/T
       x1 = pow(10, a)
       x2 = (27.624*Rs/Sggs)*x1 if Sggs else 0
       Pb = pow(x2, 0.914328)
    elif api > 30:
       a = -10.393*api/T
       x1 = pow(10, a)
       x2 = (56.18*Rs/Sggs)*x1 if Sggs else 0
       Pb = pow(x2, 0.84246)
    return(Pb)

def Pb_Glaso(Rs, Sgg, T, api):
    x1 = Rs/Sgg
    x2 = pow(x1, 0.816) if x1 >= 0 else 0
    x3 = pow(T, 0.172)
    x4 = pow(api, -0.989) if api >=0 else 0
    Pbs = x2*x3*x4
    lgPb = 1.7669+(1.7447*(log10(Pbs)))-(0.30218*(log10(Pbs))*(log10(Pbs))) if Pbs > 0 else 0
    Pb= pow(10, lgPb)
    return(Pb)

def Pb_Marhoun(Rs, Sgg, Sgo, T):
    x1 = pow(Rs, 0.715082)
    x2 = pow(Sgg, -1.87784)
    x3 = pow(Sgo, 3.1437)
    x4 = pow(T, 1.32657)
    Pb = 5.38088*0.001*x1*x2*x3*x4
    return(Pb)

def Pb_PetroskyFarshad(Rs, Sgg, api, T):
    x = 7.916*0.0001*(pow(api, 1.541))-(4.561*0.00001*(pow((T-460), 1.3911)))
    x1 = pow(Rs, 0.577421)
    x2 = pow(Sgg,0.8439)
    x3 = pow(10, x)
    Pb = ((112.727*x1)/(x2*x3))-1391.051
    return(Pb)

#Oil FVF

#def Bo_Standing(Rs, Sgg, Sgo, T):
    #x = Sgg/Sgo 
    #x1 = pow(x, 0.5)
    #x2 = (Rs*x1)+(1.25*(T-460))
    #x3 = pow(x2, 1.2)
    #Bo = 0.9759 + (0.000120*x3)
    #return(x2)

def Bo_VasquezBeggs(Sgg, api, Tsep, Psep, T, Rs):
    Sggs = Sgg*(1+(5.912*0.00001*api*(Tsep-460)*(log10(Psep/114.7)))) 
    if api <= 30:
       Bo = 1+(4.677*0.0001*Rs*1000)+((T-520)*(api/Sggs)*((1.751*0.00001)+(-1.811*0.00000001*Rs*1000)))
    elif api > 30:
       Bo = 1+(4.670*0.0001*Rs*1000)+((T-520)*(api/Sggs)*((1.1*0.00001)+(1.337*0.000000001*Rs*1000)))
    return(Bo)

def Bo_Glaso(Sgg, Sgo, T, Rs):
    x = Sgg/Sgo
    x1 = pow(x, 0.526)
    Bob = (Rs*x1) + (0.968*(T-460))
    A = -6.58511+(2.91329*(log10(Bob)))-(0.27683*(log10(Bob))*(log10(Bob)))
    Bo = 1 + (pow(10, A))
    return(Bo)

def Bo_Marhoun(Rs, Sgg, Sgo, T):
    x1 = pow(Rs, 0.742390)
    x2 = pow(Sgg, 0.323294)
    x3 = pow(Sgo, -1.202040)
    F = x1*x2*x3
    Bo = 0.497069 + (0.862963*0.001*T) + (0.182594*0.01*F) + (0.318099*0.00001*F*F)
    return(Bo)

def Bo_PetroskyFarshad(Sgg, Sgo, T, Rs):
    x1 = pow(Rs, 0.3738)
    x2 = pow(Sgg, 0.2914)
    x3 = pow(Sgo, 0.6265)
    x4 = pow((T-460), 0.5371)
    x5 = (x1*(x2/x3))+(0.24626*x4)
    x6 = pow(x5, 3.0936)
    Bo = 1.0113+(7.2046*0.00001*x6)
    return(Bo)

#Isothermal Compressibility Coefficient

def Co_VasquezBeggs(Rsb, Sgg, api, Tsep, Psep):
    Sggs = Sgg*(1+(5.912*0.00001*api*(Tsep-460)*(log10(Psep/114.7)))) if Psep > 0 else 0
    Co = (-1.433+(5*Rsb)+(17.2*(Tsep-460))-(1.18*Sggs)+(12.61*api))/(10*10*10*10*10*Psep) if Psep else 0
    return(Co)

def Co_PetroskyFarshad(Rsb, Sgg, api, T, P):
    x1 = pow(Rsb, 0.69357)
    x2 = pow(Sgg, 0.1885)
    x3 = pow(api, 0.3272)
    x4 = pow((T-460), 0.6729)
    if P == 0:
        P += 0.001
    x5 = pow(P, -0.5906)
    Co = 1.705*0.0000001*x1*x2*x3*x4*x5
    return(Co)

#def counder_VB(rsb, sgg, t, api, p):
 #   q = -1433 + 5*rsb + 17.2*t - 1180*sgg + 1251*api

#Oil FVF Undersaturated

def Bo_Undersaturated(Rs, Rsb, Sgg, Sgo, api, T, P, Pb):
    e = 2.718281828459045235360287471352
    x = Sgg/Sgo
    x1 = pow(x, 0.526)
    Bob = (Rs*x1) + (0.968*(T-460))
    x2 = pow(Rsb, 0.69357)
    x3 = pow(Sgg, 0.1885)
    x4 = pow(api, 0.3272)
    x5 = pow((T-460), 0.6729)
    A = 4.1646*0.0000001*x2*x3*x4*x5
    x6 = -A*(pow(P,0.4094)) if P >= 0 else 0
    x7 = pow(Pb, 0.4094) if Pb >= 0 else 0
    x8 = x6-x7
    Bo = Bob*(pow(e, x8))
    return(Bo)

def bo_under(bob, co, p, pb):
    return bob*exp(-co*(p-pb))

#Crude Oil Density

def Rho_CrudeOil(Rs, Sgo, Sgg, Bo):
    if Bo == 0:
        Bo += 0.000001
    Rho = ((62.4*Sgo)+(0.0136*Rs*Sgg))/Bo
    return(Rho)

#Total FVF

def Bt_Standing(Rs, T, Sgo, Sgg, P):
    x = -0.00027*Rs
    C = 2.9*(pow(10, x))
    x1 = (((pow((T-460), 0.5))*(pow(Sgo, C)))/(pow(Sgg, 0.3)))*Rs if ((pow(Sgg, 0.3))*Rs) else 0
    if P > 0:
        x2 = 10.1-(9.68/(6.604+(log10(P)))) 
        if x1 > 0:
            x3 = (log10(x1))-x2
            A = pow(10, x3)
            if A > 0:
                y = -5.223-(47.4/(-12.22+(log10(A))))
                Bt = pow(10, y)
                return(Bt)
    
def Bt_Glaso(Rs, T, Sgo, Sgg, P):
    x = -0.00027*Rs
    C = 2.9*(pow(10, x))
    x1 = pow((T-460), 0.5) if T-460 > 0 else 0
    x2 = pow(Sgo, C) if Sgo >= 0 else 0
    x3 = pow(Sgg, 0.3) if Sgg >= 0 else 0
    x4 = pow(P, -1.1089) if P >= 0 else 0
    A = ((Rs*x1*x2)/x3)*x4
    y = 0.080135+(0.47257*(log10(A)))+(0.17351*(log10(A))*(log10(A))) if A else 0
    Bt = pow(10, y)
    return(Bt)

def Bt_Marhoun(Rs, Sgg, Sgo, T, P):
    x1 = pow(Rs, 0.644516) if Rs >= 0 else 0
    x2 = pow(Sgg, -1.079340) if Sgg >= 0 else 0
    x3 = pow(Sgo, 0.724874) if Sgo >=0 else 0
    x4 = pow(T, 2.006210) if T >= 0 else 0
    x5 = pow(P, -0.761910) if P >= 0 else 0
    F = x1*x2*x3*x4*x5
    Bt = 0.314693+(0.106253*0.0001*F)+(0.18883*0.0000000001*F*F)
    return(Bt)

#Crude Oil Viscosity

#Dead Oil
#def Mu_Beal(api, T):
#    x = 0.43+(8.33/api)
 #   a = pow(10, x)
 #   x1 = 0.32+((1.8*10000000)/(pow(api, 4.53)))
 #   x2 = (360/(T-260))
  #  x3 = pow(x2, a)
   # Mu = x1*x3
    #return(Mu)

def Mud_BeggsRobinson(api, T):
    Z = 3.0324 - (0.02023*api)
    Y = pow(10, Z)
    X = Y*(pow((T-460),-1.163)) if (T-460) else 0
    Mu = (pow(10, X)) - 1
    return(Mu)

#def Mu_Glaso(api, T):
 #   a = (10.313*(log10(T-460)))-36.447
  #  x = log10(api)
   # x1 = pow(x, a)
    #Mu = (3.141*10000000000)*(pow((T-460), -3.444))*x1
    #return(Mu)

#Saturated Oil
def Mu_ChewConnally(Mud, Rs):
    c = 8.62*0.00001*Rs
    d = 1.1*0.001*Rs
    e = 3.74*0.001*Rs
    b = (0.68/(pow(10, c))) + (0.25/(pow(10, d))) + (0.062/(pow(10, e)))
    a = Rs*((2.2*0.0000001*Rs)-(7.4*0.0001))
    Mub = (pow(10, a))*(pow(Mud, b))
    return(Mub)

def Mu_BeggsRobinson(Mud, Rs):
    x1 = pow((Rs+100), -0.515)
    x2 = pow((Rs+150), -0.338)
    a = 10.715*x1
    b = 5.44*x2
    Mub = a*(pow(Mud, b))
    return(Mub)

#Undersaturated Oil
def Mu_VasquezBeggs(Mub, P, Pb):
    a = (-3.9*0.00001*P)-5
    m = 2.6*(pow(P, 1.187))*(pow(10, a)) if P >= 0 else 0
    x = (P/Pb) if Pb else 0
    Mu = Mub*(pow(x, m)) if x >= 0 else 0
    return(Mu)
    