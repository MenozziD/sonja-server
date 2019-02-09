# -*- coding: utf-8 -*-

from GreyMatter.voice.speak import speak
import random
import datetime
import time
from GreyMatter.db import DB_Manager


def start():
  mex=DB_Manager.dbtext("TEXT_002")
  mex=mex+chr(10)
  mex=mex+DB_Manager.dbtext("TEXT_001")
  return mex

def cosa_sai_fare():
  mex=DB_Manager.dbtext("TEXT_004")
  mex=mex+chr(10)
  mex=mex+DB_Manager.funzlist()
  mex=mex+DB_Manager.dbtext("TEXT_003")
  return mex

def help_cmd(funz_id):
  mex=DB_Manager.funzhelp(funz_id)
  return mex

def grazie():
  mex=['Grazie','Grazie mille','Grazie!Cosa posso fare per te?']
  return random.choice(mex)

def saluto(chat_id):
  db=None
  result=''
  mex=['Ciao','Bella']
  db=DB_Manager.openDB(db,'system.db')
  r=DB_Manager.select_user_name_from_chatid(db,chat_id)
  if r!='':
    if r[0]!='':
      #print r[0]
      result=' '+r[0]
  db=DB_Manager.closeDB(db)
  
  result=random.choice(mex)+result
  return result

def saluto_sample():
  mex=['Ciao','Bella','Uè']
  return random.choice(mex)

def chi_sei():
  mex=['Sono Sonja, la tua fantastica assistente!','Sono la Sò non te lo ho detto prima?','Quante volte vuoi chiedermelo? Sono la Sò']
  #print mex
  return random.choice(mex)
  #speak(random.choice(mex))

def non_ho_capito():
  mex=['Non ho capito!','Puoi ripetere?','Scusa non ho capito']
  #print mex
  return random.choice(mex)
  #speak(random.choice(mex))
  
def saluta_so():
  mex=['Ciao Amore mio fantastico','Ciao Luce dei miei occhi','Buongiorno stella bella']
  #print mex
  return random.choice(mex)  
  #speak(random.choice(mex))

def saluta_sga():
  mex=['Bella Sga','Ciao Sgarzo','Salve Ingegnere']
  return random.choice(mex)
  #speak(random.choice(mex))

def che_ore_sono():
  #mex= "Sono le "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  mex= "Sono le "+datetime.datetime.now().strftime("%H:%M")
  return mex
  #speak(mex)

def che_giorno_e():
  #mex= "Sono le "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  mex= "è il "+datetime.datetime.now().strftime("%Y-%m-%d")
  return mex
  #speak(mex)

def ci_sei():
  mex=['Eccomi','Si ci sono','Si dimmi tutto']
  return random.choice(mex)

def barzelletta():
  mex=['Pierino, dove vivevano gli antichi Galli? Negli antichi pollai',
       'Quale è il colmo per un matematico? Trovare la sua dolce metà nelle mani di un terzo',
       'Quale è il colmo per un computer? Non avere un programma per la serata',
       'Cosa fa un uccellino dentro un compiuter? Micro-cip'
       ]
  suffix=[' ',
           'a a a a  a a a a  a a a a ',
          ]
           #'Quanto sono spiritosa!',
           #'Che Battutone',
           #' '
          #]
  mex=random.choice(mex)+'.'+random.choice(suffix)
  #print mex
  #speak(random.choice(mex))
  #time.sleep(1)
  #speak(random.choice(suffix))
  return mex
  
