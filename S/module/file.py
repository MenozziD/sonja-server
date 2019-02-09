# -*- coding: utf-8 -*-

from GreyMatter.voice.speak import speak
import random
import datetime
import time
import os.path

def test():
  mex='/home/pi/Desktop/BotSonja/GreyMatter/test.txt'
  if os.path.isfile(mex):
   # file exists
   mex='!F'+mex
  else:
   mex='Non ho trovato: '+mex
  return mex

def file_da_path(path):
  mex=''
  print 'File Begin'
  tmp=path.split(" ")
  if len(tmp)==3:
   path=tmp[2] 
   mex=''
   if os.path.isfile(path):
    # file exists
    mex='!F'+path
   else:
    mex='Non ho trovato: '+path
  else:
   mex='Mi devi dire il percorso del file!'
  return mex
