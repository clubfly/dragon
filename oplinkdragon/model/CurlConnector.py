import pycurl
import StringIO

class CurlConnector :

    def __init__(self) :
        pass

    def cUrlPost(self,Url,PostFields) :
        cUrl = pycurl.Curl()
        cUrl.setopt(cUrl.URL, str(Url))
        cUrl.setopt(cUrl.FOLLOWLOCATION,0)
        cUrl.setopt(cUrl.POST, 1)
        cUrl.setopt(cUrl.POSTFIELDS,PostFields)
        WebContent = StringIO.StringIO()
        cUrl.setopt(cUrl.WRITEFUNCTION,WebContent.write)
        cUrl.perform()
        cUrl.close()
        ReturnData = WebContent.getvalue()
        WebContent.close()

        return ReturnData

    def cUrlGet(self,Url) :

        cUrl = pycurl.Curl()
        cUrl.setopt(cUrl.URL, str(Url))
        cUrl.setopt(cUrl.FOLLOWLOCATION,0)
        cUrl.setopt(cUrl.POST, 0)
        WebContent = StringIO.StringIO()
        cUrl.setopt(cUrl.WRITEFUNCTION,WebContent.write)
        cUrl.perform()
        cUrl.close()
        ReturnData = WebContent.getvalue()
        WebContent.close()

        return ReturnData
"""
test = CurlConnector()
content = test.cUrlGet("https://graph.facebook.com/me?access_token=AAABpnOMMv78BACNuG5WSy0pAxXouQLQNl1uzmld3tGIEYnZCmMEdQ07f0wiBlpYRC2wLfiUfRwSv3YAP2d6JMIZAcet3xoxkzEpeVt0QZDZD")
print content
"""
