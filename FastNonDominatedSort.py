__author__ = 'MJ'

import operator
import math
import GlobalVariables as gv

#This function takes a list of individuals [ID,string[2],tradesheet,per_min_mtm,parameter_list,status]
#And returns a list of lists, [[Front 1 individuals],[Front 2 individuals],[.....]]

class Sort:

    def FastNonDominatedSort(self, PopulationStore):

        FrontOfPopulation={}
        length=len(PopulationStore)


        num=0
        othernum=1

        delta1=gv.delta_Performance_Measure_1
        delta2=gv.delta_Performance_Measure_2

        dummy=max(PopulationStore,key=lambda x:x[gv.index][othernum])
        startValue_othernum=dummy[gv.index][othernum] #Take the maximum value of the performance measure (Assuming that greater the value of performance measure
                                               # better the individual)

        #Sorting on the basis of first objective function
        PopulationStore.sort(key=lambda x: x[gv.index][num])

        startValue_num=PopulationStore[length-1][gv.index][num]  #Take the maximum value of the performance measure (Assuming that greater the value of performance measure
                                                         # better the individual)


        if(self.deltaCompare(startValue_num,PopulationStore[length-1][gv.index][num],PopulationStore[length-2][gv.index][num],delta1)==0):
            FrontOfPopulation[PopulationStore[length-1][0]]=1
            #print FrontOfPopulation
            adjacentFront_1=1
            t=length-2
            #print("Different front")
        else:
            #print("Same front")
            t=length-1
            #print "t",t
            adjacentFront_1=0

        while(t>0):
            if(self.deltaCompare(startValue_num,PopulationStore[t][gv.index][num],PopulationStore[t-1][gv.index][num],delta1)==1):
                store={}
                store[t]=[PopulationStore[t][0],PopulationStore[t][gv.index][othernum]]
                store[t-1]=[PopulationStore[t-1][0],PopulationStore[t-1][gv.index][othernum]]
                #print store
                t=t-1
                while(t>0 and (startValue_num,PopulationStore[t][gv.index][num],PopulationStore[t-1][gv.index][num],delta1)==1):
                    store[t-1]=[PopulationStore[t-1][0],PopulationStore[t-1][gv.index][othernum]]
                    t=t-1

                #print store
                storeItems=store.items()
                storeItems.sort(key=lambda x:x[1][1])
                storeLength=len(storeItems)
                adjacentVal_2=storeItems[storeLength-1][1][1]

                #print storeItems
                FrontOfPopulation[storeItems[storeLength-1][1][0]]=adjacentFront_1+1
                adjacentFront_2=FrontOfPopulation[storeItems[storeLength-1][1][0]]

                l=storeLength-2
                #print "l",l
                for l in range(storeLength-2,-1,-1):
                    if(self.deltaCompare(startValue_othernum,storeItems[l][1][1],adjacentVal_2,delta2)==1):
                        FrontOfPopulation[storeItems[l][1][0]]=adjacentFront_2
                    else:
                        FrontOfPopulation[storeItems[l][1][0]]=adjacentFront_2+1

                    adjacentFront_2=FrontOfPopulation[storeItems[l][1][0]]
                    adjacentVal_2=storeItems[l][1][1]

                adjacentFront_1=adjacentFront_2
                adjacentVal_1=PopulationStore[t][gv.index][num]

            else:
                FrontOfPopulation[PopulationStore[t][0]]=adjacentFront_1+1
                adjacentFront_1=adjacentFront_1+1
                adjacentVal_1=PopulationStore[t][gv.index][num]

            t=t-1

        if(t==0):
            FrontOfPopulation[PopulationStore[t][0]]=adjacentFront_1+1
            adjacentFront_1=adjacentFront_1+1

     #   print FrontOfPopulation

    #Sorting on the basis of second objective function
        num=1
        othernum=0


        dummy=max(PopulationStore,key=lambda x:x[gv.index][othernum])
        startValue_othernum=dummy[gv.index][othernum]

        #Sorting on the basis of first objective function
        PopulationStore.sort(key=lambda x: x[gv.index][num])

        startValue_num=PopulationStore[length-1][gv.index][num]

        #print startValue_num,PopulationStore[length-1][1][num],PopulationStore[length-2][1][num],delta2

        if(self.deltaCompare(startValue_num,PopulationStore[length-1][gv.index][num],PopulationStore[length-2][gv.index][num],delta2)==0):
            FrontOfPopulation[PopulationStore[length-1][0]]=1
            #print FrontOfPopulation
            adjacentFront_1=1
            t=length-2
        else:
            t=length-1
            adjacentFront_1=0

        while(t>0):
            if(self.deltaCompare(startValue_num,PopulationStore[t][gv.index][num],PopulationStore[t-1][gv.index][num],delta2)==1):
                store={}
                store[t]=[PopulationStore[t][0],PopulationStore[t][gv.index][othernum]]
                store[t-1]=[PopulationStore[t-1][0],PopulationStore[t-1][gv.index][othernum]]
                #print store
                t=t-1
                while(t>0 and self.deltaCompare(startValue_num,PopulationStore[t][gv.index][num],PopulationStore[t-1][gv.index][num],delta2)==1):
                    store[t-1]=[PopulationStore[t-1][0],PopulationStore[t-1][gv.index][othernum]]
                    t=t-1

                #print store
                storeItems=store.items()
                storeItems.sort(key=lambda x:x[1][1])
                storeLength=len(storeItems)
                adjacentVal_2=storeItems[storeLength-1][1][1]

                #print storeItems
                FrontOfPopulation[storeItems[storeLength-1][1][0]]=min(adjacentFront_1+1,FrontOfPopulation[storeItems[storeLength-1][1][0]])
                adjacentFront_2=adjacentFront_1+1
                l=storeLength-2
                for l in range(storeLength-2,-1,-1):
                    if(self.deltaCompare(startValue_othernum,storeItems[l][1][1],adjacentVal_2,delta1)==1):
                        FrontOfPopulation[storeItems[l][1][0]]=min(adjacentFront_2,FrontOfPopulation[storeItems[l][1][0]])

                    else:
                        FrontOfPopulation[storeItems[l][1][0]]=min(adjacentFront_2+1,FrontOfPopulation[storeItems[l][1][0]])
                        adjacentFront_2=adjacentFront_2+1

                    adjacentVal_2=storeItems[l][1][1]

                adjacentFront_1=adjacentFront_2
                adjacentVal_1=PopulationStore[t][gv.index][num]

            else:
                FrontOfPopulation[PopulationStore[t][0]]=min(FrontOfPopulation[PopulationStore[t][0]],adjacentFront_1+1)
                adjacentFront_1=adjacentFront_1+1
                adjacentVal_1=PopulationStore[t][gv.index][num]

            t=t-1

        if(t==0):
            FrontOfPopulation[PopulationStore[t][0]]=min(FrontOfPopulation[PopulationStore[t][0]],adjacentFront_1+1)
            adjacentFront_1=adjacentFront_1+1

    #    print FrontOfPopulation
        counter= max(FrontOfPopulation.iteritems(), key=operator.itemgetter(1))[1]


        F = [[] for x in xrange(counter)]


        for k in FrontOfPopulation.keys():
            F[FrontOfPopulation[k]-1].append(k)

        return F

    def deltaCompare(self,startValue, v1,v2, delta):
        #print (startValue,v1,v2,delta)
        bin1=math.ceil((startValue-v1)/delta)
        bin2=math.ceil((startValue-v2)/delta)
        #print(bin1,bin2)
        if(bin1==bin2):
            return 1
        else:
            return 0



if __name__ == '__main__':

    Pt = []
    print Pt
    Pt.append([1,[],[],[],[17,20,1,1,1,1,1]])
    Pt.append([4,[],[],[],[15,10,2,2,2,2,2]])
    Pt.append([3,[],[],[],[20,11,0,0,0,0,0]])
    print Pt
    sortObject=Sort()
    F=sortObject.FastNonDominatedSort(Pt)

    #numFronts=max(F.keys())
    print F
    #print "Num of fronts",numFronts

    '''
    individualList = []
    rankList = []
    rank=1
    for j in range(1,numFronts+1):
        for individual in F[j].keys():
            individualList.append(individual)
            rankList.append(rank)
            rank=rank+1
    print individualList


    F=FastNonDominatedSort(Pt)
    numFronts=max(F.keys())
    rank=1
    for j in range(1,numFronts+1):
        for individual in F[j].keys():
            print (individual,rank)
            #dbObject.updateRank(individual, rank)
            rank=rank+1

    '''
