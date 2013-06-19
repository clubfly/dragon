#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import os
#OSPath = os.getcwd()
OSPath = os.path.abspath(os.path.dirname(__file__))
print "Program Path At " + OSPath
sys.path.append(OSPath + '/lib/')
sys.path.append(OSPath + '/model/')
sys.path.append(OSPath + '/method/')

from types import MethodType
from time import time
from Dragon import Dragon
from ReturnErrorCode import ReturnErrorCode
from bottle import route,run,Bottle
from gevent.pywsgi import WSGIServer
from JsonDataLoadControl import JsonDataLoadControl
import simplejson as json
import traceback

ConfigPath = "/etc/oplink/dragons/"

try :
    print "Config Loading..."
    Config = JsonDataLoadControl(ConfigPath + "default.conf").getJsonDataMapping()
    print "Bound Method Loading...."
    MethodList = JsonDataLoadControl(Config[Config["Version"]]["MethodSetting"]).getJsonDataMapping()
    Factory = Dragon()
    app = Bottle()
    for element in MethodList :
        try :
            print "Method : " + MethodList[element]["ReturnMethod"] + " Is Setting...."
            setattr(Factory,
                    MethodList[element]["ReturnMethod"],
                    MethodType(getattr(__import__(MethodList[element]["ReturnMethod"]),
                                       MethodList[element]["ReturnMethod"]),
                               Factory,
                               Factory.__class__))
            Url = ""
            Url += MethodList[element]["Host"]
            Url += MethodList[element]["Method"]
            Url += MethodList[element]["APIKey"]
            Url += MethodList[element]["JsonEncodeValue"]
            print "Http Url : " + Url + " Is Setting...."
            @app.route(Url,method=MethodList[element]["HttpMethod"])
            def callback(Function,APIKey,Base64EncodeJsonData) :
                try :

                    return getattr(Factory,Function)(Function,APIKey,Base64EncodeJsonData)

                except :
                    print "Method Not Allowed"

                    return json.JSONEncoder().encode(ReturnErrorCode().getReturnErrorCode("405"))

            print MethodList[element]["ReturnMethod"] + " Setting Is Finished"
        except :
            print MethodList[element]["ReturnMethod"] + " Define Error!"
    try :
        print "Server Is Starting...."
        WSGIServer((Config[Config["Version"]]["Domain"],int(Config[Config["Version"]]["Port"])),app).serve_forever()
    except :
        print "Server Error!"
        print traceback.format_exc()
except :
    print "Data Setting Error"
    print traceback.format_exc()
