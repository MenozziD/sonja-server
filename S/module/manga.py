#!/usr/bin/python
# -*- coding: utf-8 -*-

 
import urllib2
import sys
import ssl
from fpdf import FPDF
from PIL import Image
from GreyMatter.memory import memory


# variabili INPUT
cap=''
pag=''
ipag=1
# variabili URL
#http://www.mangaeden.com/it/it-manga/one-piece/863/1/
base='http://www.mangaeden.com/it/it-manga/'
url=''
end=0
imgurl=''
#sdir="/home/pi/Desktop/BotSonja/manga/"
sdir=memory.getMangaPath()


def makePdf(pdfFileName, listPages, dir = ''):
    #if (dir):
    #    dir += "/"
    max_w=0
    max_h=0
    
    for page in listPages:
        p=Image.open(dir + str(page) + ".jpg")
        width, height = p.size
        if width > max_w :
            max_w=width            
        if height > max_h :
            max_h=height
        

    print dir + str(listPages[0]) + ".jpg"
    cover = Image.open(dir + str(listPages[0]) + ".jpg")
    width, height = cover.size

    pdf = FPDF(orientation = "L" ,unit = "mm",format = [max_w, max_h])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) + ".jpg", 0, 0)

    pdf.output(pdfFileName, "F")



def defineParam(cap,pag,base,manga):
  result=''
  pag='/1/'
  if manga!='': 
    if cap!='':
      result=base+manga+'/'+cap+pag
    else:
      print 'Capitolo mancante'
  else:
    print 'Titolo manga mancante'
  return result

def modUrl(cap,pag,base,manga):
 return base+manga+'/'+cap+'/'+str(pag)+'/'


def downloadImage(imgurl,ipag):
  path=memory.getMangaPath()
  ctx=ssl._create_unverified_context()
  respIMG=urllib2.urlopen(imgurl,context=ctx)
  c=respIMG.read()
  print 'ok'
  f=open(path+'pag_'+str(ipag)+'.jpg','w')
  f.write(c)
  f.close()
  path_f=path+'pag_'+str(ipag)+'.jpg'
  Image.open(path_f).convert('RGB').save(path_f)
  photo = Image.open(path_f)
  #photo.paste("black",(100,100,200,200))
  photo.save(path_f)
  photo.close()

def manga_command(manga,cap):
  #tmp=mex.split(" ")
  result="Manga Error"
  ipag=1
  end=0
  oldurl=''
  ctx=ssl._create_unverified_context()
  url=defineParam(cap,pag,base,manga)
  if url != '':
    while (end==0):
     try:
      #if ipag>30:    
      # r=raw_input('Interrompere?(s/n')
      #if r=='s':
      # break
      print '_1:URL PAGE OPEN '+str(ipag)
      url=modUrl(cap,ipag,base,manga)
      print '_1: '+url
      respHTML=urllib2.urlopen(url,context=ctx)
      print '_2:URL IMAGE READ'+str(ipag)
      c=''
      c=respHTML.read()
      if c=='':
       end=1
      respHTML.close()
      #print c
      pos1=c.find('<meta property='+chr(34)+'og:image'+chr(34))
      if c.find('.jpg'+chr(34)+'>')>-1:
        pos2=c.find('.jpg'+chr(34)+'>')
      elif c.find('.png'+chr(34)+'>')>-1:
        pos2=c.find('.png'+chr(34)+'>')
      pos3=c.find('http:',pos1)
      print "pos1: "+str(pos1)
      print "pos2: "+str(pos2)
      print "pos3: "+str(pos3)
      imgurl= c[pos3:pos2+4]
      print '_2:FILE WRITE'+str(ipag)
      if oldurl != imgurl:
        downloadImage(imgurl,ipag)
        oldurl=imgurl
      else:
        print 'Trovata fine capitolo'
        break
      
      ipag=ipag+1
     except:
      end=-1
      print 'Error!',sys.exc_info ()[0], sys.exc_info ()[1]
    
    sdir=memory.getMangaPath()
    titolo=sdir+manga+"_"+cap+".pdf"
    listPages=[]
    print ipag
    for i in range (1,ipag):
      listPages.append('pag_'+str(i))
  
    makePdf(titolo, listPages,sdir)
    result= "!F"+titolo
  else:
    result="Errore Download Manga"
  return result
