from JsonDataLoadControl import JsonDataLoadControl
from ReturnErrorCode import ReturnErrorCode
from DebugTool import DebugTool
import traceback

ConfigSetting = {}
ConfigPath = "/etc/oplink/dragons/"
SettingPath = ConfigPath + "default.conf"

class Dragon :

     DebugMode = None
     RetrunCode = None

     def __init__(self) :

         try :
             self.RetrunCode = ReturnErrorCode()
         except :
             print "Server Init Error!"
             print traceback.format_exc()
             exit()
