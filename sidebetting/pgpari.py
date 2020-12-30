from numpy.random import rand

import numpy as np

nb_step_mart=3

def refresh_martingale(palier,cote):

    martingale=[palier]
    for i in range(nb_step_mart):
        palier=palier*(cote)/(cote-1)
        martingale.append(palier)
    # print("redefined martingale",martingale)
    return martingale

mean_br=[]
bankrupt=0
for i in range(3000):

    bankroll = 200
    cotebroker=1.2
    marge=0.05
    pourgain=(1/cotebroker)*((100-marge)/100)
    cotereelle=1/pourgain

    palier = 7 * (bankroll / 200)

    martingale=refresh_martingale(palier,cotereelle)
    step_martingale=0


    problem=0

    for i in range(30):
        if bankroll-martingale[step_martingale]<0:
            print("BANKRUPT")
            bankrupt += 1
            break

        bankroll-=martingale[step_martingale]
        result=rand(1)[0]<(1/cotereelle)+0.05
        # print(result)

        if result:
            bankroll+=martingale[step_martingale]*cotebroker
            step_martingale=0
            new_palier= 7 * (bankroll / 100)
            martingale=refresh_martingale(new_palier,cotereelle)


        else:
            step_martingale+=1
            print(step_martingale)

        if step_martingale==nb_step_mart:
            step_martingale=0
            problem+=1
            print('problem day '+str(i))
            print('bankroll '+str(bankroll))




    print("final martingale",martingale)
    print("br : ",bankroll)
    print("nb problem :",problem)
    print("cote broker",cotebroker)
    print("cote reelle",cotereelle)
    print("pourinduit",1/cotebroker)
    print("pour reel",1/cotereelle)
    mean_br.append(bankroll)

print("mean br ",np.mean(mean_br))
print("min br ",np.min(mean_br))
print("std br",np.std(mean_br))
print("bankrupt ",bankrupt)