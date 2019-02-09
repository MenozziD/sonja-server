# -*- coding: utf-8 -*-

from GreyMatter.db import DB_Manager
import random
import datetime
import time
from os import system
import os.path


def auth_permission(chat_id):
  result=False
  liv=''
  db=None
  try:
    db=DB_Manager.openDB(db,'system.db')
    r=DB_Manager.select_user_level_from_chatid(db,chat_id)
    if r != '' :
      liv=str(r[0])
      if liv=='10':
        result=True
  except Exception as e:
    print "Sub:auth_permission Error:",e
  finally:
    db=DB_Manager.closeDB(db)
    return result    

    
def home_request_app(cmd):
    result = ""
    r = ''
    db = None
    try:
      db = DB_Manager.openDB(db, 'system.db')
      DB_Manager.insert_TB_HOME_COM(db, cmd)
      r=DB_Manager.select_last_TB_HOME_COM(db)
      if int(r[0]) > 0:
        time.sleep(3)
        result=DB_Manager.select_TB_HOME_COM(db,str(r[0]))
        if result !="":
          result=result[4]
    except Exception as e:
      print "Sub:home_request Error:", e
    finally:
      DB_Manager.closeDB(db)
      return result



def home_request(chat_id,cmd):
    result = ""
    r = ''
    db = None
    try:
      if auth_permission(chat_id) == True and chat_id != '':
        db = DB_Manager.openDB(db, 'system.db')
        DB_Manager.insert_TB_HOME_COM(db, cmd)
        r=DB_Manager.select_last_TB_HOME_COM(db)
        if int(r[0]) > 0:
          time.sleep(3)
          result=DB_Manager.select_TB_HOME_COM(db,str(r[0]))
          if result !="":
            result=result[4]
      else:
        result = "Non hai l'autorizzazione per questo genere di comandi!"
    except Exception as e:
      print "Sub:home_request Error:", e
    finally:
      DB_Manager.closeDB(db)
      return result


def attiva_sistema_casa(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(BASE_DIR, 'run_com.sh &')
    print str(script_path)
    system(script_path)
    res=speakResult("","Avvio il sistema di controllo della camera")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def check_presenze():
  result=""
  db=None
  try:
    db=DB_Manager.openDB(db,'system.db')
    r=DB_Manager.select_last_TB_HOME_PRESENZE(db)
    #print r
    if r != '' :
      result="Rilevata presenza in camera!"
      result=result+chr(10)+"DATA: "+r
      DB_Manager.update_last_TB_PRESENZE(db)
      

  except Exception as e:
    print "Sub:check_presenze Error:",e
    result='Scusa ho dei problemi a comunicare con il database!'

  finally:
    db=DB_Manager.closeDB(db)
    return result  

##### LUCE #####

def comando_luce_stato(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=home_request()
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_luce(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("luce on","luce","on")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"    
  return res

##### PIR #####
def comando_pir_stato(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("pir stato","pir","stato")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_pir_off(chat_id):
  res=''
  if auth_permission(chat_id)==True:  
    res=send_cmd("pir pir_off","pir","pir_off")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"  
  return res

def comando_pir_buzz_on(chat_id):
  res=''
  if auth_permission(chat_id)==True:  
    res=send_cmd("pir buzz_on","pir","buzz_on")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"  
  return res

def comando_pir_buzz_off(chat_id):
  res=''
  if auth_permission(chat_id)==True:  
    res=send_cmd("pir buzz_off","pir","buzz_off")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"  
  return res

def comando_pir_on(chat_id):
  res=''
  if auth_permission(chat_id)==True:  
    res=send_cmd("pir pir_on","pir","pir_on")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"  
  return res

##### TV #####
def comando_temperatura(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("tv temp","tv","temp")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res
   
def comando_umidita(chat_id):
  res=''
  if auth_permission(chat_id)==True:  
    res=send_cmd("tv hum","tv","hum")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"    
  return res

def comando_tv(chat_id):
  res=''
  if auth_permission(chat_id)==True:  
    res=send_cmd("tv pow","tv","pow")
    res='Invio comando POW a TV'
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"        
  return res

def comando_tv_volp(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("tv volp","tv","volp")
    res='Invio comando VOL + a TV'
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_tv_volm(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("tv volm","tv","volm")
    res='Invio comando VOL - a TV'
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res


##### RELE #####
def comando_r1_com(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("rele r1_com","rele","r1_com")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_r1_stato(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("rele r1_stato","rele","r1_stato")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_r2_com(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("rele r2_com","rele","r2_com")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_r2_stato(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("rele r2_stato","rele","r2_stato")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_r3_com(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("rele r3_com","rele","r3_com")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_r3_stato(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("rele r3_stato","rele","r3_stato")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_r4_com(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("rele r4_com","rele","r4_com")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_r4_stato(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("rele r4_stato","rele","r4_stato")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_r5_com(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("rele r5_com","rele","r5_com")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_r5_stato(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("rele r5_stato","rele","r5_stato")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_r6_com(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("rele r6_com","rele","r6_com")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res

def comando_r6_stato(chat_id):
  res=''
  if auth_permission(chat_id)==True:
    res=send_cmd("rele r6_stato","rele","r6_stato")
  else:
    res="Non hai l'autorizzazione per questo genere di comandi!"
  return res
