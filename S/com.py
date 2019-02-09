from module import dbmanager
import serial
import sys
import os
import time
import string


class ClassCOM():
    COM_BUFF_TX = ''    # Buffer trasmesso
    COM_BUFF_RX = ''    # Buffer ricevuto
    ser = None
    COM_READ = 0
    LAST_REQ_ID = 0
    RES_REQ_ID = 0
    firs_time = 1
    db = None


    def setCOM_BUFF_TX(self, cmd):
        self.COM_BUFF_TX = cmd

    def getCOM_BUFF_RX(self):
        s = self.COM_BUFF_RX
        self.COM_BUFF_RX = ''
        return s

    def ComOpen(self):

        Result = ''
        try:
            self.ser = serial.Serial(
                port='/dev/ttyUSB0',
                baudrate=57600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
            )
            #self.ser.timeout = 0
            if not self.ser.isOpen():
                self.ser.open()
                self.ser.flushInput()
                self.ser.flushOutput()
                print 'COM: ' + port + ' OPEN!'

        except Exception as e:
            print "Error:", e

    def run(self):
        out=""
        try:
            self.db = dbmanager.openDB(self.db,str(os.path.dirname(os.path.abspath(__file__)))+"/db/", 'system.db')
            while 1:
                if self.ser.isOpen():

                    out = ""
                    mex=""
                    while self.ser.inWaiting() > 0:
                        out = self.ser.readline()
                    out = ''.join(ch for ch in str(out) if ch.isalnum())
                    if out != "":
                        # HOME
                        mex=dbmanager.select_TB_HOME_DIZ_RES(self.db,str(int(out) / 100),str(int(out) % 100))
                        dbmanager.update_last_TB_HOME_COM(self.db, str(self.LAST_REQ_ID),"", out,mex)
                        print  '<<' + out
                        print mex
                        # HOME
                        if self.RES_REQ_ID != self.LAST_REQ_ID:
                            self.RES_REQ_ID=self.LAST_REQ_ID

                    r = dbmanager.select_last_TB_HOME_COM(self.db)

                    # print "Leggo richiesta numero "+str(r[0])
                    if r != '':
                        if not int(r[0]) == self.LAST_REQ_ID:
                            if self.LAST_REQ_ID != 0:
                                #print "Leggo richiesta numero " + str(r[0]) + " " + str(r[1])
                                self.firs_time = 0

                            self.LAST_REQ_ID = int(r[0])
                            # print r[0],type(r[0]),r[2],type(r[2]),r[3],type(r[3])
                            self.COM_BUFF_TX = dbmanager.select_TB_HOME_DIZ_CMD(self.db,str(r[1]).strip())
                            # self.COM_BUFF_TX =''.join(ch for ch in str(r[1]) if ch.isalnum())

                    if self.COM_BUFF_TX != '' and self.ser.isOpen() and self.firs_time == 0 :
                        dbmanager.update_last_TB_HOME_COM(self.db, str(self.LAST_REQ_ID),self.COM_BUFF_TX, "", "")
                        print '>>' + self.COM_BUFF_TX
                        self.COM_BUFF_TX = self.COM_BUFF_TX.encode('utf-8')
                        self.ser.write(self.COM_BUFF_TX)
                        self.ser.flush()
                        time.sleep(0.5)
                        self.COM_BUFF_TX = ''

                else:
                    break

        except Exception as e:
            self.db = dbmanager.closeDB(self.db)
            print "Error:", e

def main():
    print 'Start Init COM object'
    objCOM = ClassCOM()
    objCOM.ComOpen()
    objCOM.run()



if __name__ == '__main__':
    main()





