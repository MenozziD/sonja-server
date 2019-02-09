#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


def getMangaPath():
    return str(os.path.dirname(os.path.abspath(__file__)))+"/manga/"

def getDialogPath():
    return str(os.path.dirname(os.path.abspath(__file__)))+"/dialog/"

def getCardPath():
    return str(os.path.dirname(os.path.abspath(__file__)))+"/card/"

def getYoutubePath():
    return str(os.path.dirname(os.path.abspath(__file__)))+"/youtube/"

