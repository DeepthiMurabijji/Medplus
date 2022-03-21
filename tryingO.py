
import random

parkingLotArea = 10 * 10

dictionArea = {

    'A':{
        'car': parkingLotArea * 0.6,
        'bike': parkingLotArea * 0.3,
        'bus': parkingLotArea * 0.1
    },
    'B':{
        'car': parkingLotArea * 0.6,
        'bike': parkingLotArea * 0.3,
        'bus': parkingLotArea * 0.1
    },
    'C':{
        'car': parkingLotArea * 0.6,
        'bike': parkingLotArea * 0.3,
        'bus': parkingLotArea * 0.1
    }

}

serials = ['A', 'B', 'C']

BLen = 3
BWid = 3
BArea = BLen * BWid

inTime = 0

for keys, values in dictionArea.items():

    if BArea <= dictionArea[keys]['bike']:
        dictionArea[keys]['bike'] -= BArea
        print(dictionArea[keys]['bike'])
        print(keys)

        inTime = random.randint(0,24) # 20
        outTime = random.randint(0,24) # 4

        duration = abs(inTime - outTime) * 60

        amountPayable = 0
        if duration > 600:
            amountPayable = duration//60 * 5
            print(amountPayable)
        else:
            print("Less than 10 hours in the parking")
        
        break
