class callDetails:
    def __init__(self):
        self.callf=""
        self.callt=""
        self.dur=""
        self.ctype=""
    def processDetails(self,listOfCallDetails):
        self.callf = listOfCallDetails[0]
        self.callt = listOfCallDetails[1]
        self.dur = listOfCallDetails[2]
        self.ctype = listOfCallDetails[3]
        self.printd()
    def printd(self):
        print(self.callf,end=" ")
        print(self.callt,end=" ")
        print(self.dur,end=" ")
        print(self.ctype)
class util:
    def __init__(self):
        self.list_of_cal_details = []
    def parse_customer(self,callStringList):
        for i in range(len(callStringList)):
            self.list_of_cal_details.append(callStringList[i].split(","))
            callDetails().processDetails(self.list_of_cal_details[i])
call1 = "9481476756,7406636601,5.0,local"
call2 = "9742011501,9481476756,43.0,STD"
call3 = "7975149962,7406636601,5,local"
lst = [call1,call2,call3]
util().parse_customer(lst)