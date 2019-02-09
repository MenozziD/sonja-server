# -*- coding: utf-8 -*-
#sudo apt-get install ffmpeg
#ydl.download(['https://www.youtube.com/watch?v=-vphKEmAK5s'])
from __future__ import unicode_literals
from random import randint
from GreyMatter.memory import memory
import youtube_dl
from os import system
import logging


#'outtmpl': '/home/pi/Desktop/BotSonja/media/s_%(title)s-%(id)s.%(ext)s',

def youtube_cmd(url):
  logging.basicConfig(filename='example.log',level=logging.DEBUG)
  result=''
  #home='/home/pi/Desktop/BotSonja/media/'
  home=memory.getYoutubePath()
  req_id=randint(0,9)
  system("rm " + home + "*.wav")
  system("rm " + home + "*.mp3")
  system("rm " + home + "*.txt")
  print url
  if url != '':    
    try:
      ydl_opts = {
          'outtmpl': home+'s_%(id)s.%(ext)s',
          'format': 'bestaudio/best',
          'postprocessors': [{
              'key': 'FFmpegExtractAudio',
              'preferredcodec': 'wav',              
              'preferredquality': '192',
          }],
      }
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          ydl.download([url])
      system("ls " + home + "*.wav  > " + home + "tmp.txt")
      try:
        f = open(home + "tmp.txt","r")
        target=f.readline()
        if target!="":
         system("lame " + target[:-1] + " " + target[:-4] + "mp3")
         result="!S"+ target[:-4] + "mp3"
         logging.info(result)

      except Exception as e:
        print "Error:",e
        result='Scusa ma si è verificato un problema durante upload!'
      
    except Exception as e:
      print "Error:",e
      result='Scusa ma si è verificato un problema durante download!'
  else:
    result='URL Vuoto o non valido!'
  return result  


def main():
  logging.basicConfig(filename='example.log',level=logging.DEBUG)
  youtube_cmd("youtube https://www.youtube.com/watch?v=vrpJB7ucC5Y")

if __name__ == '__main__':main()
    
