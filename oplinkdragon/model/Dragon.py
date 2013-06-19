from JsonDataLoadControl import JsonDataLoadControl
from ReturnErrorCode import ReturnErrorCode
from DebugTool import DebugTool

ConfigSetting = {}
ConfigPath = "/etc/oplink/dragon/"
SettingPath = ConfigPath + "default.conf"

class Dragon :

     DebugMode = None
     RetrunCode = None

     def __init__(self) :

         try :
             self.RetrunCode = ReturnErrorCode()
         except :
             print "Server Init Error!"
             exit()
