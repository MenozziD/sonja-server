#!/usr/bin/python
# -*- coding: utf-8 -*-

from GreyMatter.db import DB_Manager
from GreyMatter.memory import memory

def return_card_open():
    result = ''
    db = None
    try:
        db = DB_Manager.openDB(db, 'system.db')
        r = DB_Manager.select_temp_card(db)
        if r != '':
            result = str(r)

    except Exception as e:
        print "Error:", e
    finally:
        db = DB_Manager.closeDB(db)
        return result


def close_card_open(chat_id, path, nf):
    result = ''
    db = None
    try:
        db = DB_Manager.openDB(db, 'system.db')
        DB_Manager.delete_temp_card(db)
        result = DB_Manager.insert_card(db, chat_id, path, nf)

    except Exception as e:
        print "Error:", e
    finally:
        db = DB_Manager.closeDB(db)
        return result


def addCard(cardName):
    result = ''
    db = None
    try:
        db = DB_Manager.openDB(db, 'system.db')
        r = DB_Manager.insert_temp_card(db, cardName)
        if r != '':
            result = str(r)
        else:
            # result=result+' '+cardName
            result = 'Errore durante registrazione carta ' + cardName

    except Exception as e:
        print "Error:", e
    finally:
        db = DB_Manager.closeDB(db)
        return result


def getCardList():
    result = ''
    db = None
    try:
        db = DB_Manager.openDB(db, 'system.db')
        r = DB_Manager.select_list_card(db)
        if r != '':
            result = r
        result = 'Elenco Carte:' + chr(10) + result

    except Exception as e:
        print "Error:", e
    finally:
        db = DB_Manager.closeDB(db)
        return result


def getCard(cardName):
    result = ''
    db = None
    try:
        db = DB_Manager.openDB(db, 'system.db')
        r = DB_Manager.select_path_card(db, cardName)
        if r != '':
            result = "!F" + str(r)
        else:
            result = 'Non ho trovato nessuna Card per ' + cardName

    except Exception as e:
        print "Error:", e
    finally:
        db = DB_Manager.closeDB(db)
        return result