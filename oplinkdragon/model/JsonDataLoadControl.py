import simplejson as json

class JsonDataLoadControl :

    DataMapping = {}

    def __init__(self,JsonDataList) :

        FileOpen = open(JsonDataList)
        self.DataMapping = json.load(FileOpen)
        FileOpen.close()

    def getJsonDataMapping(self) :

        return self.DataMapping
