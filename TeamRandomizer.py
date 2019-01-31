import random

teams = ['Wet Supremacy', ]

def assignTargets(teams, allNames):
    used = []
    rList = random.sample(range(5* len(teams)), 5*len(teams))

    for i in range(5):
        if (rList[5 * len(teams) - 1 - i]/5 == len(teams) - 1):
            temp = rList[i]
            rlist[i] = rList[5 * len(teams) - 1 - i]
            rList[5 * len(teams) - 1 - i] = temp
        
        passed = []
        currentIndex = 0
        passedIndex = 0

        for i in range(len(teams)):
            print(teams[i] + " Targets: ")
            
            for j in range(5):
                if (currentIndex < 5 * len(teams)):
                    rt = int(rList[currentIndex]/5)
                    rp = rList[currentIndex] % 5
                    currentIndex += 1

                    while(rt == 1):
                        passed.append(rList[currentIndex - 1])
                        rt = int(rList[currentIndex]/5)
                        rp = rList[currentIndex] % 5
                        currentIndex += 1
                    
                    used.append(allNames[rt][rp])
                    print(allNames[rt][rp])
                
                else:
                        rt = int(passed[passedIndex]/5)
                        rp = passed[passedIndex] % 5
                        passedIndex += 1
                        used.append(allNames[rt][rp])
                        print(allNames[rt][rp])
                
                print('\n')
            
            for i in range(len(teams)):
                for j in range(5):
                    if(used.count(allNames[i][j]) != 1):
                        print("DO NOT USE THIS SAMPLE, RUN AGAIN")

assignTargets(teams, allNames)