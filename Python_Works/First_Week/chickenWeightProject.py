import random

chickenNum = int(input("How many chickens do you have?: "))
chickenWeightMin = int(input("What is the minimum weight of a chicken?: "))
chickenWeightMax = int(input("What is the maximum weight of a chicken?: "))
day = int(input("How many days will you measure?: "))


def calculate():
    total = 0
    avgWeight = 0
    totalChicken = 0 # it will sum chicken number which is measured randomly
    for i in range (1,day+1):
        chickenRand = random.randint(0, chickenNum) # number of measured chickens a day
        print(i, ". day ", chickenRand, " chickens measured.")
        totalChicken += chickenRand
        for j in range(1,chickenRand+1):
            weightRand = random.randint(chickenWeightMin, chickenWeightMax) # a chicken's random weight
            print(j, " . chicken weight: ", weightRand)
            total += weightRand
        print("Uploaded total weight: ", total)  # total weight of end of the per day
    print("Average weight: ", total / totalChicken) # average weight of end of the days
calculate()
              
