import DB_Manager
import serial
import time
import string


class ClassCOM():

    COM_BUFF_OUT=''
    COM_BUFF_IN=''
    ser=None
    COM_READ=0
    LAST_REQ_ID=''
    firs_time=1

    def setCOM_BUFF_IN(self,cmd):
      self.COM_BUFF_IN=cmd
    
    def getCOM_BUFF_OUT(self):
      s=self.COM_BUFF_OUT
      self.COM_BUFF_OUT=''
      return s
    
    def ComOpen (self):

        Result=''        
        try:
            # configure the serial connections (the parameters differs on the device you are connecting to)
            self.ser = serial.Serial(
                port='/dev/ttyUSB0',
                baudrate=57600,
                parity=serial.PARITY_ODD,
                stopbits=serial.STOPBITS_TWO,
                bytesize=serial.SEVENBITS
                )
            if not self.ser.isOpen():
                self.ser.open()
                print 'COM: ' + port +' OPEN!'
                
        except Exception as e:
            print "Error:",e
    

    def Upd(self,db,nodo,mex):
        upd=''
        if string.find(mex,"FAIL")>-1:
            upd="Err"
            DB_Manager.update_TB_NODI(db,nodo,upd)            
        else:
            iS=string.find(mex,"P:")
            if iS>-1:
                S=mex[iS+2:]
                #print 'Segnale:',S
            ##################
            if nodo=='LUCE':
                upd=''
                if S != '':
                    if string.find(S,"1")>-1:
                        upd='On'
                        #print 'ON!!!!!!'
                    if string.find(S,"0")>-1:
                        upd='Off'
                        #print 'OFF!!!!!!'
                    if string.find(S,"9")>-1:
                        upd='?'
                        #print 'Err!!!!!!'
                    if upd != '' :
                        DB_Manager.update_TB_NODI(db,nodo,upd)                        
                        
            if nodo=='PIR':
                upd=''
                if S != '':
                    if string.find(S,"1")>-1:
                        DB_Manager.insert_TB_PRESENZE(db)
                        #print 'PRESENZA!!!!!!'
                    if string.find(S,"0")>-1:
                        upd='Disabilitato'
                        #print 'OFF!!!!!!'
                    if string.find(S,"2")>-1:
                        upd='Abilitato Suono ON'
                        #print 'OFF!!!!!!'                        
                    if string.find(S,"3")>-1:
                        upd='Abilitato Suono OFF'
                        #print 'OFF!!!!!!'                        
                    if string.find(S,"9")>-1:
                        upd='?'
                        #print 'Err!!!!!!'
                    if upd != '' :
                        DB_Manager.update_TB_NODI(db,nodo,upd)                        
            if nodo=='TV':
                upd=''
                if S != '':
                   if string.find(S,"1")==0:
                        print "Registro Temperatura"   
                        DB_Manager.insert_TB_TEMPERATURE(db,"Temp",S[1:])
                   if string.find(S,"2")==0:
                        print "Registro Hum"   
                        DB_Manager.insert_TB_TEMPERATURE(db,"Hum",S[1:])
        
    def nrf(self,db,mex):
            
        N=''
        iN=-1
        S=''
        iS=-1
        upd=''
        nodo=''
        mex=mex.strip()
        mex=mex.strip('\n')
        mex=mex.strip('\r')
        mex=mex.strip('\t')
 
        try:
            iN=string.find(mex,"H:")
            if iN>-1:
                N=mex[iN+2:iN+3]
                #print 'Nodo:',N
                if string.find(N,"1")>-1:
                    nodo='LUCE'
                if string.find(N,"2")>-1:
                    nodo='PIR'
                if string.find(N,"3")>-1:
                    nodo='TV'                    
                if nodo!='':
                    self.Upd(db,nodo,mex)
        except Exception as e:
            print "Error:",e                     
                           

    def run(self,db):
        
        out=''
        print 'Start Listen COM...'
        try:
            while 1 :
                if self.ser.isOpen():
                    try:        
                        while self.ser.inWaiting() > 0:
                            out += self.ser.read(1)
                        if out != '':
                            self.COM_READ=1
                            print 'COM RX: ' + out
                            #self.COM_BUFF_OUT=self.COM_BUFF_OUT+out
                            self.COM_BUFF_OUT=out
                            self.nrf(db,self.COM_BUFF_OUT)
                            out=''
                            
                    except Exception as e:
                        self.ser.close()
                        print "Error:",e
                        break
                    
                    time.sleep(1)
                    
                    try:
                        r=DB_Manager.select_last_TB_HTTP_REQ(db)
                        if r !='':
                            if not r[0]==self.LAST_REQ_ID:
                                if not self.LAST_REQ_ID=='':
                                    self.firs_time=0
                                    
                                self.LAST_REQ_ID=r[0]
                                #print r[0],type(r[0]),r[2],type(r[2]),r[3],type(r[3])
                                self.COM_BUFF_IN="["+str(r[2])+str(r[3])+"]"
                                self.COM_BUFF_IN=self.COM_BUFF_IN.strip()
                                self.COM_BUFF_IN=self.COM_BUFF_IN.strip('\n')
                                self.COM_BUFF_IN=self.COM_BUFF_IN.strip('\r')
                                self.COM_BUFF_IN=self.COM_BUFF_IN.strip('\t')
                                
                        if  self.COM_BUFF_IN!=''and self.COM_READ ==1 and not self.firs_time==1:
                            print 'COM TX: ' + self.COM_BUFF_IN
                            #self.ser.write(self.COM_BUFF_IN + '\r\n')
                            self.ser.write(self.COM_BUFF_IN)
                            self.COM_BUFF_IN=''
                            
                    except Exception as e:
                        self.ser.close()
                        print "Error:",e
                        break
                       
        except Exception as e:
            print "Error:",e


def main():
    
    print 'Start Init DB object'
    db=None
    db=DB_Manager.openDB(db,'Home.db')
    print 'Start Init COM object'
    objCOM=ClassCOM()
    objCOM.ComOpen()
    objCOM.run(db)
    db=DB_Manager.closeDB(db)
    

          
if __name__ == '__main__':
    main()    

