from module import dbmanager
from os import system
import datetime
import os

# RITORNA: STRINGA STATO SERVIZIO O STRINGA ERRORE
def retServiceStatus(service):
    SUBNAME = "retServiceStatus"
    path=str(os.path.dirname(os.path.abspath(__file__)))
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

# RITORNA: STRINGA VUOTA SE ESECUZIONE OK O STRINGA ERRORE
def UpdateRealtime(retstr):
    SUBNAME = "UpdateRealtime"

    db=None
    result=""
    RT_LASTUPDATE=""
    RT_STATE=""
    RT_NOTE=""
    RT_SUBJECT=""

    # PREPARO PARAMETRI QUERY
    RT_LASTUPDATE=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    r=retstr.split(" ")
    r=r[3:] # TOLGO I PRIMI 3 ELEMENTI PERCHE VUOTI
    RT_SUBJECT=r[0]
    RT_STATE=r[1]
    RT_NOTE=" ".join(r[2:])

    # UPDATE TB_REALTIME
    try:
        db=dbmanager.openDB(db, str(os.path.dirname(os.path.abspath(__file__))) + "/db/",'system.db')
        result=dbmanager.UPDATE_TB_SYS_REALTIME_INFO(db,RT_SUBJECT,RT_STATE,RT_LASTUPDATE,RT_NOTE)
        if result != '':
            raise Exception(result)

    # ERRORE!
    except Exception as e:
        result = "Error-%s:%s " % (SUBNAME, e)
    # RITORNA RISULTATO
    finally:
        db = dbmanager.closeDB(db)
        return result

def main():
    SUBNAME = "main"

    servicelist = ['samba', 'ssh', 'openvpn', 'vsftpd']
    result=[0,""]
    path=""

    # CICLO PER TUTTI I SERVIZI E AGGIORNO STATO
    try:
        for s in servicelist:
            result=retServiceStatus(s)
            if result[0] != 0:
                raise Exception(result[1])
            result=UpdateRealtime(result[1])
            if result != "":
                raise Exception(result)

    # ERRORE!
    except Exception as e:
        print "Error-%s:%s " % (SUBNAME, e)



if __name__ == '__main__':
    main()
