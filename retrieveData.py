# this is script for retrieve data from sensor. 
# analogy data is -x -> +x
# digital data is 0 or 1

#TODO 
# push new data to buffer_for_one_time_press
# check new cycle started or current cycle finished using digital signal from a sensor.
# save analog sensor data to csv file when current cycle is finished
# file name should be timestamp.csv
import random, time, os
as1 = []
as2 = []
def produceDummyValues():
    for i in range(1000):
        analogSensor1= random.randint(0,500)
        analogSensor2 = random.randint(0,500)
        as1.append(analogSensor1)
        as2.append(analogSensor2)

def produceDummyDigitalValues():
    dig = []
    for i in range(1000):
        digitalSensor = random.randint(0,1)
        dig.append(digitalSensor)
        if digitalSensor == 1:
            cycleStartTime = time.time()
            if checkCycleFinished(digitalSensor) == True:
                pushData(digitalSensor, cycleStartTime)
        #print(checkCycleFinished(digitalSensor))
        #print("this is timestamp: ", cycleStartTime)


def checkCycleFinished(d):
    if d == 0:
        result = True
    else:
        result = False
    return result
#print(produceDummyDigitalValues())
#print (produceDummyValues())

def pushData(ds, s):
    # Create dir on local memory
    # Create a file which stores all sensor data in dir.
    p = "/home/azaa/pythonScripts/data.txt"
    if not os.path.exists(p):
        ff = open(p, 'a')
        ff.write(str(ds))
        ff.close()
    else:
        print("File already exists!")

def saveAsCSV():
    # file name will be timestamp which cycle has started.
    # csv file header info
    return

# p = "/home/azaa/pythonScripts/data.txt"
# f = open(p, 'wt')

# dumValues = produceDummyValues()
# dumDigValues = produceDummyDigitalValues()

# print(dumValues, dumDigValues)
produceDummyValues()
produceDummyDigitalValues()

for i in range (1000):
    pushData(as1[i], as2[i])

