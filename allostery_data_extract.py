#This code extracts data from the spread sheet and calculates strains. Data is saved as a pickle file.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

def compute_strain(dat):
    int_source=dat[1]
    int_target=dat[2]
    fin_source=dat[3]
    fin_target=dat[4]

    source_strain=(fin_source-int_source)/(int_source)
    target_strain=(fin_target-int_target)/(int_target)
    return source_strain, target_strain
def strain_extract(cols,px,nd_dist):
    source_strains=[]
    target_strains=[]
    data=pd.read_excel(r'/home/savannah/Documents/allostery_data_9_10.ods','Sheet1',usecols=cols)
    #convert correct source values to account for screw
    if len(px)==1:
        px=px[0]
        true_dist=nd_dist*px
        df=data[1:6].to_numpy()
        m_source=df[1]
        correction=true_dist-m_source
        df[1]=np.add(df[1],correction)
        df[3]=np.add(df[3],correction)
    else:
        px=np.array(px)
        true_dist=px*nd_dist
        true_dist=np.repeat(true_dist,3)
        df=data[1:6].to_numpy()
        m_source=df[1]
        correction=true_dist-m_source
        df[1]=np.add(df[1],correction)
        df[3]=np.add(df[3],correction)

    #get indices fro different measuring strains
    ind_25=np.where(df==0.25)[1]
    ind_50=np.where(df==0.50)[1]
    ind_75=np.where(df==0.75)[1]
    #extract data for each
    dat_25=df[:,ind_25]
    dat_50=df[:,ind_50]
    dat_75=df[:,ind_75]
    #compute strain ratios for each
    s_25,t_25=compute_strain(dat_25)
    s_50,t_50=compute_strain(dat_50)
    s_75,t_75=compute_strain(dat_75)

    source_strains.append([s_25,s_50,s_75])
    target_strains.append([t_25,t_50,t_75])
    return source_strains,target_strains



netDict = {
# initially coupled data
"durian_a":{"cols":"C:K","pixToCM":[351],"nodeDist":1.5,"timeStamps":[0,24,120]}, #static
"durian_b":{"cols":"L:T","pixToCM":[351],"nodeDist":1.5,"timeStamps":[0,24,120]}, #cyclic
"durian_c":{"cols":"U:AC","pixToCM":[351],"nodeDist":1.5,"timeStamps":[0,24,120]}, #double cyclic
"durian_d":{"cols":"FW:GH","pixToCM":[359,355,355,359],"nodeDist":1.5,"timeStamps":[0,24,48,168]}, #copy of above static

"banana_a":{"cols":"AE:AY","pixToCM":[351,351,351,351,351,356,356],"nodeDist":2.8,"timeStamps":[0,2,4,6,24,48,72]}, #static
"banana_b":{"cols":"AZ:BT","pixToCM":[351,351,351,351,351,356,356],"nodeDist":2.8,"timeStamps":[0,2,4,6,24,48,72]}, #double cyclic
"banana_c":{"cols":"BU:CO","pixToCM":[351,351,351,351,351,356,356],"nodeDist":2.8,"timeStamps":[0,2,4,6,24,48,72]}, #cyclic
"banana_d":{"cols":"KF:KT","pixToCM":[364,364,349,349,349],"nodeDist":1.8,"timeStamps":[0,24,48,72,96]}, #out of phase

"square_a":{"cols":"CP:DJ","pixToCM":[351,351,351,351,356,356,356],"nodeDist":1.9,"timeStamps":[0,2,4,6,24,48,72]}, #static
"square_b":{"cols":"DK:EE","pixToCM":[351,351,351,351,356,356,356],"nodeDist":1.9,"timeStamps":[0,2,4,6,24,48,72]}, # cyclic
"square_c":{"cols":"EF:EZ","pixToCM":[351,351,351,351,351,356,356],"nodeDist":1.9,"timeStamps":[0,2,4,6,24,48,72]}, #double cyclic
"square_d":{"cols":"GI:GT","pixToCM":[359,354,355,355],"nodeDist":1.65,"timeStamps":[0,24,48,168]},#new source target par from previous
"square_e":{"cols":"KU:LI","pixToCM":[364,364,349,349,349],"nodeDist":1.3,"timeStamps":[0,24,48,72,96]}, #new coupled pair

"square2_a":{"cols":"GU:HF","pixToCM":[359],"nodeDist":3,"timeStamps":[0,24,48,168]}, #didn't work well
"square2_f":{"cols":"JB:JP","pixToCM":[364,364,349,349,349],"nodeDist":3,"timeStamps":[0,24,48,72,96]},#duplicate of A
"square2_b":{"cols":"HH:HM","pixToCM":[355,362],"nodeDist":2,"timeStamps":[0,432]},
"square2_g":{"cols":"JQ:KE","pixToCM":[364,364,349,349,349],"nodeDist":2,"timeStamps":[0,24,48,72,96]},#duplicate of b


"apple_c":{"cols":"HH:HM","pixToCM":[364],"nodeDist":2.8,"timeStamps":[0,432]},
"apple_e":{"cols":"LJ:LX","pixToCM":[364,364,349,349,349],"nodeDist":2,"timeStamps":[0,24,48,72,96]}, #new coupled pair
"apple_g":{"cols":"AAL:AAW","pixToCM":[362],"nodeDist":2.5,"timeStamps":[0,24,49,72]}, #another new_target

# initially uncoupled data
"apple_a":{"cols":"FB:FJ","pixToCM":[359,357,358],"nodeDist":2.6,"timeStamps":[0,24,48]}, #cyclic
"apple_b":{"cols":"FK:FV","pixToCM":[359,356,358,357],"nodeDist":2.6,"timeStamps":[0,24,48,168]}, #static
"apple_d":{"cols":"HZ:IE","pixToCM":[364],"nodeDist":2.4,"timeStamps":[0,432]}, #new target further away
"apple_f":{"cols":"UE:US","pixToCM":[362],"nodeDist":2.4,"timeStamps":[0,17,24,48,96]}, #same target as a, out of phase

"apple_h":{"cols":"AAX:ACA","pixToCM":[362,362,362,362,374,378,373,389,391,390],"nodeDist":2.4,"timeStamps":[0,24,49,72,120,168,240,264,288,648]}, #another new_target
"apple_i":{"cols":"AEA:AEL","pixToCM":[373,390,406,388],"nodeDist":2.7,"timeStamps":[0,6,23,30]}, #another new_target
"apple_k":{"cols":"AEM:AEX","pixToCM":[373,390,406,388],"nodeDist":2.7,"timeStamps":[0,6,23,30]}, #another new_target
"apple_j":{"cols":"AEY:AFJ","pixToCM":[373,390,406,388],"nodeDist":2.7,"timeStamps":[0,6,23,30]}, #another new_target
"apple_l":{"cols":"AFK:AFV","pixToCM":[373,390,406,388],"nodeDist":2.7,"timeStamps":[0,6,23,30]}, #another new_target


"durian_e":{"cols":"HT:HY","pixToCM":[359,362],"nodeDist":2,"timeStamps":[0,432]},
"durian_f":{"cols":"LY:MS","pixToCM":[364,364,349,349,362,364,364],"nodeDist":2,"timeStamps":[0,24,48,72,111,120,192]},#duplicate of e, static
"durian_g":{"cols":"MT:MY","pixToCM":[364],"nodeDist":2,"timeStamps":[0,192]},#duplicate, static, but only measured twice
"durian_h":{"cols":"MZ:NK","pixToCM":[364,364,349,349],"nodeDist":2,"timeStamps":[0,24,48,72]},#cyclic

"square2_c":{"cols":"IF:IK","pixToCM":[364],"nodeDist":3,"timeStamps":[0,432]},
"square2_d":{"cols":"IL:IQ","pixToCM":[364],"nodeDist":3,"timeStamps":[0,432]}, #same source as c but further target
"square2_e":{"cols":"IR:IW","pixToCM":[364],"nodeDist":2.2,"timeStamps":[0,432]}, #diff src target, didn't work that well
"square2_h":{"cols":"NL:NW","pixToCM":[364,364,349,349],"nodeDist":3,"timeStamps":[0,24,48,72]}, #same source as c and d, new target nothing happens
"square2_i":{"cols":"ZY:AAK","pixToCM":[362],"nodeDist":2.8,"timeStamps":[0,24,49,72]}, #duplicate square2_d with repeater
"square2_j":{"cols":"ACB:ACJ","pixToCM":[370,390,390],"nodeDist":2.8,"timeStamps":[0,24,48]}, #duplicate square2_d with a different repeater
"square2_k":{"cols":"ACK:ACS","pixToCM":[370,390,390],"nodeDist":2.8,"timeStamps":[0,24,48]}, #duplicate square2_d with 2 repeaters


"banana_e":{"cols":"NX:OI","pixToCM":[364,364,349,349],"nodeDist":1.7,"timeStamps":[0,24,48,72]}, #no response

"square_f":{"cols":"OJ:OX","pixToCM":[364,364,349,349,349],"nodeDist":1.5,"timeStamps":[0,24,48,72,96]}, #
"square_g":{"cols":"OZ:PN","pixToCM":[364,362,362,363,362],"nodeDist":1.5,"timeStamps":[0,17,24,48,96]}, #duplicate f
"square_h":{"cols":"PO:QC","pixToCM":[364,362,362,363,362],"nodeDist":1.5,"timeStamps":[0,17,24,48,96]}, #cyclic version
"square_i":{"cols":"QD:QR","pixToCM":[364,362,362,362,362],"nodeDist":1.5,"timeStamps":[0,17,24,48,96]}, #new_target
"square_j":{"cols":"QS:RG","pixToCM":[364,362,362,362,362],"nodeDist":1.5,"timeStamps":[0,17,24,48,96]}, #another new_target
"square_k":{"cols":"RH:RV","pixToCM":[364,362,362,362,362],"nodeDist":1.6,"timeStamps":[0,17,24,48,96]}, #another new_target
"square_l":{"cols":"XF:XQ","pixToCM":[362],"nodeDist":1.5,"timeStamps":[0,24,49,72]}, #another new_target
"square_m":{"cols":"XR:YU","pixToCM":[362,362,362,362,374,380,374,393,389,389],"nodeDist":1.5,"timeStamps":[0,24,49,72,120,168,240,264,288,648]}, #another new_target
"square_n":{"cols":"YV:ZY","pixToCM":[362,362,362,362,377,377,374,389,394,389],"nodeDist":1.5,"timeStamps":[0,24,49,72,120,168,240,264,288,648]}, #another new_target
"square_o":{"cols":"ACT:ADB","pixToCM":[370,389,390],"nodeDist":1.5,"timeStamps":[0,24,48]}, #duplicate square2_d with 2 repeaters
"square_p":{"cols":"ADC:ADN","pixToCM":[372,390,390,390],"nodeDist":1.5,"timeStamps":[0,24,48,408]}, #duplicate square2_d with 2 repeaters
"square_q":{"cols":"AFX:AGI","pixToCM":[388,365,365,365],"nodeDist":1.5,"timeStamps":[0,18,24,72]}, #copy square_f strain dependence
"square_r":{"cols":"AGJ:AGU","pixToCM":[388,365,365,365],"nodeDist":1.5,"timeStamps":[0,18,24,72]}, #copy square_f strain dependence
"square_s":{"cols":"AGV:AHG","pixToCM":[388,365,365,365],"nodeDist":1.5,"timeStamps":[0,18,24,72]}, #copy square_f strain dependence

"square3_a":{"cols":"RW:SK","pixToCM":[364,362,362,362,362],"nodeDist":1.3,"timeStamps":[0,17,24,48,96]},
"square3_b":{"cols":"SL:SZ","pixToCM":[364,362,362,362,362],"nodeDist":1.3,"timeStamps":[0,17,24,48,96]}, #out of phase

"fig_a":{"cols":"TA:TO","pixToCM":[363,362,362,362,362],"nodeDist":1.2,"timeStamps":[0,17,24,48,96]},
"fig_b":{"cols":"TP:UD","pixToCM":[362],"nodeDist":1.2,"timeStamps":[0,17,24,48,96]}, #out of phase
"fig_c":{"cols":"UU:VL","pixToCM":[362,362,362,362,370,372],"nodeDist":1.1,"timeStamps":[0,24,49,72,168,240]},
"fig_d":{"cols":"VM:WD","pixToCM":[362,362,362,362,380,376],"nodeDist":1.1,"timeStamps":[0,24,49,72,168,240]},
"fig_e":{"cols":"WE:WS","pixToCM":[362,362,362,362,380],"nodeDist":1.1,"timeStamps":[0,24,49,72,168]},
"fig_f":{"cols":"WT:XE","pixToCM":[362],"nodeDist":1.2,"timeStamps":[0,24,49,72]},
"fig_g":{"cols":"ADO:ADZ","pixToCM":[376,388,404,391],"nodeDist":1.2,"timeStamps":[0,6,23,30]},
"fig_h":{"cols":"AHH:AHS","pixToCM":[388,365,365,365],"nodeDist":1.2,"timeStamps":[0,18,24,72]},#copy d strain dependence
"fig_i":{"cols":"AHT:AIE","pixToCM":[388,365,365,365],"nodeDist":1.2,"timeStamps":[0,18,24,72]},#copy d strain dependence
"fig_j":{"cols":"AIF:AIQ","pixToCM":[388,365,365,365],"nodeDist":1.2,"timeStamps":[0,18,24,72]},#copy d strain dependence
"fig_k":{"cols":"AIR:AJC","pixToCM":[388,365,365,365],"nodeDist":1.2,"timeStamps":[0,18,24,72]},#copy g with 1 repeater
"fig_l":{"cols":"AJD:AJO","pixToCM":[388,365,365,365],"nodeDist":1.2,"timeStamps":[0,18,24,72]},#copy e with 2 repeater
"fig_m":{"cols":"AJP:AKA","pixToCM":[388,365,365,365],"nodeDist":1.2,"timeStamps":[0,18,24,72]},#copy e with 3 repeater
"fig_n":{"cols":"AKB:AKM","pixToCM":[388,365,365,365],"nodeDist":1.1,"timeStamps":[0,18,24,72]}, #copy e with 1 repeater
"fig_o":{"cols":"AKN:AKY","pixToCM":[388,365,365,365],"nodeDist":1.1,"timeStamps":[0,18,24,72]},#copy e with 2 repeater
"fig_p":{"cols":"AKZ:ALK","pixToCM":[388,365,365,365],"nodeDist":1.1,"timeStamps":[0,18,24,72]}, #copy e with 3 repeater


}
strainDict = {}

for sample, detail in netDict.items():
    print(sample)
    cols = detail["cols"]
    pixToCM = detail["pixToCM"]
    nodeDist = detail["nodeDist"]
    src,trg=strain_extract(cols,pixToCM,nodeDist)
    src=src[0]
    trg=trg[0]
    strainDict[sample] = {"sE":src,"tE":trg,"time":detail["timeStamps"]}

    #plotting just to verfiy
    # s_25=src[0]
    # s_50=src[1]
    # s_75=src[2]
    #
    # t_25=trg[0]
    # t_50=trg[1]
    # t_75=trg[2]
    #
    # colors=['pink','red','maroon','black','yellow','purple','green','blue']
    # markers=['o','X','s','^','*']
    # lables=['original','1 day','5 days']
    # for i in range (len(s_25)):
    #     c=colors[i]
    #     # m=markers[i]
    #     # l=lables[i]
    #     plt.scatter(abs(s_25[i]),abs(t_25[i]),color=c)
    #     plt.scatter(abs(s_50[i]),abs(t_50[i]),color=c)
    #     plt.scatter(abs(s_75[i]),abs(t_75[i]),color=c)
    # # plt.legend()
    # # plt.xlim(0,.75)
    # # plt.ylim(-.01,.25)
    # plt.show()

#
outputPath ='/home/savannah/Desktop/Savannah/allostery_code_data/'
with open(f"{outputPath}/strainDict.pkl","wb") as f:
    pickle.dump(strainDict,f,protocol=pickle.HIGHEST_PROTOCOL)
