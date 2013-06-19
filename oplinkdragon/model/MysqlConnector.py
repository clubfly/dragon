import MySQLdb
import MySQLdb.cursors
import simplejson as json
import random

class MysqlConnector :

    getServerList = None

    def __init__(self,DatabaseList) :

        FileOpen = open(DatabaseList)
        self.getServerList = json.load(FileOpen)
        FileOpen.close()

    def setSelSqlCommanToDatabase(self,SqlCommand,Fields) :

        ReturnData = {}
        ServerMax = len(self.getServerList["slave"])
        ServerRandom = str(random.randint(0,ServerMax-1))
        SqlConnect = MySQLdb.Connect(
                                     host=self.getServerList["slave"][ServerRandom]["host"],
                                     user=self.getServerList["slave"][ServerRandom]["user"],
                                     passwd=self.getServerList["slave"][ServerRandom]["password"],
                                     db=self.getServerList["slave"][ServerRandom]["database"],
                                     charset='utf8',
                                     use_unicode=True,
                                     cursorclass=MySQLdb.cursors.DictCursor
                                    )
        SqlLink = SqlConnect.cursor()
        try :
            SqlLink.execute(SqlCommand,Fields)
            ReturnData = SqlLink.fetchall();
        except :
            print "Error: unable to fecth data"
        SqlLink.close()

        return ReturnData

    def setIUDSqlCommanToDatabase(self,SqlCommand,Fields) :
        ReturnData = False
        ServerMax = len(self.getServerList["master"])
        ServerRandom = str(random.randint(0,ServerMax-1))
        SqlConnect = MySQLdb.Connect(
                                     host=self.getServerList["master"][ServerRandom]["host"],
                                     user=self.getServerList["master"][ServerRandom]["user"],
                                     passwd=self.getServerList["master"][ServerRandom]["password"],
                                     db=self.getServerList["master"][ServerRandom]["database"],
                                     charset='utf8',
                                     use_unicode=True,
                                     cursorclass=MySQLdb.cursors.DictCursor
                                     )
        SqlLink = SqlConnect.cursor()
        try :
            SqlLink.execute(SqlCommand,Fields)
            SqlConnect.commit()
            ReturnData = True
        except :
            SqlConnect.rollback()
        SqlLink.close()

        return ReturnData
