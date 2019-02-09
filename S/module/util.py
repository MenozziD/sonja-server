# -*- coding: utf-8 -*-

from GreyMatter.db import DB_Manager
import random
from googletrans import Translator

def trad_EN(mex):
  result=''
  translator = Translator()
  t=translator.translate(mex, dest='en')
  if t!='':
    result=t.text
  else:
    result="Nessuna traduzione per "+mex
  return result

def trad_IT(mex):
  result=''
  translator = Translator()
  t=translator.translate(mex, dest='it')
  if t!='':
    result=t.text
  else:
    result="Nessuna traduzione per "+mex
  return result

def trad_ES(mex):
  result=''
  translator = Translator()
  t=translator.translate(mex, dest='es')
  if t!='':
    result=t.text
  else:
    result="Nessuna traduzione per "+mex
  return result

def trad_DE(mex):
  result=''
  translator = Translator()
  t=translator.translate(mex, dest='de')
  if t!='':
    result=t.text
  else:
    result="Nessuna traduzione per "+mex
  return result

def trad_RU(mex):
  result=''
  translator = Translator()
  t=translator.translate(mex,dest='ru')
  if t!='':
    result=t.text
  else:
    result="Nessuna traduzione per "+mex
  return result

def trad_JA(mex):
  result=''
  translator = Translator()
  t=translator.translate(mex,dest='ja')
  if t!='':
    result=t.text
  else:
    result="Nessuna traduzione per "+mex
  return result  
  
def getPKey(swName):
  result=''
  db=None
  try:
    db=DB_Manager.openDB(db,'system.db')
    r=DB_Manager.select_one_pkey(db,swName)
    if r != '' :
      result=str(r)
    else:
      result='Non ho trovato nessun Product Key per '+swName
      
  except Exception as e:
    print "Error:",e        
  finally:
    db=DB_Manager.closeDB(db)
    return result  

def addPKey(swName,pKey):
  result=''
  db=None
  try:
    db=DB_Manager.openDB(db,'system.db')
    r=DB_Manager.insert_pkey(db,swName,pKey)
    if r != '' :
      result=str(r)
    else:
      result=result+' '+swName
      
  except Exception as e:
    print "Error:",e        
  finally:
    db=DB_Manager.closeDB(db)
    return result  

def getTGroup():
  result=''
  db=None
  try:
    db=DB_Manager.openDB(db,'system.db')
    r=DB_Manager.select_one_tgroup(db)
    if r != '' :
      result=str(r)
    else:
      result='Non ho trovato nessun Product Key per '+tgName
      
  except Exception as e:
    print "Error:",e        
  finally:
    db=DB_Manager.closeDB(db)
    return result  

def addTGroup(tgName):
  result=''
  db=None
  try:
    db=DB_Manager.openDB(db,'system.db')
    r=DB_Manager.insert_tgroup(db,tgName)
    if r != '' :
      result=str(r)
    else:
      result=result+' '+tgName
      
  except Exception as e:
    print "Error:",e        
  finally:
    db=DB_Manager.closeDB(db)
    return result
  
