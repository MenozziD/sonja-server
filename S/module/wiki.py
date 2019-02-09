# -*- coding: utf-8 -*-
 
import re
import wikipedia
#import wikipediaapi

def definizione_subject_2(mex):
  mex_words=mex.split()
  mex_words.remove('definizione')
  x=' '.join(mex_words)
  wiki_data=''
  try:
    wiki_data=wikipedia.summary(x,sentences=5)
    regEx=re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
    m=regEx.match(wiki_data)
    while m:
      wiki_data=m.group(1)+m.group(2)
      m=regEx.match(wiki_data)

    #wiki_data=wiki_data.replace("'","")
  except wikipedia.exceptions.DisambiguationError as e:
    wiki_data='Puoi essere più preciso?'
    
  return wiki_data
  
def wiki_subject(mex):
  result=''
  l=0
  f=0
  try:
    wiki_data=''
    try:
      wikipedia.set_lang("it")
      page=wikipedia.page(mex)
      wiki_data=page.content
      #wiki_data=wiki_data.replace("'","")+page.url
      f=wiki_data.find(".")
      result=wiki_data[:f].encode('UTF8')+'.'+chr(10)+str(page.url)
      '''
      if l==1:
        f1=wiki_data.find(".")
        f=wiki_data[f1:].find(".")
        result=wiki_data[:f].encode('UTF8')
      else:
        f=wiki_data.find(".")
        result=wiki_data[:f].encode('UTF8')
      '''  
    
    except wikipedia.exceptions.DisambiguationError as e:
      result='Puoi essere più preciso ?'
    
    except Exception as e:
      print "Error:",e
      result='Scusa ma non riesco a pronunciare il risultato.'
      
  except Exception as e:
    print "Error:",e
    result='Scusa ho avuto un problema!'

  if result=='':
    result="Non ho trovato risultati per "+x


  return result


