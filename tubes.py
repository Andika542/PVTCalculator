from tkinter import *
from tkinter import ttk
from tubesgas import *
from oilprop import *
from tubesFRbrine import *
import pandas as pd
import matplotlib.pyplot as plt

# Main windows
root = Tk()
root.title("PVT Calculator")

Label(root, text="PVT CALCULATOR", font=("Comic Sans MS", 30), fg="blue").grid(row=0, column=0, columnspan=9)
Label(root, text="Calculating reservoir fluids properties", font=("Comic Sans MS",18)).grid(row=1, column=0, columnspan=9)
Label(root, text="*For non-commercial use only", font=("Arial", 7)).grid(row=2, column=0, columnspan=9)
Label(root, text="           ").grid(row=3, column=3)

Label(root, text="Please fill these following datas").grid(row=4, column=0)
Label(root, text="Reservoir Data").grid(row=5, column=0, sticky=W)
Label(root, text="Reservoir Temperature (°F)").grid(row=6, column=0, sticky=W)
Label(root, text="Initial Reservoir Pressure (psia)").grid(row=7, column=0, sticky=W)
Label(root, text="Standard Pressure (psia)").grid(row=8, column=0, sticky=W)
Label(root, text="Gas Gravity").grid(row=9, column=0, sticky=W)
Label(root, text="Oil Data").grid(row=5, column=4)
Label(root, text="API").grid(row=6, column=4, sticky=W)
Label(root, text="Bubble Point Pressure (psia)").grid(row=7, column=4, sticky=W)
Label(root, text="Separator Temperature (°F)").grid(row=8, column=4, sticky=W)
Label(root, text="Separator Pressure (psia)").grid(row=9, column=4, sticky=W)
Label(root, text="Impurities (%mole)").grid(row=11, column=0)
Label(root, text="CO2").grid(row=12, column=0, sticky=W)
Label(root, text="N2").grid(row=13, column=0, sticky=W)
Label(root, text="H2S").grid(row=14, column=0, sticky=W)
Label(root, text="Brine Data").grid(row=11, column=4)
Label(root, text="Total Dissolved Solid (%)").grid(row=12, column=4, sticky=W)
Label(root, text="           ").grid(row=6, column=3)
Label(root, text="           ").grid(row=10, column=0)
Label(root, text="           ").grid(row=4, column=6)
Label(root, text="           ").grid(row=15, column=0)

a1 = StringVar()
a2 = StringVar()
a3 = StringVar()
a4 = StringVar()
a5 = StringVar()
a6 = StringVar()
a7 = StringVar()
a8 = StringVar()
a9 = StringVar()
a10 = StringVar()
a11 = StringVar()
a12 = StringVar()
a1.set("0")
a2.set("0")
a3.set("0") 
a4.set("0") 
a5.set("0") 
a6.set("0") 
a7.set("0") 
a8.set("0") 
a9.set("0") 
a10.set("0")
a11.set("0")
a12.set("0")
tres_input = Entry(root, width=15, textvariable=a1)
pres_input = Entry(root, width=15, textvariable=a2)
pstd_input = Entry(root, width=15, textvariable=a3)
sggas_input = Entry(root, width=15, textvariable=a4)
api_input = Entry(root, width=15, textvariable=a5)
pbo_input = Entry(root, width=15, textvariable=a6)
tsep_input = Entry(root, width=15, textvariable=a7)
psep_input = Entry(root, width=15, textvariable=a8)
yco2_input = Entry(root, width=15, textvariable=a9)
yn2_input = Entry(root, width=15, textvariable=a10)
yh2s_input = Entry(root, width=15, textvariable=a11)
tds_input = Entry(root, width=15, textvariable=a12)
tres_input.grid(row=6, column=1)
pres_input.grid(row=7, column=1)
pstd_input.grid(row=8, column=1)
sggas_input.grid(row=9, column=1)
api_input.grid(row=6, column=5)
pbo_input.grid(row=7, column=5)
tsep_input.grid(row=8, column=5)
psep_input.grid(row=9, column=5)
yco2_input.grid(row=12, column=1)
yn2_input.grid(row=13, column=1)
yh2s_input.grid(row=14, column=1)
tds_input.grid(row=12, column=5)

rs_corr = "Standing"
bo_corr = "Standing"
muosat_corr = "Beggs-Robinson"
muoundersat_corr = "Vasquez-Beggs"
pb_corr = "Standing"
bt_corr = "Standing"
co_corr = "Vasquez-Beggs"
z_corr = "Dranchuk-Abou Kassem"
mug_corr = "Lee-Gonzales-Eakin"
cg_corr = "Standing-Katz"
muw_corr = "Standard"
crit_corr = "Standing"
impurities_corr = "Wichert-Aziz"


# Configuration Window
def show_setting_window():
    setting = Toplevel(root)
    setting.title("Configuration")
    Label(setting, text="Choose your correlation").grid(row=0, column=0, columnspan=10)
    Label(setting, text="Oil Properties").grid(row=2, column=0, columnspan=2)
    Label(setting, text="Rs").grid(row=3, column=0, sticky=W)
    Label(setting, text="Bo").grid(row=4, column=0, sticky=W)
    Label(setting, text="Muo saturated").grid(row=5, column=0, sticky=W)
    Label(setting, text="Muo undersaturated").grid(row=6, column=0, sticky=W)
    Label(setting, text="Bubble-Point Pressure").grid(row=7, column=0, sticky=W)
    Label(setting, text="Bt").grid(row=8, column=0, sticky=W)
    Label(setting, text="Co").grid(row=9, column=0, sticky=W)
    Label(setting, text="Gas Properties").grid(row=2, column=3, columnspan=2)
    Label(setting, text="z").grid(row=3, column=3, sticky=W)
    Label(setting, text="Mug").grid(row=4, column=3, sticky=W)
    Label(setting, text="cg").grid(row=5, column=3, sticky=W)
    Label(setting, text="Brine Properties").grid(row=2, column=6, columnspan=2)
    Label(setting, text="Muw").grid(row=3, column=6, sticky=W)
    Label(setting, text="Critical Properties").grid(row=5, column=6, columnspan=2)
    Label(setting, text="P & T critical").grid(row=6, column=6, sticky=W)
    Label(setting, text="Impurities Correction").grid(row=7, column=6, sticky=W)
    Label(setting, text="           ").grid(row=2, column=2)
    Label(setting, text="           ").grid(row=2, column=5)
    Label(setting, text="           ").grid(row=8, column=0)
    Label(setting, text="           ").grid(row=12, column=0)

    rs_box = ttk.Combobox(setting, values=["Standing", "Vasquez-Beggs", "Glaso", "Marhoun", "Petrosky-Farshad"])
    bo_box = ttk.Combobox(setting, values=["Vasquez-Beggs", "Glaso", "Marhoun", "Petrosky-Farshad"])
    muosat_box = ttk.Combobox(setting, values=["Chew-Connally", "Beggs-Robinson"])
    muoundersat_box = ttk.Combobox(setting, values=["Vasquez-Beggs"])
    pb_box = ttk.Combobox(setting, values=["Standing", "Vasquez-Beggs", "Glaso", "Marhoun", "Petrosky-Farshad"])
    bt_box = ttk.Combobox(setting, values=["Standing", "Glaso", "Marhoun"])
    co_box = ttk.Combobox(setting, values=["Vasquez-Beggs", "Petrosky-Farshad"])
    z_box = ttk.Combobox(setting, values=["Hall-Yarborough", "Dranchuk-Abou Kassem"])
    mug_box = ttk.Combobox(setting, values=["Carr-Kobayashi-Burrows", "Lee-Gonzales-Eakin"])
    cg_box = ttk.Combobox(setting, values=["Standing-Katz"])
    muw_box = ttk.Combobox(setting, values=["Standard", "Brill & Beggs"])
    crit_box = ttk.Combobox(setting, values=["Sutton", "Standing"])
    impurities_box = ttk.Combobox(setting, values=["Wichert-Aziz", "Carr-Kobayashi-Burrows"])

    rs_box.grid(row=3, column=1)
    bo_box.grid(row=4, column=1)
    muosat_box.grid(row=5, column=1)
    muoundersat_box.grid(row=6, column=1)
    pb_box.grid(row=7, column=1)
    bt_box.grid(row=8, column=1)
    co_box.grid(row=9, column=1)
    z_box.grid(row=3, column=4)
    mug_box.grid(row=4, column=4)
    cg_box.grid(row=5, column=4)
    muw_box.grid(row=3, column=7)
    crit_box.grid(row=6, column=7)
    impurities_box.grid(row=7, column=7)

    rs_box.current(0)
    bo_box.current(0)
    muosat_box.current(1)
    muoundersat_box.current(0)
    pb_box.current(0)
    bt_box.current(0)
    co_box.current(0)
    z_box.current(1)
    mug_box.current(1)
    cg_box.current(0)
    muw_box.current(0)
    crit_box.current(1)
    impurities_box.current(0)

    # Function to get correlation from configuration window
    def get_correlation():
        global rs_corr
        global bo_corr
        global muosat_corr
        global muoundersat_corr
        global pb_corr
        global bt_corr
        global co_corr
        global z_corr
        global mug_corr
        global cg_corr
        global muw_corr
        global crit_corr
        global impurities_corr
        rs_corr = rs_box.get()
        bo_corr = bo_box.get()
        muosat_corr = muosat_box.get()
        muoundersat_corr = muoundersat_box.get()
        pb_corr = pb_box.get()
        bt_corr = bt_box.get()
        co_corr = co_box.get()
        z_corr = z_box.get()
        mug_corr = mug_box.get()
        cg_corr = cg_box.get()
        muw_corr = muw_box.get()
        crit_corr = crit_box.get()
        impurities_corr = impurities_box.get()
        setting.destroy()

    close_setting_button = Button(setting, text="Close", width=15, height=2)
    close_setting_button["command"] = get_correlation
    close_setting_button.grid(row=10, column=3, columnspan=3, rowspan=2)

    setting.mainloop()

# About Window
def show_about_window():
    about = Toplevel(root)
    about.title("About Us")
    Label(about, text="This simple app is created and designed by :").grid(row=0, column=0)
    Label(about, text="Andika Nurtamin (12218021)").grid(row=1, column=0)
    Label(about, text="M. Afra Dzaki (12218054)").grid(row=2, column=0)
    Label(about, text="Febri Dwi Avianto (12218087)").grid(row=3, column=0)
    Label(about, text="  ").grid(row=4, column=0)

    close_about_button = Button(about, text="Close", command=about.destroy)
    close_about_button.grid(row=5, column=0)

# Calculation Window
def show_calculation():
    calc = Toplevel()
    calc.title("Calculation Results")
    Label(calc, text="Oil Properties").grid(row=2, column=0, columnspan=2)
    Label(calc, text="Rs").grid(row=3, column=0, sticky=W)
    Label(calc, text="Bo").grid(row=4, column=0, sticky=W)
    Label(calc, text="Muo").grid(row=5, column=0, sticky=W)
    Label(calc, text="Oil Density").grid(row=6, column=0, sticky=W)
    Label(calc, text="Bt").grid(row=7, column=0, sticky=W)
    Label(calc, text="Co").grid(row=8, column=0, sticky=W)
    Label(calc, text="Gas Properties").grid(row=2, column=3, columnspan=2)
    Label(calc, text="z").grid(row=3, column=3, sticky=W)
    Label(calc, text="Mug").grid(row=4, column=3, sticky=W)
    Label(calc, text="cg").grid(row=5, column=3, sticky=W)
    Label(calc, text="Gas Density").grid(row=6, column=3, sticky=W)
    Label(calc, text="Bg").grid(row=7, column=3, sticky=W)
    Label(calc, text="Brine Properties").grid(row=2, column=6, columnspan=2)
    Label(calc, text="Rsw").grid(row=3, column=6, sticky=W)
    Label(calc, text="Bw").grid(row=4, column=6, sticky=W)
    Label(calc, text="Muw").grid(row=5, column=6, sticky=W)
    Label(calc, text="cw").grid(row=6, column=6, sticky=W)
    Label(calc, text="Brine Density").grid(row=7, column=6, sticky=W)
    Label(calc, text="              ").grid(row=1, column=2, sticky=W)
    Label(calc, text="              ").grid(row=1, column=5, sticky=W)
    Label(calc, text="              ").grid(row=1, column=8, sticky=W)
    Label(calc, text="              ").grid(row=8, column=3, sticky=W)

    tres = tres_input.get()
    pres = (pres_input.get())
    pstd = (pstd_input.get())
    sggas = (sggas_input.get())
    api = (api_input.get())
    pbo = (pbo_input.get())
    tsep = (tsep_input.get())
    psep = (psep_input.get())
    yco2 = (yco2_input.get())
    yn2 = (yn2_input.get())
    yh2s = (yh2s_input.get())
    tds = (tds_input.get())

    tres = float(tres_input.get()) + 460
    pres = float(pres_input.get())
    sggas = float(sggas_input.get())
    api = float(api_input.get())
    pbo = float(pbo_input.get())
    tsep = float(tsep_input.get()) + 460
    psep = float(psep_input.get())
    yco2 = float(yco2_input.get())/100
    yn2 = float(yn2_input.get())/100
    yh2s = float(yh2s_input.get())/100
    tds = float(tds_input.get())/100

    # Critical Prop.
    if crit_corr == "Sutton":
        ppc = ppc_sutton(sggas)
        tpc = tpc_sutton(sggas)
    else:
        ppc = ppc_standing(sggas)
        tpc = tpc_standing(sggas)

    # Impurities
    if impurities_corr == "Wichert-Aziz":
        ppcx = ppc_corrected_wicherta(ppc, tpc, yn2, yco2, yh2s)
        tpcx = tpc_corrected_wicherta(tpc, yco2, yh2s)
    else:
        ppcx = ppc_corrected_carrkb(ppc, yn2, yco2, yh2s)
        tpcx = tpc_corrected_carrkb(tpc, yn2, yco2, yh2s)

    # Pseudo-reduced
    ppr = Ppr(pres, ppcx)
    tpr = Tpr(tres, tpcx)

    # Gas Z
    if z_corr == "Hall-Yarborough":
        z = z_hally(ppr, tpr)
    else:
        z = z_dak(ppr, tpr)
    print(z)
    # Gas Density
    rhog = densityg(sggas, pres, tres, z)

    # Gas FVF
    bg = Bg(z, tres, pres)

    # Gas Viscosity
    if mug_corr == "Carr-Kobayashi-Burrows":
        mug = mug_carrkb(sggas, yn2, yco2, yh2s, ppr, tpr, tres)
    else:
        mug = mug_leege(sggas, tres, rhog)

    # Gas Compressibility
    if z != 0 or tpr != 0:
        if z_corr == "Hall-Yarborough":
            rhor = (0.06125*ppr*(1/tpr)/z)*exp(-1.2*((1-(1/tpr))**2))
            cg = Cg(ppr, tpr, z, rhor)
        else:
            rhor = 0.27*ppr/(z*tpr) if (z*tpr) else 0
            cg = Cg(ppr, tpr, z, rhor)
    # Oil specific gravity
    sgo = 141.5/(api + 131.5)

    # Bubble point pressure
    pb = pbo

    print(rs_corr)
    # Rs
    if rs_corr == "Standing":
        rs = Rs_Standing(sggas, pres, tres, api)
    elif rs_corr == "Vasquez-Beggs":
        rs = Rs_VasquezBeggs(sggas, pres, api, tres, tsep, psep)
    elif rs_corr == "Glaso":
        rs = Rs_Glaso(api, tres, pres, sggas)
    elif rs_corr == "Marhoun":
        rs = Rs_Marhoun(sggas, sgo, tres, pres)
    elif rs_corr == "Petrosky-Farshad":
        rs = Rs_PetroskyFarshad(pres, sgo, api, tres)
    else:
        rs = 0
    print(rs)

    #Rsb
    if rs_corr == "Standing":
        rsb = Rs_Standing(sggas, pb, tres, api)
    elif rs_corr == "Vasquez-Beggs":
        rsb = Rs_VasquezBeggs(sggas, pb, api, tres, tsep, psep)
    elif rs_corr == "Glaso":
        rsb = Rs_Glaso(api, tres, pb, sggas)
    elif rs_corr == "Marhoun":
        rsb = Rs_Marhoun(sggas, sgo, tres, pb)
    else:
        rsb = Rs_PetroskyFarshad(pb, sgo, api, tres)
    
    if pres > pb:
            rs = rsb
    else:
        pass

    # Oil compressibility (Co)
    if co_corr == "Vasquez-Beggs":
        co = Co_VasquezBeggs(rsb, sggas, api, tsep, psep)
    else:
        co = Co_PetroskyFarshad(rsb, sggas, api, tres, pres)

    # Oil FVF
    if pb_corr == "Vasquez-Beggs":
        bo = Bo_VasquezBeggs(sggas, api, tsep, psep, tres, rs)
        bob = Bo_VasquezBeggs(sggas, api, tsep, psep, tres, rsb)
    elif pb_corr == "Glaso":
        bo = Bo_Glaso(sggas, sgo, tres, rs)
        bob = Bo_Glaso(sggas, sgo, tres, rsb)
    elif pb_corr == "Marhoun":
        bo = Bo_Marhoun(rs, sggas, sgo, tres)
        bob = Bo_Marhoun(rsb, sggas, sgo, tres)
    else:
        bo = Bo_PetroskyFarshad(sggas, sgo, tres, rs)
        bob = Bo_PetroskyFarshad(sggas, sgo, tres, rsb)
    bounder = bo_under(bob, co, pres, pb)
    if pres > pb:
        bo = bounder
    else:
        pass

    # Oil Density
    rhoo = Rho_CrudeOil(rs, sgo, sggas, bo)

    # Total FVF
    if bt_corr == "Standing":
        bt = Bt_Standing(rs, tres, sgo, sggas, pres)
    elif bt_corr == "Glaso":
        bt = Bt_Glaso(rs, tres, sgo, sggas, pres)
    else:
        bt = Bt_Marhoun(rs, sggas, sgo, tres, pres)
    if pres > pb:
        bt = bob
    else:
        pass

    # Oil Viscosity
    mud = Mud_BeggsRobinson(api, tres)
    if muosat_corr == "Chew-Connally":
        muob = Mu_ChewConnally(mud, rs)
    else:
        muob = Mu_BeggsRobinson(mud, rs)
    muo = Mu_VasquezBeggs(muob, pres, pb)
    if pres < pb:
        muo = muob
    else:
        pass

    # Water Solubility
    rsw = Rsw(pres, tres)

    # Bw
    bwf = BwF(pres, tres)
    bws = BwS(pres, tres)
    if pres > pb:
        bw = bwf
    else:
        bw = bws
    
    # Water Viscosity
    if muw_corr == "Standard":
        muw = WVisStd(pres, tres, tds)
    else:
        muw = WVisBB(tres)
    
    # Water Isotherm. Compr.
    cwf = CwF(pres, tres, tds)
    cws = CwS(pres, tres, tds)
    if pres > pb:
        cw = cwf
    else:
        cw = cws

    # Water Density
    rhow = WDensity(tds)
    

    Label(calc, text=str(rs)).grid(row=3, column=1)
    Label(calc, text=str(bo)).grid(row=4, column=1)
    Label(calc, text=str(muo)).grid(row=5, column=1)
    Label(calc, text=str(rhoo)).grid(row=6, column=1)
    Label(calc, text=str(bt)).grid(row=7, column=1)
    Label(calc, text=str(co)).grid(row=8, column=1)
    Label(calc, text=str(z)).grid(row=3, column=4)
    Label(calc, text=str(mug)).grid(row=4, column=4)
    Label(calc, text=str(cg)).grid(row=5, column=4)
    Label(calc, text=str(rhog)).grid(row=6, column=4)
    Label(calc, text=str(bg)).grid(row=7, column=4)
    Label(calc, text=str(rsw)).grid(row=3, column=7)
    Label(calc, text=str(bw)).grid(row=4, column=7)
    Label(calc, text=str(muw)).grid(row=5, column=7)
    Label(calc, text=str(cw)).grid(row=6, column=7)
    Label(calc, text=str(rhow)).grid(row=7, column=7)

    close_calc_button = Button(calc, text="Close", width=20, height=2, command=calc.destroy)
    close_calc_button.grid(row=9, column=3, columnspan=3)

    calc.mainloop()


def show_tabel():
    table = Toplevel()
    cols = ("P", "Rs", "Bo", "Mu oil", "Rho oil", "Bt", "z", "Mu gas", "cg", "Rho gas", "Bg", "Rsw", "Bw", "Mu w", "cw", "Rho w")
    tableBox = ttk.Treeview(table, columns=cols, show="headings")
    for col in cols:
        tableBox.heading(col, text=col)
    tableBox.grid(row=1, column=0)
    tres = tres_input.get()
    pres = (pres_input.get())
    pstd = (pstd_input.get())
    sggas = (sggas_input.get())
    api = (api_input.get())
    pbo = (pbo_input.get())
    tsep = (tsep_input.get())
    psep = (psep_input.get())
    yco2 = (yco2_input.get())
    yn2 = (yn2_input.get())
    yh2s = (yh2s_input.get())
    tds = (tds_input.get())

    tres = float(tres_input.get()) + 460
    pres = float(pres_input.get())
    sggas = float(sggas_input.get())
    api = float(api_input.get())
    pbo = float(pbo_input.get())
    tsep = float(tsep_input.get()) + 460
    psep = float(psep_input.get())
    yco2 = float(yco2_input.get())/100
    yn2 = float(yn2_input.get())/100
    yh2s = float(yh2s_input.get())/100
    tds = float(tds_input.get())/100

     # Oil specific gravity
    sgo = 141.5/(api + 131.5)

    # Bubble-point press
    pb = pbo

    df = pd.DataFrame({"P":[], "Rs":[], "Bo":[], "Mu oil":[], "Rho oil":[], "Bt":[], "z":[], "Mu gas":[], "cg":[], "Rho gas":[], "Bg":[], "Rsw":[], "Bw":[], "Mu w":[], "cw":[], "Rho w":[]})
    lower = int(pb - 150)
    upper = int(pb + 150)
    for i in range(lower, upper, 15):
        pres = i
        if crit_corr == "Sutton":
            ppc = ppc_sutton(sggas)
            tpc = tpc_sutton(sggas)
        else:
            ppc = ppc_standing(sggas)
            tpc = tpc_standing(sggas)

        # Impurities
        if impurities_corr == "Wichert-Aziz":
            ppcx = ppc_corrected_wicherta(ppc, tpc, yn2, yco2, yh2s)
            tpcx = tpc_corrected_wicherta(tpc, yco2, yh2s)
        else:
            ppcx = ppc_corrected_carrkb(ppc, yn2, yco2, yh2s)
            tpcx = tpc_corrected_carrkb(tpc, yn2, yco2, yh2s)

        # Pseudo-reduced
        ppr = Ppr(pres, ppcx)
        tpr = Tpr(tres, tpcx)

        # Gas Z
        if z_corr == "Hall-Yarborough":
            z = z_hally(ppr, tpr)
        else:
            z = z_dak(ppr, tpr)

        # Gas Density
        rhog = densityg(sggas, pres, tres, z)

        # Gas FVF
        bg = Bg(z, tres, pres)

        # Gas Viscosity
        if mug_corr == "Carr-Kobayashi-Burrows":
            mug = mug_carrkb(sggas, yn2, yco2, yh2s, ppr, tpr, tres)
        else:
            mug = mug_leege(sggas, tres, rhog)

        # Gas Compressibility
        if z != 0 or tpr != 0:
            if z_corr == "Hall-Yarborough":
                rhor = (0.06125*ppr*(1/tpr)/z)*exp(-1.2*((1-(1/tpr))**2))
                cg = Cg(ppr, tpr, z, rhor)
            else:
                rhor = 0.27*ppr/(z*tpr) if (z*tpr) else 0
                cg = Cg(ppr, tpr, z, rhor)
        # Oil specific gravity
        sgo = 141.5/(api + 131.5)

        # Rs
        if rs_corr == "Standing":
            rs = Rs_Standing(sggas, pres, tres, api)
        elif rs_corr == "Vasquez-Beggs":
            rs = Rs_VasquezBeggs(sggas, pres, api, tres, tsep, psep)
        elif rs_corr == "Glaso":
            rs = Rs_Glaso(api, tres, pres, sggas)
        elif rs_corr == "Marhoun":
            rs = Rs_Marhoun(sggas, sgo, tres, pres)
        else:
            rs = Rs_PetroskyFarshad(pres, sgo, api, tres)
        
        #Rsb
        if rs_corr == "Standing":
            rsb = Rs_Standing(sggas, pb, tres, api)
        elif rs_corr == "Vasquez-Beggs":
            rsb = Rs_VasquezBeggs(sggas, pb, api, tres, tsep, psep)
        elif rs_corr == "Glaso":
            rsb = Rs_Glaso(api, tres, pb, sggas)
        elif rs_corr == "Marhoun":
            rsb = Rs_Marhoun(sggas, sgo, tres, pb)
        else:
            rsb = Rs_PetroskyFarshad(pb, sgo, api, tres)
        
        if pres > pb:
                rs = rsb
        else:
            pass

        # Oil compressibility (Co)
        if co_corr == "Vasquez-Beggs":
            co = Co_VasquezBeggs(rsb, sggas, api, tsep, psep)
        else:
            co = Co_PetroskyFarshad(rsb, sggas, api, tres, pres)

        # Oil FVF
        if pb_corr == "Vasquez-Beggs":
            bo = Bo_VasquezBeggs(sggas, api, tsep, psep, tres, rs)
            bob = Bo_VasquezBeggs(sggas, api, tsep, psep, tres, rsb)
        elif pb_corr == "Glaso":
            bo = Bo_Glaso(sggas, sgo, tres, rs)
            bob = Bo_Glaso(sggas, sgo, tres, rsb)
        elif pb_corr == "Marhoun":
            bo = Bo_Marhoun(rs, sggas, sgo, tres)
            bob = Bo_Marhoun(rsb, sggas, sgo, tres)
        else:
            bo = Bo_PetroskyFarshad(sggas, sgo, tres, rs)
            bob = Bo_PetroskyFarshad(sggas, sgo, tres, rsb)
        bounder = bo_under(bob, co, pres, pb)
        if pres > pb:
            bo = bounder
        else:
            pass

        # Oil Density
        rhoo = Rho_CrudeOil(rs, sgo, sggas, bo)

        # Total FVF
        if bt_corr == "Standing":
            bt = Bt_Standing(rs, tres, sgo, sggas, pres)
        elif bt_corr == "Glaso":
            bt = Bt_Glaso(rs, tres, sgo, sggas, pres)
        else:
            bt = Bt_Marhoun(rs, sggas, sgo, tres, pres)
        if pres > pb:
            bt = bob
        else:
            pass

        # Oil Viscosity
        mud = Mud_BeggsRobinson(api, tres)
        if muosat_corr == "Chew-Connally":
            muob = Mu_ChewConnally(mud, rs)
        else:
            muob = Mu_BeggsRobinson(mud, rs)
        muo = Mu_VasquezBeggs(muob, pres, pb)
        if pres < pb:
            muo = muob
        else:
            pass

        # Water Solubility
        rsw = Rsw(pres, tres)

        # Bw
        bwf = BwF(pres, tres)
        bws = BwS(pres, tres)
        if pres > pb:
            bw = bwf
        else:
            bw = bws
        
        # Water Viscosity
        if muw_corr == "Standard":
            muw = WVisStd(pres, tres, tds)
        else:
            muw = WVisBB(tres)
        
        # Water Isotherm. Compr.
        cwf = CwF(pres, tres, tds)
        cws = CwS(pres, tres, tds)
        if pres > pb:
            cw = cwf
        else:
            cw = cws

        # Water Density
        rhow = WDensity(tds)
        
        df1 = pd.DataFrame({"P":[i], "Rs":[rs], "Bo":[bo], "Mu oil":[muo], "Rho oil":[rhoo], "Bt":[bt], "z":[z], "Mu gas":[mug], "cg":[cg], "Rho gas":[rhog], "Bg":[bg], "Rsw":[rsw], "Bw":[bw], "Mu w":[muw], "cw":[cw], "Rho w":[rhow]})
        df = df.append(df1, ignore_index=True)
    
        tableBox.insert("", "end", values=(str(i), str(rs), str(bo), str(muo), str(rhoo), str(bt), str(z), str(mug), str(cg), str(rhog), str(bg), str(rsw), str(bw), str(muw), str(cw), str(rhow)))
    
    table.mainloop()


def show_chart_window():
    chart = Toplevel()
    chart.title("Show Chart")

    tres = tres_input.get()
    pres = (pres_input.get())
    pstd = (pstd_input.get())
    sggas = (sggas_input.get())
    api = (api_input.get())
    pbo = (pbo_input.get())
    tsep = (tsep_input.get())
    psep = (psep_input.get())
    yco2 = (yco2_input.get())
    yn2 = (yn2_input.get())
    yh2s = (yh2s_input.get())
    tds = (tds_input.get())

    tres = float(tres_input.get()) + 460
    pres = float(pres_input.get())
    sggas = float(sggas_input.get())
    api = float(api_input.get())
    pbo = float(pbo_input.get())
    tsep = float(tsep_input.get()) + 460
    psep = float(psep_input.get())
    yco2 = float(yco2_input.get())/100
    yn2 = float(yn2_input.get())/100
    yh2s = float(yh2s_input.get())/100
    tds = float(tds_input.get())/100

     # Oil specific gravity
    sgo = 141.5/(api + 131.5)

    # Rs
    pb = pbo

    df = pd.DataFrame({"P":[], "Rs":[], "Bo":[], "Mu oil":[], "Rho oil":[], "Bt":[], "z":[], "Mu gas":[], "cg":[], "Rho gas":[], "Bg":[], "Rsw":[], "Bw":[], "Mu w":[], "cw":[], "Rho w":[]})
    lower = int(pb - 150)
    upper = int(pb + 150)
    for i in range(lower, upper, 15):
        pres = i
        if crit_corr == "Sutton":
            ppc = ppc_sutton(sggas)
            tpc = tpc_sutton(sggas)
        else:
            ppc = ppc_standing(sggas)
            tpc = tpc_standing(sggas)

        # Impurities
        if impurities_corr == "Wichert-Aziz":
            ppcx = ppc_corrected_wicherta(ppc, tpc, yn2, yco2, yh2s)
            tpcx = tpc_corrected_wicherta(tpc, yco2, yh2s)
        else:
            ppcx = ppc_corrected_carrkb(ppc, yn2, yco2, yh2s)
            tpcx = tpc_corrected_carrkb(tpc, yn2, yco2, yh2s)

        # Pseudo-reduced
        ppr = Ppr(pres, ppcx)
        tpr = Tpr(tres, tpcx)

        # Gas Z
        if z_corr == "Hall-Yarborough":
            z = z_hally(ppr, tpr)
        else:
            z = z_dak(ppr, tpr)

        # Gas Density
        rhog = densityg(sggas, pres, tres, z)

        # Gas FVF
        bg = Bg(z, tres, pres)

        # Gas Viscosity
        if mug_corr == "Carr-Kobayashi-Burrows":
            mug = mug_carrkb(sggas, yn2, yco2, yh2s, ppr, tpr, tres)
        else:
            mug = mug_leege(sggas, tres, rhog)

        # Gas Compressibility
        if z != 0 or tpr != 0:
            if z_corr == "Hall-Yarborough":
                rhor = (0.06125*ppr*(1/tpr)/z)*exp(-1.2*((1-(1/tpr))**2))
                cg = Cg(ppr, tpr, z, rhor)
            else:
                rhor = 0.27*ppr/(z*tpr) if (z*tpr) else 0
                cg = Cg(ppr, tpr, z, rhor)
        # Oil specific gravity
        sgo = 141.5/(api + 131.5)

        # Rs
        if rs_corr == "Standing":
            rs = Rs_Standing(sggas, pres, tres, api)
        elif rs_corr == "Vasquez-Beggs":
            rs = Rs_VasquezBeggs(sggas, pres, api, tres, tsep, psep)
        elif rs_corr == "Glaso":
            rs = Rs_Glaso(api, tres, pres, sggas)
        elif rs_corr == "Marhoun":
            rs = Rs_Marhoun(sggas, sgo, tres, pres)
        else:
            rs = Rs_PetroskyFarshad(pres, sgo, api, tres)
        
        #Rsb
        if rs_corr == "Standing":
            rsb = Rs_Standing(sggas, pb, tres, api)
        elif rs_corr == "Vasquez-Beggs":
            rsb = Rs_VasquezBeggs(sggas, pb, api, tres, tsep, psep)
        elif rs_corr == "Glaso":
            rsb = Rs_Glaso(api, tres, pb, sggas)
        elif rs_corr == "Marhoun":
            rsb = Rs_Marhoun(sggas, sgo, tres, pb)
        else:
            rsb = Rs_PetroskyFarshad(pb, sgo, api, tres)

        if pres > pb:
            rs = rsb
        else:
            pass

        # Oil compressibility (Co)
        if co_corr == "Vasquez-Beggs":
            co = Co_VasquezBeggs(rsb, sggas, api, tsep, psep)
        else:
            co = Co_PetroskyFarshad(rsb, sggas, api, tres, pres)

        # Oil FVF
        if pb_corr == "Vasquez-Beggs":
            bo = Bo_VasquezBeggs(sggas, api, tsep, psep, tres, rs)
            bob = Bo_VasquezBeggs(sggas, api, tsep, psep, tres, rsb)
        elif pb_corr == "Glaso":
            bo = Bo_Glaso(sggas, sgo, tres, rs)
            bob = Bo_Glaso(sggas, sgo, tres, rsb)
        elif pb_corr == "Marhoun":
            bo = Bo_Marhoun(rs, sggas, sgo, tres)
            bob = Bo_Marhoun(rsb, sggas, sgo, tres)
        else:
            bo = Bo_PetroskyFarshad(sggas, sgo, tres, rs)
            bob = Bo_PetroskyFarshad(sggas, sgo, tres, rsb)
        bounder = bo_under(bob, co, pres, pb)
        if pres > pb:
            bo = bounder
        else:
            pass

        # Oil Density
        rhoo = Rho_CrudeOil(rs, sgo, sggas, bo)

        # Total FVF
        if bt_corr == "Standing":
            bt = Bt_Standing(rs, tres, sgo, sggas, pres)
        elif bt_corr == "Glaso":
            bt = Bt_Glaso(rs, tres, sgo, sggas, pres)
        else:
            bt = Bt_Marhoun(rs, sggas, sgo, tres, pres)
        if pres > pb:
            bt = bob
        else:
            pass

        # Oil Viscosity
        mud = Mud_BeggsRobinson(api, tres)
        if muosat_corr == "Chew-Connally":
            muob = Mu_ChewConnally(mud, rs)
        else:
            muob = Mu_BeggsRobinson(mud, rs)
        muo = Mu_VasquezBeggs(muob, pres, pb)
        if pres < pb:
            muo = muob
        else:
            pass

        # Water Solubility
        rsw = Rsw(pres, tres)

        # Bw
        bwf = BwF(pres, tres)
        bws = BwS(pres, tres)
        if pres > pb:
            bw = bwf
        else:
            bw = bws
        
        # Water Viscosity
        if muw_corr == "Standard":
            muw = WVisStd(pres, tres, tds)
        else:
            muw = WVisBB(tres)
        
        # Water Isotherm. Compr.
        cwf = CwF(pres, tres, tds)
        cws = CwS(pres, tres, tds)
        if pres > pb:
            cw = cwf
        else:
            cw = cws

        # Water Density
        rhow = WDensity(tds)
        
        df1 = pd.DataFrame({"P":[i], "Rs":[rs], "Bo":[bo], "Mu oil":[muo], "Rho oil":[rhoo], "Bt":[bt], "z":[z], "Mu gas":[mug], "cg":[cg], "Rho gas":[rhog], "Bg":[bg], "Rsw":[rsw], "Bw":[bw], "Mu w":[muw], "cw":[cw], "Rho w":[rhow]})
        df = df.append(df1, ignore_index=True)

    Label(text="Please choose the following properties to be shown as chart :").grid(row=4, column=0)

    g1 = IntVar()
    g2 = IntVar()
    g3 = IntVar()
    g4 = IntVar()
    g5 = IntVar()
    g6 = IntVar()
    g7 = IntVar()
    g8 = IntVar()
    g9 = IntVar()
    g10 = IntVar()
    g11 = IntVar()
    g12 = IntVar()
    g13 = IntVar()
    g14 = IntVar()
    g15 = IntVar()
    rs_check = Checkbutton(chart, text="Rs", variable=g1)
    bo_check = Checkbutton(chart, text="Bo", variable=g2)
    muo_check = Checkbutton(chart, text="Mu oil", variable=g3)
    rhoo_check = Checkbutton(chart, text="Rho oil", variable=g4)
    bt_check = Checkbutton(chart, text="Bt", variable=g5)
    z_check = Checkbutton(chart, text="z", variable=g6)
    mug_check = Checkbutton(chart, text="Mu gas", variable=g7)
    cg_check = Checkbutton(chart, text="Cg", variable=g8)
    rhog_check = Checkbutton(chart, text="Rho gas", variable=g9)
    bg_check = Checkbutton(chart, text="Bg", variable=g10)
    rsw_check = Checkbutton(chart, text="Rsw", variable=g11)
    bw_check = Checkbutton(chart, text="Bw", variable=g12)
    muw_check = Checkbutton(chart, text="Mu w", variable=g13)
    cw_check = Checkbutton(chart, text="Cw", variable=g14)
    rhow_check = Checkbutton(chart, text="Rho w", variable=g15)
    rs_check.grid(row=7, column=0, sticky=W)
    bo_check.grid(row=8, column=0, sticky=W)
    muo_check.grid(row=9, column=0, sticky=W)
    rhoo_check.grid(row=10, column=0, sticky=W)
    bt_check.grid(row=11, column=0, sticky=W)
    z_check.grid(row=7, column=1, sticky=W)
    mug_check.grid(row=8, column=1, sticky=W)
    cg_check.grid(row=9, column=1, sticky=W)
    rhog_check.grid(row=10, column=1, sticky=W)
    bg_check.grid(row=11, column=1, sticky=W)
    rsw_check.grid(row=7, column=2, sticky=W)
    bw_check.grid(row=8, column=2, sticky=W)
    muw_check.grid(row=9, column=2, sticky=W)
    cw_check.grid(row=10, column=2, sticky=W)
    rhow_check.grid(row=11, column=2, sticky=W)

    def get_chart():
        if g1.get() == 1:
            df.plot(kind="line", y="Rs", x="P")
            plt.show()
        if g2.get() == 1:
            df.plot(kind="line", y="Bo", x="P")
            plt.show()
        if g3.get() == 1:
            df.plot(kind="line", y="Mu oil", x="P")
            plt.show()
        if g4.get() == 1:
            df.plot(kind="line", y="Rho oil", x="P")
            plt.show()
        if g5.get() == 1:
            df.plot(kind="line", y="Bt", x="P")
            plt.show()
        if g6.get() == 1:
            df.plot(kind="line", y="z", x="P")
            plt.show()
        if g7.get() == 1:
            df.plot(kind="line", y="Mu gas", x="P")
            plt.show()
        if g8.get() == 1:
            df.plot(kind="line", y="cg", x="P")
            plt.show()
        if g9.get() == 1:
            df.plot(kind="line", y="Rho gas", x="P")
            plt.show()
        if g10.get() == 1:
            df.plot(kind="line", y="Bg", x="P")
            plt.show()
        if g11.get() == 1:
            df.plot(kind="line", y="Rsw", x="P")
            plt.show()
        if g12.get() == 1:
            df.plot(kind="line", y="Bw", x="P")
            plt.show()
        if g13.get() == 1:
            df.plot(kind="line", y="Mu w", x="P")
            plt.show()
        if g14.get() == 1:
            df.plot(kind="line", y="Cw", x="P")
            plt.show()
        if g15.get() == 1:
            df.plot(kind="line", y="Rho w", x="P")
            plt.show()

    show_chartButton = Button(chart, text="Show", command=get_chart, width=25)
    show_chartButton.grid(row=14, column=1, columnspan=3)

hitungButton = Button(root, text="Calculate", width=15, height=2, command=show_calculation)
settingButton = Button(root, text="Configuration", width=15, height=2, command=show_setting_window)
tabelButton = Button(root, text="Show Table", width=15, height=2, command=show_tabel)
chartButton = Button(root, text="Show Chart", width=15, height=2, command=show_chart_window)
aboutButton = Button(root, text="About", width=15, height=2, command=show_about_window)
hitungButton.grid(row=4, column=7, rowspan=2, columnspan=2)
settingButton.grid(row=6, column=7, rowspan=2, columnspan=2)
tabelButton.grid(row=8, column=7, rowspan=2, columnspan=2)
chartButton.grid(row=10, column=7, rowspan=2, columnspan=2)
aboutButton.grid(row=12, column=7, rowspan=2, columnspan=2)


root.mainloop()