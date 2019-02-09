# -*- coding: utf-8 -*-
from module import dbmanager
import time
import os #added
from PIL import Image, ImageFilter
from os import system
import json


'''
COMANDI SERVER HTTP
- Carica pagine HTML
- Restituisce percorso directory
- Restituisce immagini


'''


def realtimeupd ():
    db = None
    result = ''
    try:
        data = {
            "vncserver": ["vncserver","ok","23122018_01"],"samba":["samba","ok","23122018_02"]
        }
        data2={}
        # ESEGUO SCRIPT RT.PY
        cmd="python %s/rt.py" % str(os.path.dirname(os.path.abspath(__file__)))
        system(cmd)
        # LEGGO ELENCO TB_REALTIME
        db = dbmanager.openDB(db, str(os.path.dirname(os.path.abspath(__file__))) + "/db/", 'system.db')
        rows = DB_Manager.SELECT_TB_SYS_SERVICE_INFO(db)
        for row in rows:
            data2[row[0]]=[str(row[0]),str(row[1]),str(row[2])]

        result=json.dumps(data2)
    except  Exception as e:
        result = "Error-%s:%s " % ("realtimeupd", e)
    finally:
        return result




''''''

def nrf24cmd (authKey,command):
    db = None
    result = ''
    try:
        if not ValidateKey(authKey):
            result = "Invalid Auth Key!"
        else:
            #print str(os.path.dirname(os.path.abspath(__file__))) + "/db/"
            db = dbmanager.openDB(db, str(os.path.dirname(os.path.abspath(__file__))) + "/db/","system.db")
            try:
                dbmanager.insert_TB_HOME_COM(db, command)
                r = dbmanager.select_last_TB_HOME_COM(db)
                if int(r[0]) > 0:
                    time.sleep(3)
                    result = dbmanager.select_TB_HOME_COM(db, str(r[0]))
                    if result != '':
                        result = result[4]
            except  Exception as e:
                db = dbmanager.closeDB(db)
                result = "Error-%s:%s " % ("nrf24cmd", e)

    except  Exception as e:
        result = "Error-%s:%s " % ("nrf24cmd", e)
    finally:
        return result

def nrf24cmdlist(authKey):
    db = None
    result = ''
    try:
        if not ValidateKey(authKey):
            result = "Invalid Auth Key!"
        else:
            #print str(os.path.dirname(os.path.abspath(__file__))) + "/db/"
            db = dbmanager.openDB(db, str(os.path.dirname(os.path.abspath(__file__))) + "/db/","system.db")
            try:
                rows=dbmanager.select_TB_HOME_DIZ_CMD_LIST(db)
                for row in rows:
                    result = result+str(row[0])+";"
            except  Exception as e:
                db = dbmanager.closeDB(db)
                result = "Error-%s:%s " % ("nrf24cmdlist", e)

    except  Exception as e:
        result = "Error-%s:%s " % ("nrf24cmdlist", e)
    finally:
        return result


def servicelist(authKey):
    db = None
    result = ''
    try:
        print 'servicelist'
        if not ValidateKey(authKey):
            result = "Invalid Auth Key!"
        else:
            #print str(os.path.dirname(os.path.abspath(__file__))) + "/db/"
            db = dbmanager.openDB(db, str(os.path.dirname(os.path.abspath(__file__))) + "/db/","system.db")
            try:
                rows=dbmanager.SELECT_TB_SYS_SERVICE_LIST(db)
                for row in rows:
                    result = result+str(row[0])+";"
            except  Exception as e:
                db = dbmanager.closeDB(db)
                result = "Error-%s:%s " % ("servicelist", e)

    except  Exception as e:
        result = "Error-%s:%s " % ("servicelist", e)
    finally:
        return result
un j
def servicecmd (s,c,authKey):
    db = None
    result = ''
    try:
        if not ValidateKey(authKey):
            result = "Invalid Auth Key!"
        else:
            system("sudo service %s %s >%sout.txt" % (s, c,str(os.path.dirname(os.path.abspath(__file__)))+"/"))
            f = open(str(os.path.dirname(os.path.abspath(__file__)))+"/out.txt", "r")
            result = f.read()
            f.close()
            result=result.replace("\n", "&lt;br&gt;")
            system("sudo rm %sout.txt " % (str(os.path.dirname(os.path.abspath(__file__))) + "/"))

    except  Exception as e:
        result = "Error-%s:%s " % ("servicecmd", e)
    finally:
        return result

def pcctrl(authKey,command):
    url = self.request.url
    result=''
    try:
        if ValidateKey(authKey):
            if command=='on':
                system("wakeonlan -i 255.255.255.255 10:E7:C6:EE:E5:03")
            elif command=='off':
                system("net rpc shutdown -I 192.168.1.17 10:E7:C6:EE:E5:03 -U dmeno%dagian92")
        result ='Comando PC '+command+' Inviato!'

    except  Exception as e:
        result = "Error-%s:%s " % ("pcctrl", e)
    finally:
        return result






# KEY Menoz: 551f0f2fc174442cadb95df9f957d808
# KEY Sonia: cc4c082091a94301848473918694b357
def ValidateKey(k):
    k_menoz="551f0f2fc174442cadb95df9f957d808"
    k_sonia="cc4c082091a94301848473918694b357"
    result=False
    if k==k_menoz or k==k_sonia:
        result=True
    return result