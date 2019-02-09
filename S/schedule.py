from GreyMatter.db import DB_Manager
from os import system
import datetime



# RITORNA: STRINGA STATO SCRIPT PY MENOZ O STRINGA ERRORE
def retPyScriptStatus(path,service):

    result=[0,""]
    line=""

    # INVIO COMANDO STATUS SERVIZIO
    cmd="sudo bash %s.sh status >%s.txt" % (path+service,path+service)
    system(cmd)
    # LEGGO RISPOSTA
    try:
        f = open(path+service + ".txt", "r")
        line = f.readline()
        if line !="":
            result[1]=line
        f.close()
        system("sudo rm %s.txt " % (path+service) )
    # ERRORE!
    except Exception as e:
        result[0] = 1
        result[1]= "Error-%s:%s " % (SUBNAME, e)
    # RITORNO RISULTATO
    finally:
        return result

# RITORNA: STRINGA STATO SERVIZIO O STRINGA ERRORE
def retServiceStatus(path,service):
    SUBNAME = "retServiceStatus"

    result=[0,""]
    line=""

    # INVIO COMANDO STATUS SERVIZIO
    cmd="service %s status | grep Active >%s.txt" % (service,path+service)
    system(cmd)
    # LEGGO RISPOSTA
    try:
        f = open(path+service + ".txt", "r")
        line = f.readline()
        if line !="":
            result[1]=line.replace("Active:",service)
        f.close()
        system("sudo rm %s.txt " % (path+service) )
    # ERRORE!
    except Exception as e:
        result[0] = 1
        result[1]= "Error-%s:%s " % (SUBNAME, e)
    # RITORNO RISULTATO
    finally:
        return result

# RITORNA: STRINGA VUOTA SE ESECUZIONE OK O STRINGA ERRORE (tipo:0=Update service;1=Update Script)
def UpdateRealtime(retstr,tipo):
    SUBNAME = "UpdateRealtime"

    db=None
    result=""
    RT_LASTUPDATE=""
    RT_STATE=""
    RT_NOTE=""
    RT_SUBJECT=""

    if tipo == 0:
        # PREPARO PARAMETRI QUERY
        RT_LASTUPDATE=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        r=retstr.split(" ")
        r=r[3:] # TOLGO I PRIMI 3 ELEMENTI PERCHE VUOTI
        RT_SUBJECT=r[0]
        RT_STATE=r[1]
        RT_NOTE=" ".join(r[2:])
    else:
        # PREPARO PARAMETRI QUERY
        RT_LASTUPDATE=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        r = retstr.split(" ")
        RT_SUBJECT = r[0]
        RT_STATE = r[1]
        RT_NOTE = ""

    # UPDATE TB_REALTIME
    try:
        db=DB_Manager.openDB(db,'system.db')
        result=DB_Manager.UPDATE_TB_SYS_REALTIME_INFO(db,RT_SUBJECT,RT_STATE,RT_LASTUPDATE,RT_NOTE)
        if result != '':
            raise Exception(result)

    # ERRORE!
    except Exception as e:
        result = "Error-%s:%s " % (SUBNAME, e)
    # RITORNA RISULTATO
    finally:
        db = DB_Manager.closeDB(db)
        return result

def main():
    SUBNAME = "main"

    servicelist = ['samba', 'ssh', 'openvpn', 'vsftpd']
    scriptlist = ['bot']
    result=[0,""]
    path=""

    # CICLO PER TUTTI I SERVIZI E AGGIORNO STATO
    try:

        for s in scriptlist:
            result=retPyScriptStatus('/home/pi/Desktop/BotSonja/support/',s)
            if result[0] != 0:
                raise Exception(result[1])
            result=UpdateRealtime(result[1],1)
            if result != "":
                raise Exception(result)

        for s in servicelist:
            result=retServiceStatus('',s)
            if result[0] != 0:
                raise Exception(result[1])
            result=UpdateRealtime(result[1],0)
            if result != "":
                raise Exception(result)

    # ERRORE!
    except Exception as e:
        print "Error-%s:%s " % (SUBNAME, e)



if __name__ == '__main__':
    main()
