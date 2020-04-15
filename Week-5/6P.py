inList = ['(','{','[']
outList = [')','}',']']
class processString:
    def __init__(self):
        self.parList = []
    def proString(self,strP):
        for i in strP:
            if i in inList:
                self.parList.append(i)
            elif i in outList and len(self.parList)!=0:
                m = outList.index(i)
                if(self.parList[-1]==inList[m]):
                    self.parList.pop()
            else:
                print("Not possible")
                break
        if len(self.parList)!=0:
            print("Not possible")
strp = "()"
processString().proString(strp)