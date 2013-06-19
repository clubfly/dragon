from time import time
class DebugTool :

    Debug = None

    def __init__(self,DebugCheck) :

        self.Debug = int(DebugCheck)

    def ShowDebugLog(self,DataSet) :

        if bool(self.Debug) :
            print DataSet + " Time : " + str(time())
