#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import datetime
import os.path





def openDB (objDB,pathDB,nameDB):
  db_path = os.path.join(pathDB, nameDB)
  #print db_path
  try:
    objDB = lite.connect(db_path)
    #print "DB OPEN!"
    
  except lite.Error as e:
    print "DB OPEN Error:",e
    
  finally:
    return objDB

def printSQLVersion(objDB):

  try:  
    if objDB:
      cur = objDB.cursor()    
      cur.execute('SELECT SQLITE_VERSION()')  
      data = cur.fetchone()
      print "SQLite version: %s" % data
    else:
      print "DB not init!"
      r="DB not init!"
    
  except lite.Error as e:
    print "Error:",e
    sys.exit(1)

def closeDB(objDB):
  try:
    if objDB:
      objDB.close()
      #print "DB CLOSE!"
      
  except lite.Error as e:
    print "DB CLOSE Error:",e
    sys.exit(1)
    
  finally:
    return objDB

'''
------------------------------------------------------------------------------------------------------------------------
TB_SONJA_KEY
------------------------------------------------------------------------------------------------------------------------
'''
def SELECT_ONE_TB_SONJA_KEY_VALUE(objDB,KEY_NAME):
  SUBNAME = "SELECT_ONE_TB_SONJA_KEY_VALUE"
  result = ''

  try:
    if objDB:
      cur = objDB.cursor()
      cur.execute("SELECT * FROM TB_SONJA_KEY WHERE KEY_NAME = '%s';" % KEY_NAME)
      rows = cur.fetchall()
      result=rows[0][2]
    else:
      result = "Error-%s:%s " % (SUBNAME, "DB not init!")



  except lite.Error as e:
    objDB.rollback()
    result = "Error-%s:%s " % (SUBNAME, e)

  except Exception as e:
    result = "Error-%s:%s " % (SUBNAME, e)

  finally:
    return result


def insert_TB_SONJA_KEY(objDB,nomekey,valuekey):
  r = ''
  try:
    if objDB:
      cur = objDB.cursor()
      print "INSERT INTO TB_SONJA_KEY VALUES(NULL,'"+nomekey+"','"+valuekey+"');"
      cur.execute("INSERT INTO TB_SONJA_KEY VALUES(NULL,'"+nomekey+"','"+valuekey+"');")
      objDB.commit()
    else:
      r= "DB not init!"

  except lite.Error, e:
    objDB.rollback()
    r = "Error %s:" % e.args[0]
    sys.exit(1)
  finally:
    return r

def SELECT_TB_SONJA_KEY_NOME(objDB):
  SUBNAME = "SELECT_TB_SONJA_KEY_NOME"
  result = ''

  try:
    if objDB:
      cur = objDB.cursor()
      cur.execute("SELECT KEY_NAME FROM TB_SONJA_KEY ;")
      rows = cur.fetchall()
      result=rows

    else:
      result = "Error-%s:%s " % (SUBNAME, "DB not init!")



  except lite.Error as e:
    objDB.rollback()
    result = "Error-%s:%s " % (SUBNAME, e)

  except Exception as e:
    result = "Error-%s:%s " % (SUBNAME, e)

  finally:
    return result


'''
------------------------------------------------------------------------------------------------------------------------
TB_SYS_SERVICE
------------------------------------------------------------------------------------------------------------------------
'''

def SELECT_TB_SYS_SERVICE_LIST(objDB):
  result = ""
  try:
    if objDB:
      cur = objDB.cursor()
      s = "SELECT RT_SUBJECT FROM TB_SYS_SERVICE ;"
      cur.execute(s)
      result = cur.fetchall()
    else:
      print "DB not init!"

  except lite.Error as e:
    objDB.rollback()
    print "Error:", e
    sys.exit(1)

  finally:
    return result

def SELECT_TB_SYS_SERVICE_INFO(objDB):
  SUBNAME = "SELECT_TB_SYS_SERVICE_INFO"
  result = ''

  try:
    if objDB:
      cur = objDB.cursor()
      cur.execute("SELECT * FROM TB_SYS_SERVICE;")
      result = cur.fetchall()
    else:
      result = "Error-%s:%s " % (SUBNAME, "DB not init!")

  except lite.Error as e:
    objDB.rollback()
    result = "Error-%s:%s " % (SUBNAME, e)

  except Exception as e:
    result = "Error-%s:%s " % (SUBNAME, e)

  finally:
    return result

def SELECT_ONE_TB_SYS_SERVICE_INFO(objDB,RT_SUBJECT):
  SUBNAME = "SELECT_ONE_TB_SYS_SERVICE_INFO"
  result = ''

  try:
    if objDB:
      cur = objDB.cursor()
      cur.execute("SELECT * FROM TB_SYS_SERVICE WHERE RT_SUBJECT='%s';" % RT_SUBJECT)
      result = cur.fetchall()
    else:
      result = "Error-%s:%s " % (SUBNAME, "DB not init!")

  except lite.Error as e:
    objDB.rollback()
    result = "Error-%s:%s " % (SUBNAME, e)

  except Exception as e:
    result = "Error-%s:%s " % (SUBNAME, e)

  finally:
    return result

def UPDATE_TB_SYS_SERVICE_INFO(objDB,RT_SUBJECT,RT_STATE,RT_LASTUPDATE,RT_NOTE):
    SUBNAME = "UPDATE_TB_SYS_SERVICE_INFO"
    result = ''

    try:
      if objDB:
        cur = objDB.cursor()
        s="UPDATE TB_SYS_SERVICE "
        s=s+"SET RT_STATE = '%s', " % (RT_STATE)
        s=s+"RT_LASTUPDATE='%s', " % (RT_LASTUPDATE)
        s=s+"RT_NOTE ='%s' " % (RT_NOTE)
        s=s+"WHERE RT_SUBJECT LIKE '%s';" % (RT_SUBJECT)
        cur.execute(s)
        objDB.commit()
      else:
        result = "Error %s %s " % (SUBNAME, "DB not init!")

    except lite.Error as e:
      objDB.rollback()
      result= "Error %s %s " % (SUBNAME, e)

    except Exception as e:
      result = "Error %s %s " % (SUBNAME, e)

    finally:
      return result


'''
------------------------------------------------------------------------------------------------------------------------
TB_SYS_REQUEST
------------------------------------------------------------------------------------------------------------------------
'''
def SELECT_LAST_TB_SYS_REQUEST(objDB):
    SUBNAME = "SELECT_LAST_TB_SYS_REQUEST"
    result = ''

    try:
      if objDB:
        cur = objDB.cursor()
        cur.execute("SELECT * FROM TB_SYS_REQUEST WHERE REQ_CHECK=0 ORDER BY REQ_ID DESC LIMIT 1;")
        rows = cur.fetchall()
        for row in rows:
          result = row
          # print row
      else:
        print "DB not init!"

    except lite.Error as e:
      objDB.rollback()
      print "Error:%s:" % SUBNAME, e
      sys.exit(1)

    finally:
      return result

def UPDATE_LAST_TB_SYS_REQUEST(objDB, REQ_CHECK, REQ_RESULT):
    SUBNAME = "UPDATE_LAST_TB_SYS_REQUEST"
    result = ''

    try:
      if objDB:
        cur = objDB.cursor()
        s = "UPDATE TB_SYS_REQUEST "
        s = s + "SET REQ_CHECK=%s, " % str(REQ_CHECK)
        s = s + "REQ_RESULT='%s' " % str(REQ_RESULT)
        s = s + "WHERE REQ_CHECK=0 "
        s = s + "ORDER BY REQ_ID DESC LIMIT 1;"
        #print s
        cur.execute(s)
        objDB.commit()
      else:
        print "DB not init!"

    except lite.Error as e:
      objDB.rollback()
      print "Error:%s:" % SUBNAME, e

    except Exception as e:
      print "Error:%s:" % SUBNAME, e

    finally:
      return result

def INSERT_TB_SYS_REQUEST(objDB, REQ_STRING, REQ_TERMINALE):
    SUBNAME = "INSERT_TB_SYS_REQUEST"
    result = ''

    try:
      if objDB:
        cur = objDB.cursor()
        s = "INSERT INTO TB_SYS_REQUEST VALUES (0,'%s','%s');" % str(REQ_STRING),str(REQ_TERMINALE)
        # print s
        cur.execute(s)
        objDB.commit()
      else:
        print "DB not init!"


    except lite.Error as e:
      objDB.rollback()
      print "Error:%s:" % SUBNAME, e

    except Exception as e:
      print "Error:%s:" % SUBNAME, e

    finally:
      return result
    
'''
------------------------------------------------------------------------------------------------------------------------
TB_HOME_REALTIME
------------------------------------------------------------------------------------------------------------------------
'''
def update_TB_HOME_REALTIME(objDB, NRF_NODO, NRF_VAL):
    result = ''
    r = ''
    try:
      if objDB:
        s = "UPDATE TB_HOME_REALTIME "
        s = s + "SET NRF_VAL ="+ NRF_VAL +" "
        s = s + "WHERE NRF_NODO =" + NRF_NODO +" "
        cur = objDB.cursor()
        cur.execute(s)
        objDB.commit()
      else:
        print "DB not init!"

    except lite.Error as e:
      objDB.rollback()
      print "Error:", e
      sys.exit(1)

    finally:
      pass

'''
------------------------------------------------------------------------------------------------------------------------
TB_HOME_DIZ_RES
------------------------------------------------------------------------------------------------------------------------
'''
def select_TB_HOME_DIZ_RES(objDB,VAL_NODO,VAL_CMD):

  result=""
  try:
    if objDB:
      cur = objDB.cursor()
      s="SELECT VAL_STR_EXPLAIN FROM TB_HOME_DIZ_RES WHERE VAL_NODO="+VAL_NODO+" AND VAL_CMD="+VAL_CMD+";"
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        result  = row[0]
        # print row
    else:
      print "DB not init!"

  except lite.Error as e:
    objDB.rollback()
    print "Error:", e
    sys.exit(1)

  finally:
    return result

'''
------------------------------------------------------------------------------------------------------------------------
TB_HOME_DIZ_CMD
------------------------------------------------------------------------------------------------------------------------
'''

def select_TB_HOME_DIZ_CMD_LIST(objDB):
  result = ""
  try:
    if objDB:
      cur = objDB.cursor()
      s = "SELECT CMD_STR FROM TB_HOME_DIZ_CMD WHERE CMD_CLIENT=='app' ORDER BY CMD_STR;"
      cur.execute(s)
      result = cur.fetchall()
    else:
      print "DB not init!"

  except lite.Error as e:
    objDB.rollback()
    print "Error:", e
    sys.exit(1)

  finally:
    return result


def select_TB_HOME_DIZ_CMD(objDB,CMD_STR):

  result=""
  try:
    if objDB:
      cur = objDB.cursor()
      s="SELECT CMD_RESULT FROM TB_HOME_DIZ_CMD WHERE CMD_STR=='"+CMD_STR+"';"
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        result  = row[0]
        # print row
    else:
      print "DB not init!"

  except lite.Error as e:
    objDB.rollback()
    print "Error:", e
    sys.exit(1)

  finally:
    return result




'''
------------------------------------------------------------------------------------------------------------------------
TB_HOME_PRESENZE
------------------------------------------------------------------------------------------------------------------------
'''
def insert_TB_HOME_PRESENZE(objDB):
  d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  r=''
  try:  
    if objDB:
      cur = objDB.cursor()
      print "INSERT INTO TB_HOME_PRESENZE VALUES(NULL,0,'"+d+"');"
      cur.execute("INSERT INTO TB_HOME_PRESENZE VALUES(NULL,0,'"+d+"');")
      objDB.commit()
      r="INSERT INTO TB_HOME_PRESENZE VALUES(NULL,0,'"+d+"');"
    else:
      print "DB not init!"
    
  except lite.Error, e:
    objDB.rollback()
    print "Error %s:" % e.args[0]
    sys.exit(1)
  finally:
    return r

def delete_all_TB_HOME_PRESENZE(objDB):
  
  try:  
    if objDB:
      cur = objDB.cursor()
      cur.execute("DELETE FROM TB_HOME_PRESENZE")
      cur.execute("DELETE FROM sqlite_sequence WHERE name='TB_HOME_PRESENZE'")
      objDB.commit()
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

def select_TB_HOME_PRESENZE(objDB):
  
  try:  
    if objDB:
      cur = objDB.cursor() 
      cur.execute("SELECT * FROM TB_HOME_PRESENZE")
      rows = cur.fetchall()
      for row in rows:
        print row
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

def update_last_TB_HOME_PRESENZE(objDB):
  result=''
  r=''
  try:  
    if objDB:
      s="UPDATE TB_HOME_PRESENZE "
      s=s+"SET PRES_CHECK = 1 "
      s=s+"WHERE PRES_CHECK = 0 "
      s=s+"ORDER BY PRES_ID DESC "
      s=s+"LIMIT 1"
      cur = objDB.cursor() 
      cur.execute(s)
      objDB.commit()
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    pass


def select_last_TB_HOME_PRESENZE(objDB):

  r=''
  sql="SELECT PRES_DATA "
  sql=sql+"FROM TB_HOME_PRESENZE "
  sql=sql+"WHERE PRES_CHECK = 0 "
  sql=sql+"ORDER BY PRES_ID DESC "
  sql=sql+"LIMIT 1"
  try:  
    if objDB:
      cur = objDB.cursor() 
      cur.execute(sql)
      rows = cur.fetchall()
      for row in rows:
        r= row[0]
        #print row
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return r


'''
------------------------------------------------------------------------------------------------------------------------
TB_BOT_UTENTI
------------------------------------------------------------------------------------------------------------------------
'''
def select_user_name_from_chatid(objDB,chat_id):

  r=''
  try:  
    if objDB:
      s="SELECT UT_NAME "
      s=s+"FROM TB_BOT_UTENTI "
      s=s+"WHERE UT_CHATID like '"+chat_id+"'"
      cur = objDB.cursor() 
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        r=row
        #print row
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return r


def select_user_level_from_chatid(objDB,chat_id):

  r=''
  try:  
    if objDB:
      s="SELECT UT_LEVEL "
      s=s+"FROM TB_BOT_UTENTI "
      s=s+"WHERE UT_CHATID like '"+chat_id+"'"
      cur = objDB.cursor() 
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        r=row
        #print row
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return r

'''
------------------------------------------------------------------------------------------------------------------------
TB_SYS_TRAD
------------------------------------------------------------------------------------------------------------------------
'''
def select_trad(objDB,trad_id):

  r=''
  try:  
    if objDB:
      s="SELECT TRAD_IT "
      s=s+"FROM TB_SYS_TRAD "
      s=s+"WHERE TRAD_ID like '"+trad_id+"'"
      cur = objDB.cursor() 
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        r=row
        #print row
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return r

def dbtext(trad_id):
  
  result=''
  con = None
  con=openDB(con,'system.db')
  r=select_trad(con,trad_id)
  if r !='':
    result=r[0]
  con=closeDB(con)
  return result  
  
'''
------------------------------------------------------------------------------------------------------------------------
TB_BOT_FUNZIONI
------------------------------------------------------------------------------------------------------------------------
'''
def select_all_funz_with_desc(objDB):
  result=''
  r=''
  try:  
    if objDB:
      s="SELECT FUNZ_NAME,FUNZ_DESC "
      s=s+"FROM TB_FUNZIONI "
      cur = objDB.cursor() 
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        r=row
        result=result+'*'+r[0]+'*'+'-'+r[1]+chr(10)
        #print row
    else:
      print "DB not init!"

  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result      

def select_help_funz(objDB,funz_id):
  result=''
  r=''
  print 'passo '+funz_id
  try:  
    if objDB:
      s="SELECT FUNZ_HELP "
      s=s+"FROM TB_FUNZIONI "
      s=s+"WHERE FUNZ_NAME like '"+funz_id+"'"
      
      cur = objDB.cursor() 
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        r=row
        print r
        result=r[0]
        #print row
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result

def funzlist():
  
  result=''
  con = None
  con=openDB(con,'system.db')
  result=select_all_funz_with_desc(con)
  con=closeDB(con)
  return result    

def funzhelp(funz_id):
  result=''
  con = None
  con=openDB(con,'system.db')
  result=select_help_funz(con,funz_id)
  con=closeDB(con)
  return result    

'''
------------------------------------------------------------------------------------------------------------------------
TB_BOT_PKEY
------------------------------------------------------------------------------------------------------------------------
'''
def select_one_pkey(objDB,swName):
  result=''
  r=''
  try:  
    if objDB:
      s="SELECT PKEY_CODE "
      s=s+"FROM TB_BOT_PKEY "
      s=s+"WHERE PKEY_SW like '"+swName+"' "
      s=s+"LIMIT 1"
      
      cur = objDB.cursor() 
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        r=row
        print r
        result=r[0]
        #print row
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result

def insert_pkey(objDB,swName,pKey):
  result=''
  r=''
  try:  
    if objDB:
      s="INSERT INTO TB_BOT_PKEY(PKEY_ID,PKEY_SW,PKEY_CODE) "
      s=s+"VALUES (NULL,'"+swName+"','"+pKey+"')"
      
      cur = objDB.cursor() 
      cur.execute(s)
      objDB.commit()
      result="PKEY inserito:"+swName+" "+pKey
      print result
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result

'''
------------------------------------------------------------------------------------------------------------------------
TB_BOT_TELEGRAMGROUP
------------------------------------------------------------------------------------------------------------------------
'''
def select_one_tgroup(objDB):
  result=''
  r=''
  try:  
    if objDB:
      s="SELECT TG_NAME "
      s=s+"FROM TB_BOT_TELEGRAMGROUP "
      s=s+"ORDER BY RANDOM () "
      s=s+"LIMIT 1"
      
      cur = objDB.cursor() 
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        r=row
        print r
        result=r[0]
        #print row
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result

def insert_tgroup(objDB,tgName):
  result=''
  r=''
  try:  
    if objDB:
      s="INSERT INTO TB_BOT_TELEGRAMGROUP(TG_ID,TG_NAME,TG_TYPE) "
      s=s+"VALUES (NULL,'"+tgName+"','')"
      
      cur = objDB.cursor() 
      cur.execute(s)
      objDB.commit()
      result="GRUPPO inserito:"+tgName
      print result
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result
  
'''
------------------------------------------------------------------------------------------------------------------------
TB_BOT_DIALOG
------------------------------------------------------------------------------------------------------------------------
'''
def select_first_dialog_open(objDB):
  result=''
  r=''
  try:  
    if objDB:
      s="SELECT DIALOG_FILE "
      s=s+"FROM TB_BOT_DIALOG "
      s=s+"WHERE DIALOG_STATE like 'A' "
      s=s+"LIMIT 1"
      
      cur = objDB.cursor() 
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        r=row
        print r
        result=r[0]
        #print row
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result

def insert_dialog(objDB,fn,dn):
  result=''
  r=''
  try:  
    if objDB:
      s="INSERT INTO TB_BOT_DIALOG(DIALOG_FILE,DIALOG_NAME,DIALOG_STATE) "
      s=s+"VALUES ('"+fn+"','"+dn+"','"+"A"+"')"
      
      cur = objDB.cursor() 
      cur.execute(s)
      objDB.commit()
      result="Inserito Dialogo! File:"+fn+" Nome:"+dn
      print result
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result

def update_dialog(objDB,fn):
  result=''
  r=''
  try:  
    if objDB:
      s="UPDATE TB_BOT_DIALOG "
      s=s+"SET DIALOG_STATE = '" +"C"+"' "
      s=s+"WHERE DIALOG_FILE like '" +fn+"' "

      
      cur = objDB.cursor() 
      cur.execute(s)
      objDB.commit()
      result="Chiuso Dialogo! File:"+fn+" Nome:"+dn
      print result
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result
  
'''
------------------------------------------------------------------------------------------------------------------------
TB_BOT_TEMP_CARD
------------------------------------------------------------------------------------------------------------------------
'''
def select_temp_card(objDB):
  result=''
  r=''
  try:  
    if objDB:
      s="SELECT TCARD_NAME "
      s=s+"FROM TB_BOT_TEMP_CARD "
      s=s+"LIMIT 1"
      
      cur = objDB.cursor() 
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        r=row
        print r
        result=r[0]
        #print row
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result

def delete_temp_card(objDB):
  result=''
  r=''
  try:  
    if objDB:
      s="DELETE FROM TB_BOT_TEMP_CARD"
      cur = objDB.cursor() 
      cur.execute(s)
      objDB.commit()
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    pass

def select_list_card(objDB):
  result=''
  r=''
  try:  
    if objDB:
      s="SELECT CARD_NAME "
      s=s+"FROM TB_BOT_CARD "
      cur = objDB.cursor() 
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        r=row
        result=result+'- '+str(r[0])+chr(10)
        #print row
    else:
      print "DB not init!"

  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result        

def insert_card(objDB,chat_id,path,fn):
  result=''
  r=''
  fpath=path+fn+'.png'
  
  try:  
    if objDB:
      s="INSERT INTO TB_BOT_CARD(CARD_ID,CARD_IMG,CARD_NAME,CARD_CODE,CARD_CHAT_ID) "
      s=s+"VALUES ( NULL,'"+fpath+"','"+fn+"','','"+chat_id+"')"      
      cur = objDB.cursor() 
      cur.execute(s)
      objDB.commit()
      result="Carta "+fn+" salvata!"
      print result
    else:
      result="Errore durante registrazione Carta "+fn+" !"
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result  

def select_path_card(objDB,cardName):
  result=''
  r=''
  try:  
    if objDB:
      s="SELECT CARD_IMG "
      s=s+"FROM TB_BOT_CARD "
      s=s+"WHERE CARD_NAME like '"+cardName+"' "
      s=s+"LIMIT 1"
      
      cur = objDB.cursor() 
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        r=row
        print r
        result=r[0]
        #print row
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result  

def insert_temp_card(objDB,cardName):
  result=''
  r=''
  try:  
    if objDB:
      s="INSERT INTO TB_BOT_TEMP_CARD(TCARD_NAME) "
      s=s+"VALUES ('"+cardName+"')"      
      cur = objDB.cursor() 
      cur.execute(s)
      objDB.commit()
      result="Inviami la foto di "+cardName
      print result
    else:
      print "DB not init!"
    
  except lite.Error as e:
    objDB.rollback()
    print "Error:",e
    sys.exit(1)

  finally:
    return result


'''
------------------------------------------------------------------------------------------------------------------------
TB_HOME_COM
------------------------------------------------------------------------------------------------------------------------
'''
def select_last_TB_HOME_COM(objDB):
  r = ''
  try:
    if objDB:

      cur = objDB.cursor()
      cur.execute("SELECT * FROM TB_HOME_COM ORDER BY REQ_ID DESC LIMIT 1;")
      rows = cur.fetchall()
      for row in rows:
        r = row
        # print row

    else:
      print "DB not init!"

  except lite.Error as e:
    objDB.rollback()
    print "Error:", e
    sys.exit(1)

  finally:
    return r

def select_TB_HOME_COM(objDB,REQ_ID):
  r = ''
  try:
    if objDB:
      cur = objDB.cursor()
      s="SELECT * FROM TB_HOME_COM WHERE REQ_ID == "+REQ_ID+";"
      #s = "SELECT * FROM TB_HOME_COM ;"
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        r = row
        # print r    ow
    else:
      print "DB not init!"

  except lite.Error as e:
    objDB.rollback()
    print "Error:", e
    sys.exit(1)

  except Exception as e:
    print "Error:",e

  finally:
    return r

def insert_TB_HOME_COM(objDB, REQ_STRING):
  try:
    if objDB:
      cur = objDB.cursor()
      s = "INSERT INTO TB_HOME_COM (REQ_STRING, REQ_RESULT) VALUES ('" + REQ_STRING + "',''); "
      # print s
      cur.execute(s)
      objDB.commit()
    else:
      print "DB not init!"

  except lite.Error as e:
    objDB.rollback()
    print "Error:", e
    sys.exit(1)


def update_last_TB_HOME_COM(objDB, REQ_ID, REQ_CMD, REQ_RESPONSE, REQ_RESULT):
  result = ''
  r = ''
  try:
    if objDB:
      s = "UPDATE TB_HOME_COM "
      s = s + "SET REQ_RESPONSE = '" + REQ_RESPONSE + "', "
      s = s + "    REQ_RESULT = '" + REQ_RESULT + "' "
      if REQ_CMD !="": s = s + ", REQ_CMD = '" + REQ_CMD + "' "
      s = s + "WHERE REQ_ID = " + REQ_ID + ";"
      cur = objDB.cursor()
      cur.execute(s)
      objDB.commit()
    else:
      print "DB not init!"

  except lite.Error as e:
    objDB.rollback()
    print "Error:", e
    sys.exit(1)

  finally:
    pass

def select_TB_HOME_DIZ_RES(objDB,RES_NODO,RES_VAL):

  result=""
  try:
    if objDB:
      cur = objDB.cursor()
      s="SELECT RES_STR FROM TB_HOME_DIZ_RES "
      s=s+"WHERE ( RES_NODO=="+RES_NODO+" AND RES_VAL=="+RES_VAL+") "
      s=s+"OR ( RES_NODO==5 AND "+RES_NODO+"==5 ) OR ( RES_NODO==6 AND  "+RES_NODO+"==6 );"
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        result  = row[0].replace('%v',RES_VAL)

        # print row
    else:
      print "DB not init!"

  except lite.Error as e:
    objDB.rollback()
    print "Error:", e
    sys.exit(1)

  finally:
    return result

## TB_HOME_DIZ_RES

def select_TB_HOME_DIZ_CMD(objDB,CMD_STR):

  result=""
  try:
    if objDB:
      cur = objDB.cursor()
      s="SELECT CMD_RESULT FROM TB_HOME_DIZ_CMD WHERE CMD_STR=='"+CMD_STR+"';"
      cur.execute(s)
      rows = cur.fetchall()
      for row in rows:
        result  = row[0]
        # print row
    else:
      print "DB not init!"

  except lite.Error as e:
    objDB.rollback()
    print "Error:", e
    sys.exit(1)

  finally:
    return result


####################
###     MAIN     ###
####################


def main():
  con = None
  con=openDB(con,'system.db')
  try:
    print 'DBManager'
    '''
    while 1:
      print '0#SQL VERSION'
      print '4#INSERT TB_NODI'
      print '5#SELECT TB_NODI'
      print '6#DELETE TB_NODI'
      print '7#INSERT TB_HTTP_REQ'
      print '8#SELECT TB_HTTP_REQ'
      print '9#DELETE TB_HTTP_REQ'
      print '10#SELECT LAST TB_HTTP_REQ'
      print '11#INSERT TB_HOME_LOGANDI'
      print '12#SELECT TB_HOME_LOGANDI'
      print '13#DELETE TB_HOME_LOGANDI'
      print '14#SELECT NODO+COMANDO'
      print '15#UPDATE NODO STATO'
      print '16#INSERT TB_HOME_PRESENZE'
      print '17#SELECT TB_HOME_PRESENZE'
      print '18#DELETE TB_HOME_PRESENZE'
      print '19#INSERT TB_TEMPERATURE'
      print '20#SELECT TB_TEMPERATURE'
      print '21#DELETE TB_TEMPERATURE'
      print '22#SHOW ULTIMA PRESENZA'
      print '23#SHOW ULTIMA TEMPERATURA'
      print '24#SHOW ULTIMA UMIDITA'
      print '25#LIV. UTENTE DA CHATID'
      print '26#NOME UTENTE DA CHATID'
      print '27#TESTO DA TB_SYS_TRAD'
      print 'exit#END PROGRAM!'
      c=raw_input('')
      if c=='0':
        printSQLVersion(con)
      elif c=='4':
        nodo_id=raw_input('Inserisci ID nodo: ')
        nodo_nome=raw_input('Inserisci nome nodo: ')
        nodo_desc=raw_input('Inserisci descrizione nodo: ')
        nodo_tipo=raw_input('Inserisci tipo nodo: ')
        nodo_stato=raw_input('Inserisci stato nodo: ')
        insert_TB_NODI(con,nodo_id,nodo_nome,nodo_desc,nodo_tipo,nodo_stato)
      elif c=='5':
        select_TB_NODI(con)
      elif c=='6':
        delete_all_TB_NODI(con)
      elif c=='7':
        nodo_nome=raw_input('Inserisci nome nodo: ')
        nodo_desc=raw_input('Inserisci descrizione nodo: ')
        nodo_tipo=raw_input('Inserisci tipo nodo: ')
        insert_TB_HTTP_REQ(objDB,url,cmd,par)
      elif c=='8':
        select_TB_HTTP_REQ(con)
      elif c=='9':
        pass
      elif c=='10':
        print select_last_TB_HTTP_REQ(con)
      elif c=='11':
        com_nome=raw_input('Inserisci nome comando: ')
        com_value=raw_input('Inserisci valore comando: ')
        com_tipo=raw_input('Inserisci tipo comando: ')
        insert_TB_HOME_LOGANDI(con,com_nome,com_value,com_tipo)
      elif c=='12':
        select_TB_HOME_LOGANDI(con)
      elif c=='13':
        delete_all_TB_HOME_LOGANDI(con)
      elif c=='14':
        nodo_nome=raw_input('Inserisci nome nodo: ')
        com_nome=raw_input('Inserisci nome comando: ')
        print select_NODO_COM(con,nodo_nome,com_nome)
      elif c=='15':
        nodo_nome=raw_input('Inserisci nome nodo: ')
        nodo_stato=raw_input('Inserisci stato nodo: ')
        update_TB_NODI(con,nodo_nome,nodo_stato)
      elif c=='16':
        insert_TB_HOME_PRESENZE(con)
      elif c=='17':
        select_TB_HOME_PRESENZE(con)
      elif c=='18':
        delete_all_TB_HOME_PRESENZE(con)
      elif c=='19':
        temp_tipo=raw_input('Inserisci tipo temp: ')
        temp_value=raw_input('Inserisci valore temp: ')
        insert_TB_TEMPERATURE(con,temp_tipo,temp_value)
      elif c=='20':
        select_TB_TEMPERATURE(con)
      elif c=='21':
        delete_all_TB_TEMPERATURE(con)
      elif c=='22':        
        print select_last_TB_HOME_PRESENZE(con)
      elif c=='23':
        print select_last_temp_TB_TEMPERATURE(con)
      elif c=='24':
        print select_last_hum_TB_TEMPERATURE(con)        
      elif c=='25':
        chat_id=raw_input('Inserisci chat_id: ')
        print select_user_level_from_chatid(con,chat_id)
      elif c=='26':
        chat_id=raw_input('Inserisci chat_id: ')
        print select_user_name_from_chatid(con,chat_id)         
      elif c=='27':
        trad_id=raw_input('Inserisci trad_id: ')
        print select_trad(con,trad_id)         

      elif c=='exit':
        break
      '''
  except:
    print 'Error!',sys.exc_info ()[0], sys.exc_info ()[1]
    
  finally:  
    con=closeDB(con)
  
          
if __name__ == '__main__':
    main()


