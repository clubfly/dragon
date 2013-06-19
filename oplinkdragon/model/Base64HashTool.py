import base64

class Base64HashTool :

    def getBase64Encode(self,String) :

        return base64.urlsafe_b64encode(String)

    def getBase64Decode(self,String) :

        return base64.urlsafe_b64decode(String)
