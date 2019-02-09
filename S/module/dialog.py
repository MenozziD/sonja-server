# -*- coding: utf-8 -*-

from GreyMatter.voice.speak import speak
import random
import datetime
import time
from GreyMatter.db import DB_Manager


def inizio_discorso():
  result=''
  db=None 
  fn=crea_dialog()
  try:
    db=DB_Manager.openDB(db,'system.db')
    r=DB_Manager.insert_dialog(db,fn,'')
    mex="Inizio discorso "+fn
    result= mex
      
  except Exception as e:
    print "Error:",e
    result="Errore durante creazione discorso"

  finally:
    db=DB_Manager.closeDB(db)
    return result
  

def crea_dialog():
  dt=datetime.datetime.now()
  nf='{:%B_%d_%Y_%H_%M_%S}'.format(dt)
  mex="# INIZIO DISCORSO #"
  path="/home/pi/Desktop/BotSonja/dialog/"
  f=open(path+'conv_'+str(nf)+'.txt','w')
  f.write(mex)
  f.close()
  return 'conv_'+str(nf)

def scrivi_dialog(nf,txt):
  mex=txt
  path="/home/pi/Desktop/BotSonja/dialog/"
  f=open(path+str(nf)+'.txt','a')
  f.write(mex)
  f.close()

def chiudi_discorso():
  result=''
  db=None
  fn=return_dialog_open()
  try:
    db=DB_Manager.openDB(db,'system.db')
    r=DB_Manager.update_dialog(db,fn)
    mex="Chiudo discorso "+fn
    result= mex
      
  except Exception as e:
    print "Error:",e
    result="Errore durante creazione discorso"

  finally:
    db=DB_Manager.closeDB(db)
    return result
  
  
  

def return_dialog_open():
  result=''
  db=None  
  try:
    db=DB_Manager.openDB(db,'system.db')
    r=DB_Manager.select_first_dialog_open(db)
    if r != '' :
      result=str(r)
      
  except Exception as e:
    print "Error:",e        
  finally:
    db=DB_Manager.closeDB(db)
    return result
