# -*- coding: utf-8 -*-
#from GreyMatter.voice.speak import speak
from GreyMatter.module import general, card, dialog, home, manga, util, wiki, youtube, math

comandi = {
  '/ciao' : general.saluto_sample,
  '/check' : general.ci_sei,
  '/wiki' : wiki.wiki_subject,
  '/youtube' : youtube.youtube_cmd,
  '/barzelletta' :  general.barzelletta,
  '/data': general.che_giorno_e,
  '/ora': general.che_ore_sono,
  '/manga': manga.manga_command,
  '/math': math.exeOperation,
  '/pkey': util.getPKey,
  '/pkey_add': util.addPKey,
  '/tgroup': util.getTGroup,
  '/tgroup_add': util.addTGroup,
  '/home': home.attiva_sistema_casa,
  '/home_lampada_com': home.comando_luce,
  '/home_lampada': home.comando_luce_stato,
  '/home_temperatura': home.comando_temperatura,
  '/home_umidita': home.comando_umidita,
  '/home_tv': home.comando_tv,
  '/home_chp': home.comando_tv,
  '/home_chm': home.comando_tv,
  '/home_volp': home.comando_tv,
  '/home_volm': home.comando_tv,
  '/home_pir_stato': home.comando_pir_stato,
  '/home_pir_on': home.comando_pir_on,
  '/home_pir_off': home.comando_pir_off,
  '/home_buzz_on': home.comando_pir_buzz_on,
  '/home_buzz_off': home.comando_pir_buzz_off,
  '/home_r1_com': home.comando_r1_com,
  '/home_r1_stato': home.comando_r1_stato,
  '/home_r2_com': home.comando_r2_com,
  '/home_r2_stato': home.comando_r2_stato,
  '/home_r3_com': home.comando_r3_com,
  '/home_r3_stato': home.comando_r3_stato,
  '/home_r4_com': home.comando_r4_com,
  '/home_r4_stato': home.comando_r4_stato,
  '/home_r5_com': home.comando_r5_com,
  '/home_r5_stato': home.comando_r5_stato,
  '/home_r6_com': home.comando_r6_com,
  '/home_r6_stato': home.comando_r6_stato,
  '/card_add': card.addCard,
  '/card': card.getCard,
  '/card_list': card.getCardList,
  '/cards': card.getCardList,
  '/trad_en': util.trad_EN,
  '/trad_it': util.trad_IT,
  '/trad_es': util.trad_ES,
  '/trad_de': util.trad_DE,
  '/trad_ru': util.trad_RU,
  '/trad_ja': util.trad_JA
}

#'0'=0 parametri
#'1'=1 parametro
#'2'=2 parametri
#'n'=1 parametro con spazi es:/wiki Nuova Zelanda
#'x'=chat_id Telegram come parametro
parametri={
  '/ciao' : '0',
  '/check' : '0',
  '/wiki':'n',
  '/youtube':'1',
  '/barzelletta': '0',
  '/data':'0',
  '/ora':'0',
  '/manga':'2',
  '/math':'1',
  '/pkey':'1',
  '/pkey_add':'2',
  '/tgroup':'0',
  '/tgroup_add':'1',
  '/home':'x',
  '/home_lampada_com':'x',
  '/home_lampada':'x',
  '/home_temperatura':'x',
  '/home_umidita':'x',
  '/home_tv':'x',
  '/home_chp':'x',
  '/home_chm':'x',
  '/home_volp':'x',
  '/home_volm':'x',
  '/home_pir_stato':'x',
  '/home_pir_on':'x',
  '/home_pir_off':'x',
  '/home_buzz_on':'x',
  '/home_buzz_off':'x',
  '/home_r1_com': 'x',
  '/home_r1_stato': 'x',
  '/home_r2_com': 'x',
  '/home_r2_stato': 'x',
  '/home_r3_com': 'x',
  '/home_r3_stato': 'x',
  '/home_r4_com': 'x',
  '/home_r4_stato': 'x',
  '/home_r5_com': 'x',
  '/home_r5_stato': 'x',
  '/home_r6_com': 'x',
  '/home_r6_stato': 'x',
  '/card_add':'1',
  '/card':'1',
  '/card_list':'0',
  '/cards':'0',
  '/trad_en':'n',
  '/trad_it':'n',
  '/trad_es':'n',
  '/trad_de':'n',
  '/trad_ru':'n',
  '/trad_ja':'n'
}

def brain_bot(mex,chat_id):
  result=''
  s=''
  l=''
  print 'CHAT ID:'+chat_id
  print 'MEX:'+mex
  mex_split=mex.split()
  #print 'PAR:'+parametri[mex_split[0]]
  if len(mex_split)>0:
    if comandi.has_key(mex_split[0])==True:
      if parametri[mex_split[0]]=='0':
          result=comandi[mex_split[0]]()
      elif parametri[mex_split[0]]=='1':
        if len(mex_split)==2:
          result=comandi[mex_split[0]](mex_split[1])
        else:
          result='Manca parametro'
      elif parametri[mex_split[0]]=='2':
        if len(mex_split)==3:
          result=comandi[mex_split[0]](mex_split[1],mex_split[2])
        else:
          result='Mancano parametri'
      elif parametri[mex_split[0]]=='n':
        if len(mex_split)>1:
          l=mex_split[1:] 
          s=' '.join(l)
          result=comandi[mex_split[0]](s)
        else:
          result='Mancano parametri'
      elif parametri[mex_split[0]]=='x':
          result=home.home_request(chat_id,mex)
          #result=comandi[mex_split[0]](chat_id)
    else:
      result='Comando non valido'
  else:
    result='Messaggio non valido'
  if result=='':
    result="Non ho una risposta x_x'"
  print 'RISP:'+result
  return result
  

def update_presenze():
  result=''
  result= home.check_presenze()
  return result

def card_open():
  result=''
  nf=''
  nf= card.return_card_open()
  if nf != '' :
    result=nf    
  return result  

def card_close(chat_id,path,nf):
  result=''
  result= card.close_card_open(chat_id, path, nf)
  return result  
  

def check_dialog_open(usr_txt,bot_txt):
  result=''
  mex=''
  nf= dialog.return_dialog_open()
  if nf != '' :
    mex="# User:"+chr(10)
    mex=mex+usr_txt+chr(10)
    mex="# Bot:"+chr(10)
    mex=mex+bot_txt+chr(10)
    dialog.scrivi_dialog(nf, mex)
  

def found_superuser_key(speech):

  pos=speech.find("sonia")
  return pos

def check_mex(speech,check):
  words_of_message=speech.split()
  if set(check).issubset(set(words_of_message)):
    return True
  else:
    return False
    
'''
def brain_bot(mex,chat_id):
  r=''
  su=False
  #VERIFICO SU
  if found_superuser_key(mex)>-1:
    su=True

  comandi[mex] 
  #HELP  
  if check_mex(mex,['?']):
    l=mex.split(" ")
    if len(l)==2:
      print 'HELP! '+l[0] 
      r=general_conversation.help_cmd(l[0])
      return r
      

    
  # FILE
  if check_mex(mex,['file','test']):
    r=file_conversation.test()
  elif check_mex(mex,['file','in']):
    r=file_conversation.file_da_path(mex)
    
  mex=mex.lower()


  
  # GENERAL
  if check_mex(mex,['/start']) :
    r=general_conversation.start
  elif check_mex(mex,['cosa','sai','fare?']) or check_mex(mex,['cosa','sai','fare']):
    r= general_conversation.cosa_sai_fare()
  # DIALOGO
  elif check_mex(mex,['inizio','discorso']):
    r= dialog_conversation.inizio_discorso()
  elif check_mex(mex,['chiudi','discorso']):
    r= dialog_conversation.chiudi_discorso()
 
      

    
  if r== '':
    r=general_conversation.non_ho_capito()

  check_dialog_open(mex,r) 
  
  
  #speak(r)
  return r
'''

