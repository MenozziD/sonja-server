
ver="1.0.1"
path='python /home/pi/Desktop/BotSonja/com.py'

cd /home/pi/Desktop/BotSonja/

if [ "$1" == "start" ];
then
 processId=$(ps -ef | grep 'com.py' | grep -v 'grep' | awk '{ printf $2 }')
 if [[ $processId ]];
 then
  echo "com gia attivo!"
 else
  if [ "$2" != "lx" ];
  then
   #python ../com.py &
   python /home/pi/Desktop/BotSonja/com.py &
  else
   lxterminal -t "comSonja" -e bash -c "$path"
  fi
  sleep 1
  processId=$(ps -ef | grep 'com.py' | grep -v 'grep' | awk '{ printf $2 }') 
  if [[ $processId ]];	
  then
   echo "com START"
  else
   echo "com ERRORE: Il comando python non ha avviato il processo!"
   exit	
  fi
 fi
fi

if [ "$1" == "stop" ];
then
 processId=$(ps -ef | grep 'com.py' | grep -v 'grep' | awk '{ printf $2 }')
 if [[ $processId ]];
 then
  sudo kill $processId
  processId=$(ps -ef | grep 'com.py' | grep -v 'grep' | awk '{ printf $2 }')
  if [[ $processId ]];	
  then
   echo "com ERRORE: Il comando kill non ha fermato il processo!"
   exit	
  else
   echo "com STOP"
  fi
 else
  echo "com non attivo!"	
 fi
fi

if [ "$1" == "pid" ];
then
 processId=$(ps -ef | grep 'com.py' | grep -v 'grep' | awk '{ printf $2 }')
 echo "com PID:" $processId	
fi

if [ "$1" == "status" ];
then
 processId=$(ps -ef | grep 'com.py' | grep -v 'grep' | awk '{ printf $2 }')
 if [[ $processId ]];
 then
  echo "com ON "
 else
  echo "com OFF"
 fi
fi

if [ "$1" == "restart" ];
then
 processId=$(ps -ef | grep 'com.py' | grep -v 'grep' | awk '{ printf $2 }')
 if [[ $processId ]];
 then
  echo "com PID:" $processId
  sudo kill $processId
  processId=$(ps -ef | grep 'com.py' | grep -v 'grep' | awk '{ printf $2 }')
  if [[ $processId ]];	
  then
   echo "com ERRORE: Il comando kill non ha fermato il processo!"
   exit	
  else
   echo "com STOP"
  fi
  if [ "$2" != "lx" ];
  then
   python /home/pi/Desktop/BotSonja/com.py &
  else
   lxterminal -t "comSonja" -e bash -c "$path"
  fi
  sleep 1
  processId=$(ps -ef | grep 'com.py' | grep -v 'grep' | awk '{ printf $2 }')
  if [[ $processId ]];	
  then
   echo "com RESTART"
  else
   echo "com ERRORE: Il comando python non ha avviato il processo!"
   exit	
  fi
 fi
fi

if [ "$1" == "version" ];
then
 echo "comcmd " $ver
fi


